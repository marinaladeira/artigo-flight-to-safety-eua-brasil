# Dicionário de variáveis – `dados/processados/base_diaria.csv`

Gerado por `codigo/02_processamento.ipynb`. Retornos em % (log-retorno × 100). Indicadores de regime gravados como 0/1.

| Coluna | Descrição | Unidade | Fonte | Transformação |
|---|---|---|---|---|
| `data` | Data (dia útil comum a Brasil e EUA) | aaaa-mm-dd | — | Interseção dos calendários das séries principais |
| `sp500` | S&P 500, fechamento | pontos | Yahoo Finance (^GSPC); S&P DJI | Close |
| `y_treasury10` | Yield do Treasury de 10 anos, vencimento constante | % a.a. | Federal Reserve, H.15 (RIFLGFCY10_N.B) | ND → ausente |
| `vix` | VIX, fechamento | pontos | Cboe (VIX_History.csv) | CLOSE |
| `ibov` | Ibovespa, fechamento | pontos | Yahoo Finance (^BVSP); B3 | Close |
| `imab` | IMA-B, número-índice | índice | ANBIMA (IMAB) | Número Índice |
| `usdbrl_ptax` | Câmbio PTAX venda | R$/US$ | Banco Central, SGS 1 | texto → número |
| `imab5mais` | IMA-B 5+, número-índice | índice | ANBIMA (IMAB5MAIS) | Número Índice |
| `idka10` | IDkA IPCA 10 anos, número-índice (desde 30/12/2005) | índice | ANBIMA (IDKAIPCA10A) | Número Índice |
| `irfm` | IRF-M, número-índice | índice | ANBIMA (IRFM) | Número Índice |
| `ief` | ETF IEF, preço ajustado por dividendos | US$ | Yahoo Finance (IEF) | Adj Close |
| `y_tips10` | Yield real do TIPS de 10 anos, vencimento constante | % a.a. | Federal Reserve, H.15 (RIFLGFCY10_XII_N.B) | ND → ausente |
| `usdbrl_fech` | Câmbio USD/BRL de fechamento (desde dez. 2003) | R$/US$ | Yahoo Finance (BRL=X) | Close; descartado se desvio da PTAX > 5% |
| `imab_duration_anos` | Duration do IMA-B (desde 31/03/2005) | anos | ANBIMA | Duration (d.u.) / 252 |
| `imab5mais_duration_anos` | Duration do IMA-B 5+ (desde 31/03/2005) | anos | ANBIMA | Duration (d.u.) / 252 |
| `irfm_duration_anos` | Duration do IRF-M | anos | ANBIMA | Duration (d.u.) / 252; 0 → ausente |
| `dd_ibov` | Drawdown do Ibovespa sobre o máximo de 252 pregões | fração | derivada | calendário da B3 |
| `dd_sp500` | Drawdown do S&P 500 sobre o máximo de 252 pregões | fração | derivada | calendário da NYSE |
| `r21_ibov` | Log-retorno acumulado do Ibovespa em 21 pregões | % | derivada | calendário da B3 |
| `r_sp500` | Log-retorno diário do S&P 500 | % | derivada | 100·ln(P_t/P_t−1) |
| `r_ibov` | Log-retorno diário do Ibovespa | % | derivada | 100·ln(P_t/P_t−1) |
| `r_ntnb` | Log-retorno diário do IMA-B (NTN-B, série principal) | % | derivada | 100·ln(P_t/P_t−1) |
| `r_ntnb5mais` | Log-retorno diário do IMA-B 5+ | % | derivada | 100·ln(P_t/P_t−1) |
| `r_idka10` | Log-retorno diário do IDkA IPCA 10A | % | derivada | 100·ln(P_t/P_t−1) |
| `r_irfm` | Log-retorno diário do IRF-M | % | derivada | 100·ln(P_t/P_t−1) |
| `r_ief` | Log-retorno diário do IEF | % | derivada | 100·ln(P_t/P_t−1) |
| `r_usdbrl` | Log-retorno diário da PTAX (positivo = real se desvaloriza) | % | derivada | 100·ln(P_t/P_t−1) |
| `r_usdbrl_fech` | Log-retorno diário do BRL=X | % | derivada | 100·ln(P_t/P_t−1) |
| `r_treasury` | Retorno diário do Treasury de 10 anos | % | derivada | título ao par reprecificado + carry; log |
| `r_treasury_aprox` | Retorno aproximado do Treasury (conferência) | % | derivada | y_t−1·τ − D·Δy |
| `r_tips` | Retorno diário do TIPS de 10 anos | % | derivada | título ao par reprecificado + carry; log |
| `r_ibov_usd` | Log-retorno do Ibovespa em dólar | % | derivada | r_ibov − r_usdbrl |
| `r_ntnb_usd` | Log-retorno do IMA-B em dólar | % | derivada | r_ntnb − r_usdbrl |
| `dias_corridos` | Dias corridos desde o dia útil comum anterior | dias | derivada | diferença de datas |
| `crise_global` | VIX acima do limiar | 0/1 | derivada | vix > 30 |
| `crise_global_p90` | VIX acima do percentil 90 da amostra | 0/1 | derivada | vix > 27.76 |
| `crise_local_br` | Ibovespa em drawdown | 0/1 | derivada | dd_ibov ≤ -0.2 |
| `crise_eua` | S&P 500 em drawdown | 0/1 | derivada | dd_sp500 ≤ -0.2 |
| `crise_p1_eua` | Crise de aversão a risco nos EUA (P1) | 0/1 | derivada | crise_global ou crise_eua |
| `so_local` | Só crise local | 0/1 | derivada | crise_local_br e não crise_global |
| `so_global` | Só crise global | 0/1 | derivada | crise_global e não crise_local_br |
| `ambas` | Crise local e global | 0/1 | derivada | crise_local_br e crise_global |
| `normal` | Sem crise local nem global | 0/1 | derivada | nenhuma das duas |
| `so_local_p90` | Só crise local, com VIX p90 | 0/1 | derivada | crise_local_br e não crise_global_p90 |
| `so_local_sem_cauda` | Só crise local, fora da cauda de crise global | 0/1 | derivada | so_local sem crise_global nos 63 pregões anteriores |
| `crise_local_fixa` | Janela após evento local da lista fixa (preliminar) | 0/1 | derivada | 21 pregões a partir de cada evento |
| `choque_local_br` | Choque de curto prazo no Ibovespa | 0/1 | derivada | r21_ibov < -10.16% (p5) |
| `so_local_choque` | Choque local sem crise global | 0/1 | derivada | choque_local_br e não crise_global |
