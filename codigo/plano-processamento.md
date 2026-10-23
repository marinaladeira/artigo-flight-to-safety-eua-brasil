# Plano de processamento dos dados

Este plano descreve o que o notebook `02_processamento.ipynb` deve fazer com os arquivos brutos baixados por `01_coleta.ipynb`. A meta é chegar a `dados/processados/base_diaria.csv`. O diagnóstico abaixo foi feito sobre a coleta de 21/10/2026 (`dados/brutos/2026-10-21/`). O notebook já foi implementado e roda do início ao fim.

As decisões de fundo (fontes, início da amostra, limiares, feriados) estão no `plano-de-trabalho.md`, seção 3.1. O papel de cada fonte na análise está em `codigo/resumo.md`.

## 1. Visão geral do fluxo

1. **Leitura e padronização:** ler cada arquivo bruto e gerar uma série com índice de data e nome de coluna padronizado.
2. **Variáveis de crise no calendário próprio:** calcular os drawdowns de cada índice de ações no calendário da sua bolsa, antes de alinhar.
3. **Alinhamento:** manter só os dias úteis comuns aos dois países e às séries principais.
4. **Retornos:** calcular os retornos a partir dos **níveis** já alinhados, nunca a partir de retornos diários calculados antes.
5. **Variáveis de regime:** montar `crise_global`, `crise_local_br`, `so_local`, `so_global` e `ambas`.
6. **Recorte da amostra e verificações:** aplicar as datas de início e fim e rodar as checagens de qualidade (seção 6).
7. **Saídas:** salvar a base, o dicionário de variáveis e um log de tratamento.

## 2. Diagnóstico e tratamento por dataset

### 2.1 Yahoo Finance: `yahoo_gspc.csv`, `yahoo_bvsp.csv`, `yahoo_ief.csv`

**Colunas disponíveis:** `Date`, `Adj Close`, `Close`, `High`, `Low`, `Open`, `Volume`.

| Arquivo | Coluna usada | Nome padronizado | Por quê |
|---|---|---|---|
| `yahoo_gspc.csv` | `Close` | `sp500` | Nível do S&P 500. Para índices, `Adj Close` = `Close` (conferido) |
| `yahoo_bvsp.csv` | `Close` | `ibov` | Nível do Ibovespa (já é índice de retorno total) |
| `yahoo_ief.csv` | `Adj Close` | `ief` | Preço ajustado por dividendos (difere do `Close` em 6.058 dias), ou seja, retorno total do ETF |

**O que o diagnóstico encontrou:**

- Sem valores ausentes, sem datas duplicadas, sem preços ≤ 0 e sem `High` < `Low`.
- Retornos diários acima de 10% em módulo só em out. 2008 e mar. 2020. São eventos reais, não erros.
- `Volume` = 0 em 1.058 dias do Ibovespa. Não afeta nada, porque o volume não é usado.
- A maior lacuna entre datas é de 6 dias corridos no Ibovespa (Carnaval de 2012), o que é esperado.

**Tratamentos:**

- Descartar `Open`, `High`, `Low` e `Volume`.
- Converter `Date` para data, sem hora nem fuso.
- Não aplicar winsorização nem excluir *outliers*: os extremos coincidem com crises, que são justamente o objeto do estudo.

### 2.2 ANBIMA: `anbima_IMAB.xlsx`, `anbima_IMAB5MAIS.xlsx`, `anbima_IDKAIPCA10A.xlsx`, `anbima_IRFM.xlsx`

**Colunas disponíveis:** `Índice`, `Data de Referência`, `Número Índice`, `Variação Diária (%)`, `Variação no Mês (%)`, `Variação no Ano (%)`, `Variação 12 Meses (%)`, `Variação 24 Meses (%)`, `Duration (d.u.)` e `PMR`. O IDkA não tem `Variação 24 Meses (%)`, `Duration (d.u.)` nem `PMR`.

