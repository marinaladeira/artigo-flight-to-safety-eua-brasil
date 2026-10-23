# Resumo das fontes de dados

Este arquivo explica de onde vem cada série baixada por `01_coleta.ipynb`, o que ela representa economicamente e qual papel cumpre na análise. As decisões e suas justificativas estão no `plano-de-trabalho.md` (seções 3.1 e 3.2).

## Visão geral

O artigo compara dois casos (YIN, 2015). Para cada país, a análise precisa de um **ativo de risco** (índice de ações), de um **título público** (o candidato a porto seguro) e de **variáveis que identificam crises**. No Brasil, a análise usa ainda o **câmbio**, como controle.

| Papel na análise | EUA (caso de referência) | Brasil (caso contrastante) |
|---|---|---|
| Ativo de risco | S&P 500 | Ibovespa |
| Título público (principal) | Treasury nominal de 10 anos | IMA-B (carteira de NTN-B) |
| Identificação de crise | VIX > 30; drawdown do S&P 500 | VIX > 30 (crise global); drawdown do Ibovespa (crise local) |
| Controle | não se aplica | Câmbio USD/BRL (PTAX) |
| Robustez | TIPS 10 anos; ETF IEF | IMA-B 5+, IDkA IPCA 10A, IRF-M; câmbio de fechamento (BRL=X) |

**Amostra:** de set. 2003 (início do IMA-B) até a data mais recente. A coleta começa em set. 2002 para que o drawdown sobre o pico de 252 dias já possa ser calculado no primeiro dia da amostra.

**Frequência:** diária. Só entram os dias úteis comuns aos dois países.

## Fontes, uma a uma

### Federal Reserve, publicação H.15 (*Selected Interest Rates*)

| Série | Código | O que é |
|---|---|---|
| Treasury 10 anos | `RIFLGFCY10_N.B` | Taxa (yield) nominal do título do Tesouro americano de 10 anos, vencimento constante, em % a.a. Equivale ao DGS10 do FRED |
| TIPS 10 anos | `RIFLGFCY10_XII_N.B` | Taxa real do título americano de 10 anos indexado à inflação, vencimento constante, em % a.a. Equivale ao DFII10 do FRED |

- **Treasury 10 anos:** é o porto seguro clássico da literatura de *flight to quality* (BAUR; LUCEY, 2009; BAELE et al., 2020). Sustenta a **P1** e a **P2**. Como o H.15 publica a taxa, e não o preço, o retorno diário é o de um título de 10 anos ao par reprecificado a cada dia (inclui *carry*, duration e convexidade). Detalhes em `plano-processamento.md`.
- **TIPS 10 anos:** entra na robustez. A NTN-B é um título real (indexado ao IPCA), enquanto o Treasury de 10 anos é nominal. O TIPS permite comparar títulos reais nos dois países.

**Por que não o FRED:** o FRED só republica essas séries (a fonte indicada por ele é o próprio H.15). Em 21/10/2026 o site estava em manutenção sem previsão de volta, então a coleta passou a usar a fonte primária. O FRED também tem o S&P 500 (série `SP500`), mas só com os últimos 10 anos, por causa da licença da S&P Dow Jones Indices.

**Formato:** o pacote completo do H.15 vem em zip, com um XML no padrão SDMX. Dias sem dado aparecem como `OBS_STATUS="ND"` e valor −9999.

### Cboe

| Série | Arquivo | O que é |
|---|---|---|
| VIX | `VIX_History.csv` (coluna `CLOSE`) | Volatilidade implícita de 30 dias das opções do S&P 500, calculada e publicada pela Cboe. Equivale ao VIXCLS do FRED |

- **VIX:** é a medida de aversão a risco global. Serve para três coisas: (1) definir crise global (VIX > 30; percentil 90 na robustez), em **P1** e **P4**; (2) servir como variável contínua de incerteza na **P2**, em que a correlação ações x títulos é regredida sobre o VIX (CONNOLLY; STIVERS; SUN, 2005); (3) separar crises globais de locais no Brasil.

### Yahoo Finance (biblioteca `yfinance`)

| Série | Código | O que é | Fonte primária |
|---|---|---|---|
| S&P 500 | `^GSPC` | Índice das 500 maiores empresas americanas, só preço (sem dividendos) | S&P Dow Jones Indices |
| Ibovespa | `^BVSP` | Principal índice de ações da B3, de retorno total (reinveste proventos) | B3 |
| ETF IEF | `IEF` | Fundo de índice com Treasuries de 7 a 10 anos (preço de mercado) | iShares/BlackRock |
| USD/BRL de fechamento | `BRL=X` | Câmbio R$/US$ no fim do dia (desde dez. 2003) | mercado de câmbio |

- **S&P 500:** ativo de risco do caso de referência (**P1**, **P2**). Também gera o drawdown americano, para que o critério de crise seja simétrico entre os países.
- **Ibovespa:** ativo de risco do caso brasileiro (**P2**, **P3**, **P4**). O drawdown do Ibovespa (≤ −20% sobre o pico de 252 dias) define a **crise local**. "Só crise local" corresponde a drawdown sem VIX acima do limiar, o que é central para a **P4**.
- **IEF:** serve só para conferência. Como é um preço de mercado, mostra se a conversão do yield de 10 anos em retorno está razoável. Na base atual, a correlação entre os dois retornos diários é 0,967.
- **BRL=X:** robustez da P3. A PTAX é medida entre 10h e 13h, e o `BRL=X` é o câmbio de fim de dia, mais sincronizado com ações e títulos. Tem erros pontuais (saltos que se revertem no dia seguinte); as observações que se afastam mais de 5% da PTAX do mesmo dia são descartadas no processamento (6 casos).

