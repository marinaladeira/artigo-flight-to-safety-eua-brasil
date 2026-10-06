# Plano de trabalho: etapas para a escrita do artigo

Artigo: "Treasury como porto seguro: Brasil x EUA"
Desenho: estudo de caso comparativo com 2 casos, em lógica de replicação teórica (YIN, 2015)

Este arquivo descreve o que fazer em cada etapa, o que ela entrega e quando ela pode ser considerada concluída. As caixas de seleção (`- [ ]`) servem para o grupo marcar o avanço.

## Visão geral

| Etapa | Entregável principal | Depende de | Pode rodar em paralelo com |
|---|---|---|---|
| 1. Fichamento da literatura | Uma ficha por referência | Nenhuma | 2 |
| 2. Lacunas e referências | Matriz referência x proposição e lista ABNT | 1 | 1 |
| 3. Bases de dados e processamento | Base processada e script reprodutível | Decisões em aberto (ver etapa 3) | 5 |
| 4. Análise de dados | Tabelas, figuras e veredito por proposição | 3 | 5 |
| 5. Revisão da literatura (texto) | Seção 2 do artigo | 1 e 2 | 3 e 4 |
| 6. Desenvolvimento | Metodologia completa e seção de resultados e discussão | 4 e 5 | Nenhuma |
| 7. Conclusão | Seção de conclusão, resumo e revisão final | 6 | Nenhuma |

### Proposições de referência

- **P1:** nos EUA, a correlação ações x Treasury é negativa em crises de aversão a risco.
- **P2:** a correlação ações x títulos diminui à medida que o VIX aumenta nos EUA, padrão que não se espera observar no Brasil.
- **P3:** no Brasil, a NTN-B se comporta como ativo de risco em crises, mesmo controlando pelo câmbio.
- **P4:** o comportamento de ativo de risco da NTN-B é mais intenso em crises locais do que em crises globais.
- **Exploratória:** episódio de 2022 (choque de inflação e juros), sem proposição formal.

---

## Etapa 1: Fichamento da literatura

**Objetivo:** registrar, de forma padronizada, o que cada referência diz e para que ela serve no artigo.

**Entradas:** as 11 referências dos 4 eixos e as incluídas depois: Cardoso e Garcia (2023), Bianconi, Yoshino e Machado de Sousa (2013) e Connolly, Stivers e Sun (2005), que agora sustenta a P2.

**Passo a passo:**

1. Criar a pasta `fichamento/`, com um arquivo por referência no formato `sobrenome-ano.md` (ex.: `baur-2009.md`).
2. Copiar para cada arquivo o modelo de ficha abaixo.
3. Dividir as referências entre os 5 integrantes (cerca de 3 por pessoa). Sugestão: quem é de finanças fica com os eixos 1 e 2, e quem é de outras áreas fica com textos mais descritivos, revisados depois por alguém de finanças.
4. Ler o texto completo, não só o resumo. Os números e o método citados no artigo precisam vir do texto completo.
5. Preencher todos os campos. Se algo não puder ser confirmado, escrever "não confirmado" em vez de deixar em branco.
6. Fazer uma revisão cruzada: cada ficha é conferida por outro integrante.

**Modelo de ficha:**

```markdown
# SOBRENOME (ano)

- **Referência ABNT:**
- **DOI ou link:**
- **Tipo:** artigo de periódico / working paper / anais / livro
- **Eixo:** 1 / 2 / 3 / 4
- **Objetivo do estudo:**
- **Dados e período:** (países, ativos, frequência, datas)
- **Método:** (correlação móvel, DCC-GARCH, regressão etc.; janela usada)
- **Principais resultados:** (com números e página)
- **Relação com o artigo:** qual proposição sustenta (P1 a P4, exploratória ou contexto)
- **Parâmetro que fornece:** (ex.: janela, limiar de crise, definição de variável)
- **Citação direta útil:** (até 2 linhas, com página)
- **Revisado por:**
```

**Confirmações pendentes nesta etapa:**

- [ ] Molenaar et al. (2024): método de correlação e se a amostra inclui o Brasil
- [ ] Connolly, Stivers e Sun (2005): confirmar que VIX mais alto está associado a correlação menor (base da P2)
- [ ] Forbes e Rigobon (2002): referência completa e argumento do viés de volatilidade
- [ ] Yin (2015): edição e editora usadas
- [ ] Cardoso e Garcia (2023): verificar se foi publicado em periódico depois do evento
- [ ] Silva, Bertella e Pereira (2014) e Martínez Arroyo e Marín Rodríguez (2021): verificar como tratam o Brasil

**Etapa concluída quando:**

- [ ] Todas as referências têm ficha com todos os campos preenchidos
- [ ] Toda ficha passou por revisão cruzada
- [ ] Cada ficha indica a proposição ou o papel que cumpre no artigo

