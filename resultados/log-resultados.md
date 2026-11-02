# Log de resultados (etapa 4)

Gerado a partir de `codigo/04_analise.ipynb` sobre `dados/processados/base_diaria.csv` (2003-09-17 a 2026-09-30, 5.525 dias com retorno). Primeira rodada em 2026-11-02. Números arredondados; os valores completos estão nos CSV de `resultados/`.

**Como ler.** "Correlação no regime" é a correlação de Pearson dos retornos diários dos dias daquele regime. O IC 95% e o p do bootstrap vêm de um bootstrap em blocos circular (blocos de 21 pregões, 2.000 réplicas, semente fixa), que respeita a dependência entre dias seguidos. O z de Fisher supõe dias independentes e por isso é só complementar. Em estudo de caso, o resultado é "proposição sustentada ou não", e os testes dão suporte à leitura (plano, etapa 4).

**Reprodutibilidade (etapa 3).** Em 2026-11-02 o `02_processamento.ipynb` foi rodado do zero, em outra máquina, a partir de `dados/brutos/2026-10-21`. A base gerada é idêntica à do repositório (mesmas 5.526 linhas e 47 colunas, diferença máxima 0).

## Resumo dos vereditos

| Proposição | Veredito | Número-chave |
|---|---|---|
| P1 | Sustentada, com ressalva | Correlação em crise −0,36 contra −0,24 no normal; diferença −0,12 (IC95% bootstrap [−0,22; −0,00]) |
| P2 | Sustentada | EUA: b = −0,0078 por ponto de VIX (p < 0,001). Brasil: b = +0,0023 (p = 0,36) |
| P3 | Sustentada, com ressalva | Crise: +0,43 (+0,36 com controle da PTAX). Mas o normal também é positivo (+0,39) |
| P4 | Não sustentada (sinal oposto) | Só local +0,18 contra só global +0,43; diferença −0,25 (IC95% [−0,43; −0,11]) |
| 2022 | Correlação EUA ficou positiva | EUA +0,20 em 2022 contra −0,28 em 2018–2023 sem 2022 |

## P1 · EUA, crise x período normal

Crise = `crise_p1_eua` (VIX > 30 ou drawdown do S&P 500 ≤ −20%), 524 dias. Normal = o resto, 5.001 dias.

| | Crise | Normal | Diferença | IC95% bootstrap da diferença | p bootstrap | p Fisher |
|---|---|---|---|---|---|---|
| S&P 500 x Treasury | −0,361 | −0,241 | −0,120 | [−0,225; −0,002] | 0,048 | 0,004 |

- A correlação é negativa em crise e mais negativa que no período normal, como prevê a P1.
- **Ressalva 1 (volatilidade):** com o ajuste de Forbes e Rigobon (2002), a correlação de crise vai a −0,12, menos negativa que a do normal. Parte da diferença pode vir só do aumento da volatilidade. Lembrar que o ajuste exige condições pouco plausíveis em crise (ver revisão, seção 2.2).
- **Ressalva 2 (bootstrap):** com blocos de 63 pregões, o IC passa a incluir zero (p = 0,059).
- Robustez: VIX p90 (−0,37 x −0,23, p = 0,02), só VIX > 30 (−0,39 x −0,23, p = 0,01) e IEF no lugar do Treasury (−0,39 x −0,23, p = 0,02) confirmam. **Com o TIPS, não há diferença** (−0,09 x −0,12, p = 0,66): a proteção vem do título nominal.
- Nos EUA o período normal também tem correlação negativa (−0,24), o que bate com Campbell, Sunderam e Viceira (2017) e Molenaar et al. (2024) para o pós-2000.

## P2 · Correlação móvel x VIX (Newey-West, 63 defasagens)

Regressão da correlação móvel de 63 pregões sobre o VIX do dia.

| País | b (por ponto de VIX) | EP Newey-West | p | R² |
|---|---|---|---|---|
| EUA | −0,0078 | 0,0020 | < 0,001 | 0,04 |
| Brasil | +0,0023 | 0,0025 | 0,36 | 0,01 |

- Nos EUA a correlação cai quando o VIX sobe (VIX 10 pontos mais alto ≈ correlação 0,08 menor). No Brasil, o coeficiente é nulo. A diferença entre os países é significativa (regressão de corr BR − corr EUA sobre o VIX: b = +0,010, p = 0,002).
- Robusto a: correlação futura de 22 pregões, como em Connolly, Stivers e Sun (2005) (EUA −0,0079, p < 0,001; Brasil −0,0017, p = 0,43); tendência linear; log do VIX; janelas de 21 e 126 pregões. Em nenhum caso o Brasil fica significativo.
- O R² é baixo nos EUA, como em Connolly et al.: o VIX explica a direção, não a maior parte da variação.

## P3 · Brasil em crise, com controle do câmbio

Crise = `crise_local_br` ou `crise_global` (840 dias). Normal = nenhuma das duas (4.685 dias).

| | Crise | Normal | Diferença | IC95% bootstrap da diferença |
|---|---|---|---|---|
| Ibovespa x NTN-B | +0,430 | +0,387 | +0,043 | [−0,18; +0,21] |
| Parcial, controle PTAX | +0,364 | +0,298 | +0,067 | [−0,14; +0,25] |
| Parcial, controle BRL=X | +0,419 | +0,393 | +0,026 | [−0,20; +0,22] |

