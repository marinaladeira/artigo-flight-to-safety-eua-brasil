
# 1 INTRODUÇÃO (rascunho v2: problema, pergunta de pesquisa e justificativa)

## 1.1 Contextualização e problema de pesquisa

Em momentos de crise, investidores costumam vender ativos de risco e buscar proteção em ativos considerados seguros. Esse movimento, conhecido na literatura como *flight to quality* ou *flight to safety*, tem os títulos do Tesouro norte-americano (Treasuries) como principal destino. Como consequência, espera-se que a correlação entre os retornos de ações e desses títulos se torne negativa justamente quando a proteção é mais necessária (BAUR; LUCEY, 2009; BAELE et al., 2020).

Essa relação, porém, não é fixa ao longo do tempo. Em 2022, ações e Treasuries registraram quedas simultâneas nos Estados Unidos, em um ambiente de inflação elevada e alta acelerada de juros pelo Federal Reserve. O episódio reforçou a visão de que o sinal da correlação depende da natureza do choque: crises de aversão a risco tendem a gerar correlação negativa, enquanto choques de inflação e juros tendem a produzir correlação positiva (CAMPBELL; SUNDERAM; VICEIRA, 2017).

No caso de economias emergentes, há um elemento adicional. O título público doméstico carrega risco-país, e em crises o investidor pode reduzir a exposição a esse título em vez de procurá-lo como refúgio (DUFOUR; STANCU; VAROTTO, 2017; HOFMANN; SHIM; SHIN, 2020). No Brasil, portanto, não é evidente que a NTN-B cumpra o mesmo papel de proteção que o Treasury exerce nos Estados Unidos.

O problema de pesquisa surge desse contraste. A teoria de *flight to quality* foi construída e testada, em sua maior parte, com dados de mercados desenvolvidos, e sua validade para um país com risco soberano relevante permanece pouco explorada.

## 1.2 Pergunta de pesquisa

**Pergunta principal:**

> A correlação entre os retornos de ações e de títulos públicos torna-se negativa em períodos de crise, como prevê a hipótese de *flight to quality*, e esse padrão observado nos Estados Unidos se repete no Brasil, ou o risco-país faz o título público brasileiro reagir de forma distinta do Treasury?

A pergunta principal se desdobra em quatro questões específicas, cada uma associada a uma proposição derivada da revisão de literatura (seção 3.2.5):

- **Q1 (EUA, crises de aversão a risco):** a correlação entre S&P 500 e Treasury é significativamente mais negativa em crises do que em períodos normais? *(testa P1)*
- **Q2 (intensidade da incerteza):** a correlação entre S&P 500 e Treasury diminui à medida que o VIX aumenta, e essa relação se enfraquece ou se inverte no caso de Ibovespa e NTN-B? *(testa P2)*
- **Q3 (Brasil, risco-país):** em crises, a correlação entre Ibovespa e NTN-B é positiva, indicando que o título doméstico se comporta como ativo de risco, e esse resultado se mantém após o controle pela taxa de câmbio? *(testa P3)*
- **Q4 (Brasil, origem da crise):** a correlação entre Ibovespa e NTN-B é mais positiva em crises de origem local do que em crises de origem global? *(testa P4)*

As proposições correspondentes são:

- **P1:** nos EUA, a correlação entre ações e Treasury é negativa em crises de aversão a risco (BAUR; LUCEY, 2009; BAELE et al., 2020).
- **P2:** a correlação entre ações e títulos é uma função decrescente da incerteza do mercado acionário nos EUA (CONNOLLY; STIVERS; SUN, 2005), padrão que não se espera observar no Brasil.
- **P3:** no Brasil, o título público doméstico se comporta como ativo de risco em crises (DUFOUR; STANCU; VAROTTO, 2017; HOFMANN; SHIM; SHIN, 2020).
- **P4:** o comportamento de ativo de risco da NTN-B é mais intenso quando a crise decorre de fatores domésticos, que elevam diretamente o risco-país (DUFOUR; STANCU; VAROTTO, 2017).

O episódio de 2022, marcado por choque de inflação e aperto monetário, será tratado como análise exploratória e descritiva, sem proposição formal associada.

## 1.3 Justificativa