---

## Etapa 2: Identificação de lacunas e referências

**Objetivo:** confirmar que cada proposição tem base na literatura e que a lacuna descrita na introdução é verdadeira.

**Passo a passo:**

1. Montar a matriz referência x proposição no arquivo `fichamento/matriz.md`:

   | Referência | P1 | P2 | P3 | P4 | 2022 | Contexto/lacuna |
   |---|---|---|---|---|---|---|
   | Baur e Lucey (2009) | x | | | | | |

2. Identificar proposições com pouca base. Sugestão (opinião): cada proposição deve ter pelo menos 2 referências revisadas por pares.
3. Fazer uma busca dirigida para reforçar o eixo 4 (Brasil e América Latina):
   - Bases: SciELO, Revista Brasileira de Finanças, RBE, EconomiA (ANPEC), Estudos Econômicos e anais da SBE, ANPEC e SBFin
   - Termos em português: "correlação ações títulos públicos", "NTN-B Ibovespa", "comovimento renda fixa ações", "fuga para qualidade"
   - Termos em inglês: "stock-bond correlation Brazil", "flight to quality emerging markets", "sovereign risk stock bond comovement"
4. Registrar cada busca (base, termos, data e número de resultados relevantes) em `fichamento/log-buscas.md`. Isso documenta o método da revisão narrativa.
5. Fichar todo achado relevante usando a etapa 1.
6. Revisar o parágrafo de lacuna da introdução (seção 1.3) com base no que for encontrado.
7. Montar a lista única de referências em ABNT no arquivo `referencias.md`, em ordem alfabética.

**Etapa concluída quando:**

- [ ] A matriz está completa e nenhuma proposição está sem base
- [ ] O log de buscas está registrado
- [ ] O parágrafo de lacuna foi revisado e todas as afirmações têm fonte
- [ ] `referencias.md` contém todas as obras citadas, com DOI quando houver
- [ ] As notas para o grupo no fim do `artigo.md` sobre referências foram resolvidas

---

## Etapa 3: Busca das bases de dados e processamento inicial

**Objetivo:** montar uma base diária, limpa e reprodutível, com todas as séries necessárias.

### 3.1 Decisões a fechar antes de coletar (decisão do grupo)

- [ ] Fonte da NTN-B: IMA-B, IDkA IPCA (vértice fixo, usado por Cardoso e Garcia, 2023) ou preços do Tesouro IPCA+
- [ ] Título dos EUA: Treasury nominal de 10 anos (principal) e TIPS (robustez), ou o contrário
- [ ] Fonte do S&P 500 e do Ibovespa (o Yahoo Finance saiu da introdução)
- [ ] Início da amostra (limitado pelo início da série de NTN-B escolhida)
- [ ] Limiares de crise: VIX > 30 ou percentil 90; drawdown de −20% sobre o pico de 252 dias
- [ ] Aplicar ou não o mesmo critério de drawdown ao S&P 500 (simetria entre os casos)
- [ ] Tratamento de feriados diferentes entre Brasil e EUA: usar só os dias úteis comuns aos dois países ou repetir o último valor

### 3.2 Séries e fontes

| Variável | Uso | Fonte pública | Observação |
|---|---|---|---|
| S&P 500 | P1, P2 | A definir | No FRED, a série SP500 pode ter histórico limitado (verificar) |
| Treasury 10 anos | P1, P2 | FRED (yield DGS10) ou ETF IEF | Se usar yield, converter: r ≈ −D·Δy |
| VIX | P1, P2, P4 | FRED (VIXCLS) | |
| Ibovespa | P2, P3, P4 | A definir | |
| NTN-B | P2, P3, P4 | ANBIMA (IMA-B ou IDkA) ou Tesouro Nacional | Ver decisão 3.1 |
| USD/BRL (PTAX) | P3 | Banco Central (SGS) | Conferir o código da série |
| IRF-M, TIPS | Robustez | ANBIMA, FRED | |

### 3.3 Passo a passo

1. Criar a estrutura de pastas: `dados/brutos/`, `dados/processados/`, `codigo/` e `figuras/`.
2. Escrever `codigo/01_coleta.py`: baixa cada série e salva o arquivo original em `dados/brutos/`, sem alterações e com a data do download.
3. Escrever `codigo/02_processamento.py`, que deve:
   - alinhar as datas conforme a decisão sobre feriados
   - calcular os log-retornos diários na moeda local
   - converter yield em retorno, se for o caso, documentando a duration usada e a fonte
   - criar as variáveis de crise: `crise_global` (VIX), `crise_local_br` (drawdown do Ibovespa) e a combinação `so_local`, `so_global`, `ambas`
   - salvar a base final em `dados/processados/base_diaria.csv`