| Arquivo | Colunas usadas | Nomes padronizados |
|---|---|---|
| `anbima_IMAB.xlsx` | `Data de Referência`, `Número Índice`, `Duration (d.u.)` | `imab`, `imab_duration_anos` |
| `anbima_IMAB5MAIS.xlsx` | idem | `imab5mais`, `imab5mais_duration_anos` |
| `anbima_IDKAIPCA10A.xlsx` | `Data de Referência`, `Número Índice` | `idka10` |
| `anbima_IRFM.xlsx` | `Data de Referência`, `Número Índice`, `Duration (d.u.)` | `irfm`, `irfm_duration_anos` |

**O que o diagnóstico encontrou:**

- **A coluna `Índice` muda de grafia** ao longo do arquivo (`IMA-B` e `IMA - B`; `IRF-M` e `IRF - M`). Não usar essa coluna para filtrar.
- **A coluna `Variação Diária (%)` tem erros.** No IRF-M aparece 336,78% em 09/04/2021, quando o número-índice mostra −0,24%. No IDkA, a variação de 16/07/2021 não bate com o número-índice, nem a do IRF-M em 04/01/2005. **Regra: calcular os retornos sempre pelo `Número Índice`.** Nos demais dias, as duas colunas batem até a 4ª casa decimal.
- **Faltam alguns dias no IRF-M em 2002** (por exemplo, 24/09 e de 27/09 a 30/09/2002). Fica fora da amostra (que começa em set. 2003), mas o log deve registrar o fato.
- **A `Duration (d.u.)` só existe a partir de 31/03/2005** no IMA-B e no IMA-B 5+. Há um valor 0 no IRF-M (12/05/2004), que deve ser tratado como ausente.
- O IDkA IPCA 10A começa em 30/12/2005.
- **A ANBIMA publica o índice em dias sem pregão na B3**: são 78 dias na amostra, como 25/01 e 09/07 (feriados de São Paulo), 20/11, 24/12 e 31/12. Esses dias saem no alinhamento (seção 3).
- O maior movimento do IMA-B foi de −7,8% em 18/05/2017 (Joesley Day), e do IMA-B 5+, de −10,2% no mesmo dia. São eventos reais.

**Tratamentos:**

- Descartar as colunas de variação acumulada e o `PMR`.
- Converter a duration de dias úteis para anos: `duration_anos = Duration (d.u.) / 252`. Usar só em estatísticas descritivas e para justificar a comparação de prazos com o Treasury.
- Trocar o 0 de duration por ausente.

### 2.3 Banco Central (SGS): `sgs_1.json`

**Estrutura:** lista de registros `{"data": "dd/mm/aaaa", "valor": "x.xxxx"}`. **O valor vem como texto.**

| Coluna | Tratamento | Nome padronizado |
|---|---|---|
| `data` | converter com o formato `%d/%m/%Y` | índice |
| `valor` | converter de texto para número | `usdbrl` |

**O que o diagnóstico encontrou:**

- Sem valores ausentes nem datas duplicadas. Existe PTAX em todos os dias com Ibovespa e IMA-B.
- Há 33 dias com variação zero, a maioria em 31/12, quando a PTAX repete a do dia anterior. Esses dias saem no alinhamento, porque a B3 não abre em 31/12.
- **A PTAX não é um preço de fechamento.** Ela é a média de quatro consultas feitas pelo Banco Central entre 10h e 13h. Ações e títulos são medidos no fim do dia. Na P3, isso pode enfraquecer o controle pelo câmbio. Proposta de robustez: usar o câmbio de fechamento (Yahoo, `BRL=X`) e comparar. Para isso, o ticker precisa entrar na coleta.

### 2.4 Federal Reserve (H.15) e Cboe: `h15_completo.zip`, `cboe_vix.csv`

