
# 1 INTRODUÇÃO (rascunho v3: problema, pergunta de pesquisa e justificativa)

## 1.1 Contextualização e problema de pesquisa

Em momentos de crise, investidores costumam vender ativos de risco e buscar proteção em ativos considerados seguros. Esse movimento, conhecido na literatura como *flight to quality* ou *flight to safety*, tem no título público de referência, como o Treasury norte-americano, o ativo seguro e líquido típico (BAELE et al., 2020). Como consequência, espera-se que a correlação entre os retornos de ações e desses títulos se torne negativa justamente quando a proteção é mais necessária. Nos dias de *flight to safety* em países desenvolvidos, essa correlação chega a −58,5% em média (BAELE et al., 2020), mas o padrão não aparece em todas as crises: nos Estados Unidos, Baur e Lucey (2009) o encontram em duas de seis crises entre 1997 e 2002.

Essa relação também não é fixa ao longo do tempo. A covariância entre ações e Treasuries foi positiva no início dos anos 1980, de inflação alta, e negativa nos anos 2000, sobretudo nas recessões de 2001 e de 2007 a 2009 (CAMPBELL; SUNDERAM; VICEIRA, 2017). Até 2022, a correlação voltou a subir nos Estados Unidos e na zona do euro, em um ambiente de inflação elevada e de aperto monetário (MOSK; PANGALLO; ZEMA, 2022). Esses episódios reforçam a visão de que o sinal da correlação depende do ambiente: a maior aversão a risco tende a reduzir a correlação, enquanto a inflação alta tende a torná-la positiva (MOLENAAR et al., 2024; MOSK; PANGALLO; ZEMA, 2022).

No caso de economias emergentes, há um elemento adicional. O título público carrega risco soberano e, quando esse risco é alto, deixa de funcionar como proteção. Na zona do euro, os títulos dos países de maior risco passaram a se mover junto com as ações durante a crise da dívida soberana (DUFOUR; STANCU; VAROTTO, 2017). Nos emergentes, a depreciação cambial vem acompanhada de saída de investidores estrangeiros e de alta do prêmio de risco de crédito dos títulos em moeda local (HOFMANN; SHIM; SHIN, 2020). No Brasil, portanto, não é evidente que a NTN-B cumpra o mesmo papel de proteção que o Treasury exerce nos Estados Unidos.

O problema de pesquisa surge desse contraste. A teoria de *flight to quality* foi construída e testada, em sua maior parte, com dados de mercados desenvolvidos, e sua validade para um país com risco soberano relevante permanece pouco explorada.

## 1.2 Pergunta de pesquisa

**Pergunta principal:**

> A correlação entre os retornos de ações e de títulos públicos torna-se negativa em períodos de crise, como prevê a hipótese de *flight to quality*, e esse padrão observado nos Estados Unidos se repete no Brasil, ou o risco-país faz o título público brasileiro reagir de forma distinta do Treasury?

A pergunta principal se desdobra em quatro questões específicas, cada uma associada a uma proposição derivada da revisão de literatura (seção 2.5):

- **Q1 (EUA, crises de aversão a risco):** a correlação entre S&P 500 e Treasury é significativamente mais negativa em crises do que em períodos normais? *(testa P1)*
- **Q2 (intensidade da incerteza):** a correlação entre S&P 500 e Treasury diminui à medida que o VIX aumenta, e essa relação se enfraquece ou se inverte no caso de Ibovespa e NTN-B? *(testa P2)*
- **Q3 (Brasil, risco-país):** em crises, a correlação entre Ibovespa e NTN-B é positiva, indicando que o título doméstico se comporta como ativo de risco, e esse resultado se mantém após o controle pela taxa de câmbio? *(testa P3)*
- **Q4 (Brasil, origem da crise):** a correlação entre Ibovespa e NTN-B é mais positiva em crises de origem local do que em crises de origem global? *(testa P4)*

As proposições correspondentes são:

- **P1:** nos EUA, a correlação entre ações e Treasury é negativa em crises de aversão a risco (BAUR; LUCEY, 2009; BAELE et al., 2020).
- **P2:** nos EUA, a correlação entre ações e títulos diminui à medida que a incerteza do mercado acionário aumenta (CONNOLLY; STIVERS; SUN, 2005; OHMI; OKIMOTO, 2016). Não se espera esse padrão no Brasil, já que, em países com títulos considerados mais arriscados, a correlação tende a ser mais positiva e menos ligada aos fatores que a explicam nos EUA (MOLENAAR et al., 2024; OHMI; OKIMOTO, 2016).
- **P3:** no Brasil, o título público doméstico se comporta como ativo de risco em crises, mesmo controlando pela taxa de câmbio (DUFOUR; STANCU; VAROTTO, 2017; HOFMANN; SHIM; SHIN, 2020; MOLENAAR et al., 2024).
- **P4:** o comportamento de ativo de risco da NTN-B é mais intenso quando a crise decorre de fatores domésticos, que elevam diretamente o risco-país. A proposição é inspirada em Dufour, Stancu e Varotto (2017): na zona do euro, o título dos países de maior risco seguiu protegendo a carteira na crise de 2008, de origem externa, e só passou a se mover com as ações na crise da dívida soberana, que elevou o risco de crédito desses países.

