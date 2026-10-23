# Log do processamento

- Gerado em: 2026-10-21
- Brutos: `dados/brutos/2026-10-21` (SHA-256 do manifesto: `369a9716da30bd9d…`)
- Amostra: 2003-09-16 a 2026-09-30, 5526 dias úteis comuns
- Percentil 90 do VIX: 27.76; percentil 5 de `r21_ibov`: -10.16%
- Retornos que cobrem mais de um dia útil (seg. a sex.) por causa de dia excluído: 418

## Verificações

| verificação                                                                  | resultado   | detalhe                                                                                        |
|:-----------------------------------------------------------------------------|:------------|:-----------------------------------------------------------------------------------------------|
| Datas únicas e em ordem crescente                                            | ok          |                                                                                                |
| Sem ausentes nas séries principais (após a 1ª linha)                         | ok          | nenhum                                                                                         |
| Níveis positivos                                                             | ok          |                                                                                                |
| Correlação r_treasury x r_ief > 0,9                                          | ok          | 0.967                                                                                          |
| Correlação r_treasury x r_treasury_aprox > 0,99                              | ok          | 1.0000                                                                                         |
| ANBIMA: número-índice x 'Variação Diária (%)' (dias divergentes > 0,01 p.p.) | ok          | IDKAIPCA10A 2021-07-16 (0.20 p.p.); IRFM 2005-01-04 (0.09 p.p.); IRFM 2021-04-09 (337.02 p.p.) |
| Regimes so_local/so_global/ambas/normal somam o total de dias                | ok          |                                                                                                |

## Datas excluídas na amostra, por séries principais ausentes

| séries ausentes                                   |   dias |
|:--------------------------------------------------|-------:|
| ibov, imab, usdbrl_ptax                           |    154 |
| sp500, y_treasury10, vix                          |    112 |
| ibov                                              |     74 |
| sp500, y_treasury10, vix, ibov, imab, usdbrl_ptax |     56 |
| y_treasury10                                      |     40 |
| sp500, y_treasury10                               |     29 |
| sp500, vix, ibov, imab, usdbrl_ptax               |      7 |
| sp500, y_treasury10, vix, ibov                    |      4 |
| sp500, y_treasury10, ibov, imab, usdbrl_ptax      |      4 |
| y_treasury10, ibov, imab, usdbrl_ptax             |      3 |
| sp500, vix                                        |      2 |
| sp500                                             |      1 |

## Observações descartadas do BRL=X (desvio da PTAX > 5%)

| Date                |   desvio |
|:--------------------|---------:|
| 2006-05-08 00:00:00 |  -0.0571 |
| 2006-07-14 00:00:00 |  -0.0525 |
| 2006-08-16 00:00:00 |  -0.0556 |
| 2012-01-27 00:00:00 |   0.0625 |
| 2017-05-18 00:00:00 |  -0.0732 |
| 2020-05-11 00:00:00 |  -0.0549 |

## Dias por regime

|                    |   dias |   % da amostra |
|:-------------------|-------:|---------------:|
| crise_global       |    422 |            7.6 |
| crise_global_p90   |    553 |           10   |
| crise_local_br     |    729 |           13.2 |
| crise_eua          |    314 |            5.7 |
| crise_p1_eua       |    524 |            9.5 |
| so_local           |    418 |            7.6 |
| so_global          |    111 |            2   |
| ambas              |    311 |            5.6 |
| normal             |   4686 |           84.8 |
| so_local_p90       |    378 |            6.8 |
| so_local_sem_cauda |    296 |            5.4 |
| crise_local_fixa   |     84 |            1.5 |
| choque_local_br    |    277 |            5   |
| so_local_choque    |    182 |            3.3 |

## Eventos da lista fixa de crises locais (preliminar)

- 2015-09-09: S&P retira o grau de investimento do Brasil
- 2015-12-02: Abertura do processo de impeachment na Câmara
- 2017-05-18: Joesley Day (divulgação da gravação na noite de 17/05)
- 2018-05-21: Início da greve dos caminhoneiros

## Dez maiores retornos em módulo (conferir contra eventos conhecidos)

- `r_sp500`: 2020-03-16 (-12.77%); 2008-10-14 (+10.42%); 2008-10-28 (+10.25%); 2020-03-12 (-9.99%); 2008-10-15 (-9.47%); 2008-12-01 (-9.35%); 2008-09-29 (-9.22%); 2025-04-09 (+9.09%); 2020-03-24 (+8.97%); 2020-03-13 (+8.88%)
- `r_treasury`: 2009-03-18 (+4.39%); 2009-01-02 (-3.11%); 2020-03-17 (-2.79%); 2022-11-10 (+2.45%); 2022-06-13 (-2.35%); 2008-09-15 (+2.27%); 2009-02-17 (+2.19%); 2020-03-10 (-2.14%); 2022-09-28 (+2.06%); 2008-11-25 (+2.04%)
- `r_ibov`: 2020-03-12 (-15.99%); 2008-10-14 (+15.47%); 2020-03-16 (-14.99%); 2020-03-13 (+13.02%); 2020-03-09 (-12.98%); 2008-10-28 (+12.60%); 2008-10-15 (-12.10%); 2020-03-18 (-10.92%); 2008-10-22 (-10.73%); 2008-09-29 (-9.83%)
- `r_ntnb`: 2017-05-18 (-7.82%); 2020-03-13 (+5.26%); 2020-03-12 (-4.69%); 2020-03-11 (-4.36%); 2015-09-24 (+4.18%); 2020-04-24 (-3.97%); 2020-03-18 (-3.96%); 2013-06-10 (-2.82%); 2018-10-09 (+2.79%); 2007-08-16 (-2.71%)
- `r_usdbrl`: 2008-10-14 (-9.58%); 2008-10-09 (-9.21%); 2008-10-08 (+8.92%); 2017-05-18 (+8.42%); 2008-10-22 (+7.50%); 2015-09-25 (-6.07%); 2008-11-12 (+5.90%); 2008-10-06 (+5.81%); 2008-12-11 (-5.35%); 2008-09-29 (+5.27%)
