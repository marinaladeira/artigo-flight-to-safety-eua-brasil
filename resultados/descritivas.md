# Estatísticas descritivas e contagem de regimes

Gerado por `codigo/03_descritivas.ipynb` a partir de `dados/processados/base_diaria.csv` (2003-09-16 a 2026-09-30, 5526 dias úteis comuns). Retornos em % ao dia (log-retorno × 100); VIX em pontos.

## Contagem de dias e episódios por regime

| regime             | descrição                                               |   dias |   % da amostra |   episódios |   maior episódio (dias) |
|:-------------------|:--------------------------------------------------------|-------:|---------------:|------------:|------------------------:|
| crise_global       | VIX > 30                                                |    422 |            7.6 |          51 |                     161 |
| crise_global_p90   | VIX > percentil 90                                      |    553 |           10   |          71 |                     186 |
| crise_local_br     | Drawdown do Ibovespa ≤ −20%                             |    729 |           13.2 |          59 |                     222 |
| crise_eua          | Drawdown do S&P 500 ≤ −20%                              |    314 |            5.7 |          20 |                     225 |
| crise_p1_eua       | Crise EUA para a P1 (VIX > 30 ou drawdown do S&P 500)   |    524 |            9.5 |          57 |                     234 |
| normal             | Normal                                                  |   4686 |           84.8 |          81 |                     482 |
| so_global          | Só crise global                                         |    111 |            2   |          39 |                      10 |
| so_local           | Só crise local                                          |    418 |            7.6 |          66 |                      60 |
| ambas              | Crise local e global                                    |    311 |            5.6 |          29 |                     161 |
| so_local_p90       | Só crise local (VIX p90) – robustez                     |    378 |            6.8 |          58 |                      46 |
| so_local_sem_cauda | Só crise local sem cauda de crise global – robustez (a) |    296 |            5.4 |          36 |                      53 |
| crise_local_fixa   | Lista fixa de eventos locais – robustez (b)             |     84 |            1.5 |           4 |                      21 |
| choque_local_br    | Choque de 21 pregões no Ibovespa                        |    277 |            5   |          62 |                      25 |
| so_local_choque    | Choque local sem crise global – robustez (c)            |    182 |            3.3 |          48 |                      19 |

## Descritivas – Amostra toda

| série                |    n |   média |   desvio |   mínimo |   máximo |
|:---------------------|-----:|--------:|---------:|---------:|---------:|
| S&P 500              | 5525 |   0.036 |    1.191 |  -12.765 |   10.424 |
| Treasury 10 anos     | 5525 |   0.011 |    0.49  |   -3.114 |    4.395 |
| Ibovespa             | 5525 |   0.044 |    1.657 |  -15.993 |   15.473 |
| IMA-B (NTN-B)        | 5525 |   0.051 |    0.411 |   -7.818 |    5.26  |
| USD/BRL (PTAX)       | 5525 |   0.011 |    0.93  |   -9.584 |    8.917 |
| VIX (nível)          | 5526 |  18.919 |    8.303 |    9.14  |   82.69  |
| TIPS 10 anos         | 5525 |   0.002 |    0.495 |   -3.895 |    5.644 |
| ETF IEF              | 5525 |   0.013 |    0.432 |   -2.551 |    3.369 |
| IMA-B 5+             | 5525 |   0.053 |    0.619 |  -10.235 |    8.526 |
| IDkA IPCA 10A        | 4974 |   0.048 |    0.656 |   -9.801 |    7.461 |
| IRF-M                | 5525 |   0.047 |    0.201 |   -3.546 |    1.893 |
| USD/BRL (fechamento) | 5039 |   0.016 |    1.113 |  -11.07  |    9.669 |

## Descritivas – Normal

| série                |    n |   média |   desvio |   mínimo |   máximo |
|:---------------------|-----:|--------:|---------:|---------:|---------:|
| S&P 500              | 4685 |   0.078 |    0.86  |   -6.862 |    5.395 |
| Treasury 10 anos     | 4685 |   0.004 |    0.442 |   -1.956 |    2.455 |
| Ibovespa             | 4685 |   0.096 |    1.374 |   -9.211 |    6.389 |
| IMA-B (NTN-B)        | 4685 |   0.056 |    0.36  |   -7.818 |    2.794 |
| USD/BRL (PTAX)       | 4685 |  -0.021 |    0.784 |   -4.61  |    8.423 |
| VIX (nível)          | 4686 |  16.821 |    4.522 |    9.14  |   29.99  |
| TIPS 10 anos         | 4685 |   0.001 |    0.432 |   -2.179 |    2.481 |
| ETF IEF              | 4685 |   0.007 |    0.393 |   -1.866 |    2.219 |
| IMA-B 5+             | 4685 |   0.062 |    0.539 |  -10.235 |    4.114 |
| IDkA IPCA 10A        | 4150 |   0.057 |    0.577 |   -9.801 |    3.746 |
| IRF-M                | 4685 |   0.048 |    0.177 |   -3.546 |    1.432 |
| USD/BRL (fechamento) | 4223 |  -0.021 |    0.971 |   -5.15  |    7.01  |

## Descritivas – Só crise global