O FRED estava em manutenção em 21/10/2026, e a coleta passou a usar as fontes primárias das mesmas séries (decisão registrada no `plano-de-trabalho.md`, seção 3.1).

**H.15:** zip com o XML (`H15_data.xml`, padrão SDMX) de toda a publicação. Cada série é um elemento `Series` com `SERIES_NAME`; cada observação é um `Obs` com `TIME_PERIOD`, `OBS_VALUE` e `OBS_STATUS`.

**Cboe:** CSV com `DATE` (formato mm/dd/aaaa), `OPEN`, `HIGH`, `LOW` e `CLOSE`.

| Origem | Série / coluna usada | Nome padronizado | Unidade |
|---|---|---|---|
| H.15 | `RIFLGFCY10_N.B` | `y_treasury10` | % a.a. |
| H.15 | `RIFLGFCY10_XII_N.B` | `y_tips10` | % a.a. (real) |
| Cboe | `CLOSE` | `vix` | pontos |

**O que o diagnóstico encontrou:**

- No H.15, os dias sem dado têm `OBS_STATUS="ND"` e valor −9999 (261 no Treasury e 255 no TIPS desde set. 2002). Viram ausentes.
- O VIX da Cboe não tem ausentes, duplicatas nem valores ≤ 0 (mínimo 9,1; máximo 82,7).

**Tratamentos e cuidados:**

- Ler o XML com leitura incremental (o arquivo tem 70 MB) e extrair só as duas séries.
- **O mercado de títulos americano fecha em dias em que a bolsa abre**, como o Columbus Day e o Veterans Day. Nesses dias, o yield fica vazio enquanto o S&P 500 tem preço. Esses dias saem no alinhamento (40 dias na amostra).
- **Conversão de yield em retorno (decidido):** reprecificar todo dia um título de 10 anos ao par, com cupom semestral. O título tem cupom igual à taxa do dia anterior e é avaliado à taxa do dia, com prazo reduzido pelo tempo decorrido (τ = dias corridos / 365), mais o cupom corrido. Isso inclui *carry* e convexidade, e a duration fica implícita na fórmula. A aproximação y·τ − D·Δy, com D modificada do título ao par, fica na base como conferência (`r_treasury_aprox`). Resultado: correlação de 0,967 com o IEF e de 1,000 com a aproximação.
- O mesmo tratamento se aplica ao TIPS. Como o yield real ficou negativo em 2012-13 e 2020-21, a fórmula trata o caso de taxa próxima de zero.

### 2.5 Yahoo Finance: `yahoo_brlx.csv` (câmbio de fechamento)

Mesmas colunas dos outros arquivos do Yahoo; usa-se `Close` (nome `usdbrl_fech`). A série começa em 01/12/2003.

**O que o diagnóstico encontrou:** saltos isolados que se revertem no dia seguinte, e alguns valores parados (por exemplo, 18/05/2017, quando o `BRL=X` repete o nível anterior ao Joesley Day). Também há dias faltando (por exemplo, 20 a 23/03/2006).

**Tratamento:** descartar as observações que se afastam mais de 5% da PTAX do mesmo dia (6 casos: 08/05/2006, 14/07/2006, 16/08/2006, 27/01/2012, 18/05/2017 e 11/05/2020). Diferenças menores são esperadas, porque a PTAX é medida entre 10h e 13h.

## 3. Alinhamento de datas

**Regra (decisão 3.1):** só os dias úteis comuns aos dois países.

**Calendário de referência:** a interseção das datas de `sp500`, `y_treasury10`, `vix`, `ibov`, `imab` e `usdbrl`. As séries de robustez (IMA-B 5+, IDkA, IRF-M, TIPS, IEF) entram por *left join* nesse calendário e não reduzem a base principal.

**Números do diagnóstico (16/09/2003 a 20/10/2026, antes de incluir o yield e o VIX):**