4. Gerar estatísticas descritivas: média, desvio, mínimo, máximo e número de observações por série e por regime.
5. Contar os dias em cada regime de crise. **Ponto crítico para a P4:** se houver poucos dias de "só crise local", rever a proposição ou o limiar antes da etapa 4.
6. Criar o dicionário de variáveis em `dados/dicionario.md`: nome, descrição, unidade, fonte e transformação aplicada.
7. Rodar os scripts do zero em outra máquina para confirmar que a base é reproduzida.

**Etapa concluída quando:**

- [ ] Todas as decisões de 3.1 foram registradas, com justificativa
- [ ] Os scripts geram `base_diaria.csv` do zero, sem passos manuais
- [ ] O dicionário de variáveis está completo
- [ ] A tabela descritiva e a contagem de dias por regime estão prontas
- [ ] Outro integrante reproduziu a base com sucesso

---

## Etapa 4: Análise de dados para validação das hipóteses

**Objetivo:** testar cada proposição e registrar se ela é sustentada, sustentada em parte ou não sustentada pelos dados.

**Observação:** em estudo de caso, o resultado é "proposição sustentada ou não", e não "hipótese comprovada". Os testes estatísticos dão suporte à interpretação, mas não a substituem.

### 4.1 Base comum

1. Calcular a correlação móvel de 63 dias úteis para S&P 500 x Treasury e Ibovespa x NTN-B (`codigo/03_correlacoes.py`).
2. Plotar as duas séries de correlação, com as crises sombreadas. Essa é a figura central do artigo.

### 4.2 Teste por proposição

| Proposição | Teste principal | Resultado que sustenta a proposição |
|---|---|---|
| P1 | Correlação média em crise x em período normal (EUA); z de Fisher e bootstrap em blocos | Correlação em crise negativa e significativamente menor que em período normal |
| P2 | Regressão da correlação móvel sobre o VIX, com erros de Newey-West, nos dois países | Coeficiente negativo nos EUA; nulo ou positivo no Brasil |
| P3 | Correlação Ibovespa x NTN-B em crise; correlação parcial ou regressão com o USD/BRL como controle | Correlação positiva em crise, que se mantém com o controle do câmbio |
| P4 | Comparação da correlação em "só crise local" x "só crise global" | Correlação mais positiva em crises locais |
| 2022 | Descrição gráfica e numérica do período, nos dois países | Sem critério formal (análise exploratória) |

**Cuidados metodológicos:**

- Janelas móveis se sobrepõem, então as observações não são independentes. Por isso o bootstrap em blocos é necessário, e o z de Fisher sozinho não basta.
- Correlações sobem mecanicamente quando a volatilidade sobe (FORBES; RIGOBON, 2002, a confirmar). Aplicar o ajuste ou discutir isso como limitação.

### 4.3 Robustez

- [ ] Janelas de 21 e 126 dias
- [ ] Limiares alternativos de crise
- [ ] Datas de crise fixas da literatura
- [ ] IRF-M no lugar da NTN-B
- [ ] TIPS no lugar do Treasury nominal
- [ ] Retornos em USD para o Brasil

### 4.4 Registro

- Salvar todas as tabelas em `resultados/` e todas as figuras em `figuras/`.
- Manter `resultados/log-resultados.md` com o veredito de cada proposição e os números que o sustentam.

**Etapa concluída quando:**

- [ ] Cada proposição tem veredito registrado, com estatística e intervalo de confiança
- [ ] Os testes de robustez foram rodados e o que muda em cada um foi registrado
- [ ] Figuras e tabelas estão numeradas, com título e fonte
- [ ] O código roda do início ao fim e reproduz os resultados

---

## Etapa 5: Desenvolvimento da seção de revisão da literatura

**Roda em paralelo com as etapas 3 e 4.** A revisão não depende dos resultados, mas deve estar pronta antes da etapa 6, porque a discussão compara resultados com a literatura.

**Estrutura sugerida (organizada pelas proposições):**

1. **2.1 Flight to quality e o papel do Treasury:** base da P1 e da P2
2. **2.2 Instabilidade da correlação e natureza do choque:** contexto para 2022 (eixo 2)
3. **2.3 Risco soberano e títulos de emergentes:** base da P3 e da P4
4. **2.4 Evidência para o Brasil e a América Latina:** lacuna
5. **2.5 Síntese:** quadro com as proposições, as referências que sustentam cada uma e o resultado esperado

**Passo a passo:**

1. Redigir cada subseção a partir das fichas, nunca a partir da memória.
2. Terminar cada subseção mostrando de onde sai a proposição correspondente.
3. Montar o quadro-síntese da subseção 2.5.
4. Conferir a numeração: a introdução cita "seção 3.2.5" para as proposições. Ajustar para a numeração real.
5. Revisar o estilo: parágrafos de 3 a 5 linhas, sem travessões, sem conectivos repetidos e com citações em ABNT.