**Diferença entre os índices de ações:** o `^GSPC` é índice de preço e o Ibovespa é de retorno total. Em retornos diários, o efeito dos dividendos é muito pequeno e praticamente não altera correlações, mas a diferença deve ser mencionada na metodologia.

**Cuidado:** o Yahoo pode revisar dados antigos. Por isso o arquivo bruto é guardado com a data do download e o hash no manifesto.

### ANBIMA (ANBIMA Data, histórico completo)

| Série | Código | O que é | Desde |
|---|---|---|---|
| IMA-B | `IMAB` | Carteira de mercado de todas as NTN-B (títulos públicos indexados ao IPCA) | 16/09/2003 |
| IMA-B 5+ | `IMAB5MAIS` | NTN-B com vencimento acima de 5 anos | 16/09/2003 |
| IDkA IPCA 10A | `IDKAIPCA10A` | Carteira sintética de NTN-B com prazo fixo de 10 anos | 30/12/2005 |
| IRF-M | `IRFM` | Carteira de títulos prefixados (LTN e NTN-F) | 01/02/2000 |

Os arquivos trazem o número-índice diário (retorno total), as variações e, para os IMA, a duration em dias úteis.

- **IMA-B:** é a série principal do título público brasileiro (**P2**, **P3**, **P4**). Como já é um índice de retorno total, o retorno diário sai direto do número-índice, sem precisar converter taxa em preço. A hipótese do artigo é que, por carregar risco-país, a NTN-B se comporta como ativo de risco em crises (DUFOUR; STANCU; VAROTTO, 2017; HOFMANN; SHIM; SHIN, 2020), ou seja, cai junto com o Ibovespa.
- **IMA-B 5+:** robustez. A duration é mais longa (cerca de 2.400 d.u., perto de 9,7 anos, contra cerca de 1.750 d.u., perto de 7 anos, do IMA-B), o que a aproxima do Treasury de 10 anos.
- **IDkA IPCA 10A:** robustez com prazo fixo de 10 anos, a mesma lógica de vértice usada por Cardoso e Garcia (2023). A série começa só em dez. 2005, então essa robustez tem amostra um pouco mais curta.
- **IRF-M:** robustez com títulos prefixados (nominais). Testa se o resultado da P3 depende de o título ser indexado à inflação.

**Observação:** o SGS do Banco Central também publica o IMA-B (séries 12466 a 12468), mas essas séries param em 22/05/2023.

### Banco Central do Brasil (SGS)

| Série | Código | O que é |
|---|---|---|
| PTAX venda | `1` | Taxa de câmbio R$/US$ de referência, calculada pelo Banco Central |

- **PTAX:** é o controle da **P3**. Em crises, o real se desvaloriza junto com a queda das ações e dos títulos. A pergunta é se a correlação positiva entre Ibovespa e NTN-B sobrevive depois de retirar o efeito do câmbio, por correlação parcial ou regressão. A PTAX também permite converter os retornos brasileiros para dólar, como robustez.

**Observação:** a série 7 do SGS (Ibovespa) foi descontinuada em 30/09/2019 e por isso não é usada.

## O que sai da coleta

Cada execução do notebook cria a pasta `dados/brutos/AAAA-MM-DD/` com:

| Arquivo | Conteúdo |
|---|---|
| `h15_completo.zip` | Pacote completo do H.15 (XML), com o Treasury e o TIPS de 10 anos |
| `cboe_vix.csv` | VIX: abertura, máxima, mínima e fechamento |
| `yahoo_gspc.csv`, `yahoo_bvsp.csv`, `yahoo_ief.csv`, `yahoo_brlx.csv` | Abertura, máxima, mínima, fechamento, fechamento ajustado e volume |
| `anbima_*.xlsx` | Histórico completo de cada índice ANBIMA |
| `sgs_1.json` | PTAX de venda (data e valor) |
| `manifesto.csv` | Fonte, URL, período, número de observações e hash SHA-256 de cada arquivo |

Nenhum valor é alterado nesta etapa. Alinhamento de datas, retornos e variáveis de crise ficam para o `02_processamento.ipynb`; a lista completa de colunas da base está em `dados/dicionario.md`.

## Da série bruta à variável da análise

| Variável no processamento | Série de origem | Transformação prevista |
|---|---|---|
| `r_sp500` | `^GSPC` (Close) | log-retorno diário |
| `r_treasury` | `RIFLGFCY10_N.B` (H.15) | reprecificação diária de título de 10 anos ao par |
| `r_ibov` | `^BVSP` (Close) | log-retorno diário |
| `r_ntnb` | IMA-B (número-índice) | log-retorno diário |
| `r_usdbrl` | PTAX venda | log-retorno diário |
| `vix` | Cboe (`CLOSE`) | nível |
| `crise_global` | Cboe (`CLOSE`) | VIX > 30 |
| `crise_local_br` | `^BVSP` | drawdown ≤ −20% sobre o pico de 252 dias |
| `crise_eua` | `^GSPC` | drawdown ≤ −20% sobre o pico de 252 dias |
| `so_local`, `so_global`, `ambas` | combinações acima | indicadores de regime (P4) |