O episódio de 2021 e 2022, marcado por choque de inflação e aperto monetário, será tratado como análise exploratória e descritiva, sem proposição formal associada.

## 1.3 Justificativa

A relação entre ações e títulos públicos sustenta a diversificação de carteiras, mas a evidência mostra que ela é instável e depende do emissor. Dufour, Stancu e Varotto (2017) mostram que, na zona do euro, os títulos de países de maior risco perderam o status de ativo seguro durante a crise da dívida soberana, e Ohmi e Okimoto (2016) encontram, para Itália, Portugal e Espanha, a passagem para correlação positiva logo no início dessa crise. Entender em que condições o título público protege uma carteira torna-se relevante tanto para a teoria de alocação de ativos quanto para a gestão de risco em países emergentes.

Para o Brasil, a evidência ainda é escassa e não trata de crises com títulos domésticos em frequência diária. Cardoso e Garcia (2023) documentam comovimento positivo entre títulos e ações de 2015 ao início de 2020, medido por betas de regressão com retornos em horizonte anual e sem condicionar a análise a episódios de crise. Molenaar et al. (2024) incluem o Brasil entre cinco emergentes, com dados mensais, e mostram que inflação e juro real praticamente não explicam a correlação no país. Bianconi, Yoshino e Machado de Sousa (2013) estudam os BRIC na crise de 2008 com o EMBI, índice da dívida externa em dólar, e não com títulos domésticos. Silva, Bertella e Pereira (2014) relacionam o Ibovespa ao risco-país medido pelo EMBI-BR, sem analisar títulos públicos domésticos. Este estudo contribui ao testar diretamente a hipótese de *flight to quality* com a NTN-B, em frequência diária e distinguindo crises globais e locais.

A escolha dos casos segue a lógica de replicação teórica do estudo de caso (YIN, 2015). Os Estados Unidos são o caso de referência, pois é nesse mercado que a hipótese de *flight to quality* foi formulada e mais testada. O Brasil é o caso contrastante: tem mercado acionário e de títulos públicos indexados à inflação com séries diárias públicas, ciclo monetário próprio e exposição recorrente a episódios de risco-país. Se a teoria estiver correta, os dois casos devem produzir resultados opostos por razões previsíveis, o que reforça a explicação em vez de enfraquecê-la.

Os resultados interessam a gestores de fundos, entidades de previdência e investidores individuais que mantêm carteiras "balanceadas" entre ações e renda fixa doméstica, pois indicam se essa combinação oferece proteção nas crises ou se a proteção precisa vir do câmbio ou de ativos externos. A validação ocorre em três frentes: testes formais de diferença entre correlações (z de Fisher e bootstrap em blocos), análises de robustez com janelas, limiares e índices alternativos, e reprodutibilidade integral, com dados públicos (FRED, ANBIMA e Banco Central) e código aberto. Como a correlação sobe mecanicamente quando a volatilidade aumenta (FORBES; RIGOBON, 2002), o ajuste para esse viés entra como teste de robustez.

---
Notas para o grupo (remover antes da entrega):
- **P4, definição operacional:** crise local = drawdown do Ibovespa ≤ −20% sem VIX acima do limiar. Verificar se há dias suficientes nessa categoria antes de fechar a proposição. A P4 tem base fraca na literatura (só Dufour et al., de forma indireta; ver `fichamento/matriz.md`). Alternativa a discutir: reformular a P4 em termos de risco soberano elevado (CDS de 5 anos do Brasil acima de 2%, limiar de Dufour et al., p. 13). Miyajima, Mohanty e Chan (2015) pode reforçar a P4, mas ainda depende do PDF.
- **2022:** o texto não afirma mais "quedas simultâneas" de ações e Treasuries, porque nenhuma fonte fichada o documenta em texto. O box do BCE diz que a correlação "has increased recently"; confirmar o sinal no Gráfico A do box ou com os dados do próprio estudo na Etapa 4.
- **P2, parte do Brasil:** nenhuma referência testa VIX x correlação em emergentes. A justificativa no texto é indireta (Molenaar et al.; Ohmi e Okimoto para os países de risco do euro). Deixar isso explícito na revisão de literatura.
- **Yin (2015):** conferir a página da replicação teórica num exemplar da Bookman antes de citar com página.
- **Yahoo Finance** saiu da lista de fontes. Definir a fonte do S&P 500 e do Ibovespa.