| Série | Dias |
|---|---|
| S&P 500 | 5.811 |
| Ibovespa | 5.723 |
| IMA-B | 5.801 |
| PTAX | 5.801 |
| **Comuns (sem yield e VIX)** | **5.579** |

- Isso equivale a 97,5% dos dias brasileiros e 96,0% dos americanos. Com o yield de 10 anos e o VIX, a base final fica com 5.526 dias úteis comuns entre 16/09/2003 e 30/09/2026.
- Dias com bolsa só nos EUA: 232. Dias com bolsa só no Brasil: 144.

**Ponto crítico:** calcular os retornos **depois** de alinhar os níveis. Se o retorno de um dia que vai ser excluído for calculado antes do alinhamento, o movimento daquele dia some da base. Calculando sobre os níveis alinhados, o retorno do dia seguinte acumula os dois dias, para as duas séries ao mesmo tempo. Na base final, 418 retornos cobrem mais de um dia útil. Isso será informado na metodologia.

**Horário de medição:** a B3 fecha às 17h ou 18h de Brasília, perto das 16h de Nova York, então os fechamentos são quase simultâneos. A defasagem entre os países não é corrigida, mas é citada como limitação.

## 4. Transformações

| Variável | Origem | Transformação |
|---|---|---|
| `r_sp500` | `sp500` | 100 · ln(P_t / P_{t−1}) |
| `r_ibov` | `ibov` | idem |
| `r_ntnb` | `imab` | idem |
| `r_ntnb5mais`, `r_idka10`, `r_irfm` | ANBIMA | idem (robustez) |
| `r_ief` | `ief` | idem (conferência do Treasury) |
| `r_usdbrl` | `usdbrl` | idem. Positivo significa real se desvalorizando |
| `r_treasury` | `y_treasury10` | reprecificação de um título ao par (seção 2.4), em % (log) |
| `r_tips` | `y_tips10` | idem (robustez) |
| `r_ibov_usd`, `r_ntnb_usd` | `r_ibov` ou `r_ntnb` menos `r_usdbrl` | retornos em dólar (robustez) |
| `vix` | Cboe | nível, sem transformação |

Os retornos ficam em % (log-retorno × 100). A 1ª observação de cada série fica vazia.

## 5. Variáveis de crise

Os drawdowns são calculados **no calendário próprio de cada bolsa, antes do alinhamento**, para que a janela de 252 dias corresponda a 252 pregões de verdade. A coleta começa em set. 2002, então a janela já está completa em set. 2003.

| Variável | Definição |
|---|---|
| `dd_ibov` | Ibovespa_t / máximo dos últimos 252 pregões − 1 |
| `dd_sp500` | idem, para o S&P 500 |
| `crise_global` | VIX > 30 |
| `crise_global_p90` | VIX acima do percentil 90 da amostra (robustez) |
| `crise_local_br` | `dd_ibov` ≤ −20% |
| `crise_eua` | `dd_sp500` ≤ −20% (simetria) |
| `so_local` | `crise_local_br` e não `crise_global` |
| `so_global` | `crise_global` e não `crise_local_br` |
| `ambas` | `crise_local_br` e `crise_global` |
| `normal` | nenhuma das anteriores |
| `crise_p1_eua` | `crise_global` ou `crise_eua` (crise de aversão a risco nos EUA, para a P1) |

**Prévia da contagem de dias** (calculada com o VIX do Yahoo, `^VIX`, antes da base final; set. 2003 a set. 2026, 5.565 dias). A contagem da base final, com o VIX da Cboe e as robustezes (a) a (c), está em `dados/processados/log_processamento.md` (por exemplo, 418 dias de `so_local`, 296 de `so_local_sem_cauda` e 182 de `so_local_choque`):

| Regime | VIX > 30 | VIX > p90 |
|---|---|---|
| `crise_global` | 428 | 555 |
| `crise_local_br` | 732 | 732 |
| `so_local` | 418 | 378 |
| `so_global` | 114 | 201 |
| `ambas` | 314 | 354 |
| `crise_eua` (drawdown do S&P 500) | 317 | 317 |