**Etapa concluída quando:**

- [ ] Cada proposição é derivada explicitamente no texto
- [ ] O quadro-síntese está pronto
- [ ] Toda citação consta em `referencias.md`
- [ ] Um integrante de fora da área financeira leu e entendeu o texto

---

## Etapa 6: Desenvolvimento

**Escopo assumido:** metodologia completa (etapa 2 da metodologia, hoje só em tópicos) mais a seção de resultados e discussão. Ajustar se o grupo entender diferente.

### 6.1 Metodologia (etapa 2, texto)

1. Transformar os tópicos atuais em texto, usando as decisões registradas na etapa 3.
2. Descrever dados, fontes, período, transformações, definições de crise e testes, com detalhe suficiente para outra pessoa reproduzir.
3. Indicar onde está o código (repositório) e os dados.

### 6.2 Resultados e discussão

**Estrutura sugerida:**

1. Estatísticas descritivas
2. Caso de referência (EUA): P1 e P2
3. Caso contrastante (Brasil): P2, P3 e P4
4. Análise exploratória de 2022
5. Robustez (resumo; detalhes em apêndice)
6. Discussão comparativa: os dois casos produziram resultados opostos pelas razões previstas? É aqui que a lógica de replicação teórica é avaliada.

**Passo a passo:**

1. Para cada proposição, apresentar o resultado, compará-lo com a literatura (usando a etapa 5) e declarar se a proposição foi sustentada.
2. Relatar resultados contrários ou fracos com a mesma clareza dos favoráveis.
3. Escrever cada figura e tabela de forma que se entenda sozinha (título, legenda e fonte em ABNT).

**Etapa concluída quando:**

- [ ] A metodologia permite reproduzir o estudo sem consultar o código
- [ ] Cada proposição tem resultado, comparação com a literatura e veredito
- [ ] A discussão comparativa responde à pergunta principal

---

## Etapa 7: Conclusão

**Passo a passo:**

1. Responder à pergunta principal em 1 ou 2 parágrafos.
2. Resumir o veredito de cada proposição (P1 a P4) e o achado exploratório de 2022.
3. Explicitar as contribuições, que devem bater com as prometidas na justificativa (seção 1.3).
4. Listar as limitações:
   - Estudo de caso não permite generalização estatística
   - Possível viés de volatilidade nas correlações
   - NTN-B é título real e o Treasury de 10 anos é nominal
   - A série da NTN-B começa por volta de 2002-03, então a crise de 1998 fica fora
   - Poucos episódios de crise local
5. Sugerir pesquisas futuras: outros emergentes como novos casos e outros títulos.
6. Escrever o resumo e o abstract (objetivo, método, resultado e conclusão) e de 3 a 5 palavras-chave.
7. Revisão de consistência:
   - A introdução promete o que a conclusão entrega?
   - As numerações de seções, figuras e tabelas estão corretas?
   - Todas as notas "remover antes da entrega" foram removidas?
8. Ajustar o texto às normas do periódico escolhido e conferir o Qualis na Sucupira.

**Etapa concluída quando:**

- [ ] A conclusão responde à pergunta e a cada proposição
- [ ] Resumo, abstract e palavras-chave estão prontos
- [ ] A revisão de consistência foi feita por pelo menos 2 integrantes
- [ ] O texto está formatado nas normas do periódico-alvo

---

## Cronograma sugerido (estimativa)

Supõe o prazo de 4 a 6 semanas a partir de agora. Ajustar às datas reais do grupo.

| Semana | Etapas |
|---|---|
| 1 | Etapa 1 completa; início da etapa 2; fechamento das decisões da etapa 3.1 |
| 2 | Etapa 2 concluída; etapa 3 (coleta e processamento); início da etapa 5 |
| 3 | Etapa 4 (testes principais); etapa 5 em andamento |
| 4 | Etapa 4 (robustez); etapa 5 concluída; início da etapa 6 |
| 5 | Etapa 6 concluída |
| 6 | Etapa 7, revisão final e submissão |

**Riscos para o prazo:**

- Indefinição da fonte da NTN-B, que trava a etapa 3 inteira
- Poucos dias de crise local, que pode obrigar a reformular a P4
- Achado de estudo brasileiro muito próximo, que exigiria reescrever a lacuna e a contribuição

## Divisão de responsabilidades (a preencher pelo grupo)

| Etapa | Responsável | Revisor |
|---|---|---|
| 1. Fichamento | | |
| 2. Lacunas e referências | | |
| 3. Dados | | |
| 4. Análise | | |
| 5. Revisão da literatura | | |
| 6. Desenvolvimento | | |
| 7. Conclusão | | |