| série                |   n |   média |   desvio |   mínimo |   máximo |
|:---------------------|----:|--------:|---------:|---------:|---------:|
| S&P 500              | 111 |  -0.802 |    2.16  |   -6.161 |    9.089 |
| Treasury 10 anos     | 111 |   0.098 |    0.677 |   -1.543 |    2.061 |
| Ibovespa             | 111 |  -0.398 |    1.799 |   -4.767 |    5.393 |
| IMA-B (NTN-B)        | 111 |  -0.008 |    0.394 |   -2.708 |    0.875 |
| USD/BRL (PTAX)       | 111 |   0.313 |    1.236 |   -3.892 |    5.253 |
| VIX (nível)          | 111 |  33.443 |    3.975 |   30.02  |   52.33  |
| TIPS 10 anos         | 111 |  -0.003 |    0.781 |   -2.226 |    2.875 |
| ETF IEF              | 111 |   0.078 |    0.623 |   -1.677 |    2.228 |
| IMA-B 5+             | 111 |  -0.067 |    0.653 |   -4.812 |    1.339 |
| IDkA IPCA 10A        | 111 |  -0.079 |    0.718 |   -5.289 |    1.753 |
| IRF-M                | 111 |   0.022 |    0.213 |   -1.001 |    0.749 |
| USD/BRL (fechamento) | 111 |   0.343 |    1.372 |   -3.3   |    5.354 |

## Descritivas – Só crise local (BR)

| série                |   n |   média |   desvio |   mínimo |   máximo |
|:---------------------|----:|--------:|---------:|---------:|---------:|
| S&P 500              | 418 |   0.003 |    1.167 |   -3.473 |    4.24  |
| Treasury 10 anos     | 418 |   0.055 |    0.524 |   -1.829 |    1.673 |
| Ibovespa             | 418 |  -0.229 |    1.744 |   -5.611 |    5.164 |
| IMA-B (NTN-B)        | 418 |   0.021 |    0.553 |   -2.616 |    4.18  |
| USD/BRL (PTAX)       | 418 |   0.101 |    1.1   |   -6.069 |    3.52  |
| VIX (nível)          | 418 |  20.425 |    4.898 |   11.84  |   29.96  |
| TIPS 10 anos         | 418 |   0.03  |    0.518 |   -1.751 |    2.487 |
| ETF IEF              | 418 |   0.047 |    0.465 |   -1.697 |    1.386 |
| IMA-B 5+             | 418 |   0.001 |    0.808 |   -3.745 |    6.113 |
| IDkA IPCA 10A        | 402 |   0.006 |    0.835 |   -3.878 |    6.224 |
| IRF-M                | 418 |   0.033 |    0.235 |   -0.905 |    1.242 |
| USD/BRL (fechamento) | 398 |   0.134 |    1.255 |   -5.974 |    3.373 |

## Descritivas – Ambas

| série                |   n |   média |   desvio |   mínimo |   máximo |
|:---------------------|----:|--------:|---------:|---------:|---------:|
| S&P 500              | 311 |  -0.249 |    3.204 |  -12.765 |   10.424 |
| Treasury 10 anos     | 311 |   0.032 |    0.886 |   -3.114 |    4.395 |
| Ibovespa             | 311 |  -0.211 |    3.853 |  -15.993 |   15.473 |
| IMA-B (NTN-B)        | 311 |   0.039 |    0.76  |   -4.691 |    5.26  |
| USD/BRL (PTAX)       | 311 |   0.258 |    1.954 |   -9.584 |    8.917 |
| VIX (nível)          | 311 |  43.313 |   11.818 |   30.03  |   82.69  |
| TIPS 10 anos         | 311 |  -0.017 |    0.984 |   -3.895 |    5.644 |
| ETF IEF              | 311 |   0.031 |    0.743 |   -2.551 |    3.369 |
| IMA-B 5+             | 311 |   0.023 |    1.179 |   -7.26  |    8.526 |
| IDkA IPCA 10A        | 311 |   0.037 |    1.163 |   -6.49  |    7.461 |
| IRF-M                | 311 |   0.061 |    0.396 |   -2.513 |    1.893 |
| USD/BRL (fechamento) | 307 |   0.257 |    2.136 |  -11.07  |    9.669 |

## Descritivas – Crise EUA (P1)

| série                |   n |   média |   desvio |   mínimo |   máximo |
|:---------------------|----:|--------:|---------:|---------:|---------:|
| S&P 500              | 524 |  -0.321 |    2.731 |  -12.765 |   10.424 |
| Treasury 10 anos     | 524 |   0.051 |    0.808 |   -3.114 |    4.395 |
| Ibovespa             | 524 |  -0.202 |    3.164 |  -15.993 |   15.473 |
| IMA-B (NTN-B)        | 524 |   0.029 |    0.628 |   -4.691 |    5.26  |
| USD/BRL (PTAX)       | 524 |   0.223 |    1.676 |   -9.584 |    8.917 |
| VIX (nível)          | 524 |  37.907 |   11.617 |   21.48  |   82.69  |
| TIPS 10 anos         | 524 |  -0.004 |    0.883 |   -3.895 |    5.644 |
| ETF IEF              | 524 |   0.044 |    0.696 |   -2.551 |    3.369 |
| IMA-B 5+             | 524 |   0.007 |    0.981 |   -7.26  |    8.526 |
| IDkA IPCA 10A        | 524 |   0.015 |    0.981 |   -6.49  |    7.461 |
| IRF-M                | 524 |   0.049 |    0.329 |   -2.513 |    1.893 |
| USD/BRL (fechamento) | 518 |   0.216 |    1.861 |  -11.07  |    9.669 |