- Em crise, a NTN-B anda junto com o Ibovespa (correlação positiva), e isso se mantém com o câmbio como controle. Na regressão r_ntnb = a + b·r_ibov + c·r_câmbio em crise, b = +0,089 (p < 0,001).
- **Ressalva:** a correlação é positiva também fora de crise, e a diferença crise x normal não é significativa. A NTN-B se comporta como ativo de risco **sempre**, não só em crise. Isso é ainda mais forte que a P3, mas muda a frase: o achado é "a NTN-B nunca funciona como porto seguro", e não "deixa de funcionar em crise".
- Robustez: IMA-B 5+ (+0,37), IDkA IPCA 10A (+0,37), IRF-M (+0,34, título prefixado), retornos em dólar (+0,78) e VIX p90 (+0,36) dão o mesmo resultado. O sinal positivo não depende do índice nem de o título ser indexado à inflação.
- Contraste com os EUA (replicação teórica): em crise, −0,36 nos EUA contra +0,43 no Brasil.

## P4 · Só crise local x só crise global

| | Só local (418 dias) | Só global (111 dias) | Diferença | IC95% bootstrap | p bootstrap |
|---|---|---|---|---|---|
| Ibovespa x NTN-B | +0,181 | +0,431 | −0,250 | [−0,43; −0,11] | 0,001 |
| Parcial, controle PTAX | +0,163 | +0,323 | −0,160 | [−0,40; 0,00] | 0,051 |

- O resultado vai **contra** a P4: nas fases de "só crise local" a correlação é **menor** que nas de "só crise global" e menor que no período normal (+0,18 x +0,39, p < 0,001).
- O mesmo vale com VIX p90 (−0,30), excluindo a cauda de crise global (a) (−0,30), com o IMA-B 5+ (−0,24) e com blocos de 63 pregões. Com choque de 21 pregões (c), IRF-M e retornos em dólar a diferença some (não significativa).
- **A exceção é a lista fixa de eventos locais (b):** nos 84 pregões após os 4 eventos (rebaixamento de 2015, impeachment, Joesley Day, greve dos caminhoneiros), a correlação é +0,64, acima da crise global (+0,43), mas sem significância (p = 0,50) e com amostra muito pequena.
- **Leitura (interpretação):** o drawdown de −20% do Ibovespa marca fases longas de bolsa em queda (2008 fora do pico do VIX, 2013–2016, 2021–2022), e não choques de risco-país. Em choques locais agudos o padrão previsto aparece, mas a amostra é pequena. Decisão para o grupo: manter a P4 com veredito "não sustentada", ou reformular a crise local (CDS de 5 anos > 2%, como sugerem as notas do `artigo.md`, o que exige baixar o CDS).

## 2022 (exploratória)

| | 2022 | 2018–2023 sem 2022 | Diferença | IC95% bootstrap |
|---|---|---|---|---|
| EUA: S&P 500 x Treasury | +0,197 | −0,279 | +0,476 | [+0,25; +0,66] |
| Brasil: Ibovespa x NTN-B | +0,490 | +0,655 | −0,165 | [−0,37; +0,07] |

- Nos EUA, 2022 é o primeiro ano desde 2006 com correlação anual positiva, e depois oscilou perto de zero (2023 +0,09, 2024 +0,06, 2025 −0,15), chegando a +0,43 em 2026 até setembro. Isso confirma o sinal que as notas do `artigo.md` pediam para checar e bate com Mosk, Pangallo e Zema (2022).
- No Brasil, 2022 não destoa: a correlação já era positiva e ficou no patamar dos anos vizinhos.
- Ou seja, em 2022 o Treasury passou a se comportar como a NTN-B. Ver `figuras/figura2_correlacao_por_ano.png` e `resultados/correlacao_por_ano.csv`.

## Robustez: o que já foi rodado

| Item do plano (4.3) | Situação |
|---|---|
| Janelas de 21 e 126 dias | Rodado na P2 (`p2_regressoes_vix.csv`). A figura usa 63 |
| Limiares alternativos de crise | VIX p90 e só VIX > 30 (P1, P3, P4); robustezes (a), (b), (c) da crise local (P4) |
| Datas de crise fixas da literatura | Parcial: só a lista fixa de eventos locais (preliminar). Falta lista de crises globais da literatura |
| IRF-M no lugar da NTN-B | Rodado (P3, P4); também IMA-B 5+ e IDkA IPCA 10A |
| TIPS no lugar do Treasury | Rodado (P1): sem diferença crise x normal |
| Retornos em USD para o Brasil | Rodado (P3, P4) |
| Ajuste de Forbes e Rigobon | Rodado (coluna `r_a_forbes_rigobon` em `testes_proposicoes.csv` e `robustez.csv`) |

## Arquivos

- `codigo/04_analise.ipynb`: todo o código desta etapa.
- `resultados/testes_proposicoes.csv`, `robustez.csv`, `p2_regressoes_vix.csv`, `p3_regressoes.csv`, `correlacao_por_ano.csv`, `correlacoes_moveis.csv`, `correlacao_movel_media_por_regime.csv`.
- `figuras/figura1_correlacao_movel.png` (figura central) e `figuras/figura2_correlacao_por_ano.png`.