A relação entre ações e títulos públicos sustenta a diversificação de carteiras, mas a evidência recente mostra que ela é instável e depende do emissor. Dufour, Stancu e Varotto (2017) mostram que, na zona do euro, os títulos de países de maior risco perderam o status de ativo seguro durante a crise da dívida soberana. Entender em que condições o título público protege uma carteira torna-se relevante tanto para a teoria de alocação de ativos quanto para a gestão de risco em países emergentes.

Para o Brasil, a evidência ainda é escassa. Cardoso e Garcia (2023) documentam comovimento positivo entre títulos e ações entre 2015 e 2020, mas com retornos em horizonte anual e sem condicionar a análise a episódios de crise. Bianconi, Yoshino e Machado de Sousa (2013) estudam os BRIC na crise de 2008 com o EMBI, índice da dívida externa em dólar, e não com títulos domésticos. Este estudo contribui ao testar diretamente a hipótese de *flight to quality* com a NTN-B, em frequência diária e distinguindo crises globais e locais.

A escolha dos casos segue a lógica de replicação teórica do estudo de caso (YIN, 2015). Os Estados Unidos são o caso de referência, pois é nesse mercado que a hipótese de *flight to quality* foi formulada e mais testada. O Brasil é o caso contrastante: tem mercado acionário e de títulos públicos indexados à inflação com séries diárias públicas, ciclo monetário próprio e exposição recorrente a episódios de risco-país. Se a teoria estiver correta, os dois casos devem produzir resultados opostos por razões previsíveis, o que reforça a explicação em vez de enfraquecê-la.

Os resultados interessam a gestores de fundos, entidades de previdência e investidores individuais que mantêm carteiras "balanceadas" entre ações e renda fixa doméstica, pois indicam se essa combinação oferece proteção nas crises ou se a proteção precisa vir do câmbio ou de ativos externos. A validação ocorre em três frentes: testes formais de diferença entre correlações (z de Fisher e bootstrap em blocos), análises de robustez com janelas, limiares e índices alternativos, e reprodutibilidade integral, com dados públicos (FRED, ANBIMA e Banco Central) e código aberto.

---
Notas para o grupo (remover antes da entrega):
- **Numeração das proposições mudou:** P2 agora é a antiga hipótese A (VIX contínuo) e P4 é a antiga hipótese B (crise local x global). A antiga P2 (2022) virou análise exploratória. Atualizar os fichamentos com essa correspondência.
- **Cardoso e Garcia (2023):** é trabalho apresentado em evento (arquivo nos anais do 45º EBE, SBE), não artigo de periódico. Conferir se foi publicado depois em revista e completar a referência ABNT (local e páginas não confirmados). Link: https://sbe.org.br/anais/45EBE/macroeconomia/45_EBE_paper_108.pdf
- **Bianconi, Yoshino e Machado de Sousa (2013):** Emerging Markets Review, v. 14, p. 76-109, DOI 10.1016/j.ememar.2012.11.002. O sinal da correlação para o Brasil não foi citado de propósito: o EMBI é tratado ora como taxa, ora como retorno, e isso muda a interpretação.
- **Silva, Bertella e Pereira (2014) e Martínez Arroyo e Marín Rodríguez (2021)** saíram do parágrafo de lacuna porque a descrição anterior ("tratam o Brasil de forma indireta") não foi verificada. Reinserir se as fichas confirmarem.
- **Molenaar et al. (2024):** um resumo de busca indica que a amostra inclui o Brasil entre cinco emergentes, com baixo poder explicativo dos fatores macro. Não confirmado no texto completo. Se confirmar, é mais um trabalho que reforça a lacuna.
- **P2:** confirmar na ficha de Connolly, Stivers e Sun (2005) que o resultado é de correlação menor com VIX mais alto.
- **P4, definição operacional:** crise local = drawdown do Ibovespa ≤ −20% sem VIX acima do limiar. Verificar se há dias suficientes nessa categoria antes de fechar a proposição.
- **Seção 3.2.5:** conferir se a numeração da revisão de literatura está correta.
- **Fato de 2022:** citar fonte para as quedas simultâneas (ex.: dados do próprio estudo ou Molenaar et al., 2024).
- **Yahoo Finance** saiu da lista de fontes. Definir a fonte do S&P 500 e do Ibovespa.