**O que a prévia mostra para a P4 (a discutir com o grupo):**

- **Há dias suficientes de "só crise local"** (cerca de 400). O risco de amostra pequena, apontado no plano, não se confirma.
- **Contaminação por crises globais:** o drawdown de 252 dias é uma variável persistente. Depois que o VIX volta para baixo de 30, o Ibovespa continua abaixo de −20% por semanas. Exemplos: ago. 2008 (antes do pico do VIX), maio a jul. 2009 e maio a jun. 2020. Esses dias aparecem como "só local", mas são a cauda de crises globais.
- **Classificações duvidosas:** o *taper tantrum* (jun. a ago. 2013, 44 dias) teve origem global, mas aparece como "só local" porque o VIX ficou abaixo de 30. Já o **Joesley Day (18/05/2017)**, o choque local mais claro da amostra, **não aparece**: o Ibovespa não chegou a −20% sobre o pico.
- **Propostas de robustez:** (a) excluir de `so_local` os dias até 63 pregões depois de um dia de `crise_global`; (b) usar uma lista fixa de crises locais tirada da literatura (eleição de 2002, que fica fora da amostra; perda do grau de investimento em 2015; *impeachment* em 2015-16; Joesley Day em 2017; greve dos caminhoneiros em 2018); (c) usar um critério de choque de curto prazo, como o retorno de 21 dias do Ibovespa abaixo do percentil 5.

## 6. Recorte e verificações de qualidade

**Recorte:** de 16/09/2003 (primeiro valor do IMA-B) até uma **data de corte fixa**, para que a base não mude a cada coleta. Decidido: 30/09/2026.

**Verificações automáticas, registradas no log:**

- [x] Nenhuma data duplicada e índice de datas em ordem crescente
- [x] Nenhum valor ausente nas séries principais dentro da amostra
- [x] Nenhum nível ≤ 0
- [ ] Lista dos 10 maiores retornos em módulo de cada série, conferida contra eventos conhecidos (a lista sai no log; a conferência é manual)
- [x] Correlação entre `r_treasury` e `r_ief` acima de 0,9 (valida a conversão do yield): 0,967
- [x] Retornos da ANBIMA recalculados batendo com a `Variação Diária (%)`, exceto nos dias de erro conhecidos (IRF-M em 04/01/2005 e 09/04/2021; IDkA em 16/07/2021)
- [x] Contagem de dias por regime refeita com o VIX da Cboe
- [x] Número de datas excluídas no alinhamento, por séries ausentes

## 7. Decisões (aceitas pelo grupo em 21/10/2026)

1. **Conversão do yield do Treasury:** reprecificação diária de um título de 10 anos ao par; a aproximação −D·Δy fica como conferência.
2. **Data de corte:** 30/09/2026.
3. **Câmbio de fechamento (`BRL=X`):** incluído na coleta como robustez da P3.
4. **Definição de crise local:** drawdown do Ibovespa como principal, com as robustezes (a) sem a cauda de crises globais, (b) lista fixa de eventos e (c) choque de 21 pregões. A lista fixa é **preliminar** e precisa ser validada com a literatura na etapa 2.
5. **Crise para a P1:** `crise_p1_eua` = `crise_global` ou `crise_eua`; `crise_global` sozinha fica disponível para comparação.

## 8. Saídas do `02_processamento.ipynb`

| Arquivo | Conteúdo |
|---|---|
| `dados/processados/base_diaria.csv` | Uma linha por dia comum: níveis, retornos, VIX, drawdowns e indicadores de regime |
| `dados/processados/log_processamento.md` | Origem dos brutos (pasta e hash do manifesto), dias excluídos por motivo e resultado de cada verificação |
| `dados/dicionario.md` | Nome, descrição, unidade, fonte e transformação de cada coluna |
