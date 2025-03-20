# Análise Estatística com Python

Este projeto é um treinamento que faço para aprender a trabalhar com análise exploratória de dados (EDA) e aplicar técnicas de estatística descritiva e visualização de dados. As bibliotecas como pandas, seaborn, matplotlib e scipy são essenciais para análise e visualização eficaz de dados em Python. Foram utilizados dados fictícios para a prática de testes estatísticos, visualização de distribuições e análise de diferentes grupos.


# Objetivos
Este projeto visa:
- Criar um conjunto de dados fictício para análise estatística.
- Explorar estatísticas descritivas como média, mediana e desvio padrão.
- Criar histogramas para entender a distribuição dos dados.
- Analisar tendências ao longo do tempo (exemplo: Data de Admissão dos funcionários).
- Comparar diferentes grupos de cargos e calcular a média de vendas por cargo.
- Aplicar testes estatísticos como o teste t de Student para verificar diferenças entre grupos.

## Tecnologias Utilizadas
- Python: Linguagem de programação principal.
- pandas: Biblioteca para manipulação de dados em formato tabular.
- numpy: Biblioteca para operações numéricas.
- matplotlib: Biblioteca para visualização de gráficos.
- seaborn: Biblioteca para visualização de dados baseada no matplotlib.
- scipy.stats: Biblioteca para cálculos estatísticos (usada em testes de hipóteses e correlações).
- Scikit-Learn: Modelagem de regressão linear.

## Geração dos Dados Fictícios

- O dataset é criado utilizando NumPy e Pandas, gerando informações como:
- Idade (entre 18 e 65 anos)
- Salário (média de R$5000,00 com desvio padrão)
- Número de Vendas (entre 100 e 500 por mês)
- Cargo (Analista, Gerente, Coordenador, Diretor)
- Data de Admissão (aleatória entre 2010 e 2023)


## Captura de Tela:

### DataSet

![DataSet](assets/dataset.png)

### Media - Mediana - Moda
![Média - Mediana - Moda](assets/media_mediana_moda.png)

 - Histograma: mostra a distribuição dos salários e inclui as linhas para a média, mediana e moda.
 - Boxplot: ajuda a visualizar possíveis outliers e a distribuição dos dados.

### Desvio_Padrão e Variancia
![Desvio Padrão e Variancia](assets/desvio_padrao_e_variancia.png)

 - Histograma: mostra a distribuição dos salários.
 - Linha Vermelha: representa a média dos salários.
 - Linhas Verdes: indicam um desvio padrão acima e abaixo da média.

### Correlação vendas e salário
![Correlação de Vendas e Salários](assets/correlacao_vendas_salario.png)

- Gráfico de dispersão (scatter plot): Mostra a relação entre número de vendas e salário.
- Linha de tendência (regressão): Adiciona uma linha vermelha para visualizar a tendência.
- Correlação no título: O valor da correlação é exibido diretamente no gráfico.
- Transparência nos pontos: Deixa o gráfico mais limpo e profissional.

### CBox Plot de Salário
![Correlação de Vendas e Salários](assets/boxplot.png)


O boxplot (ou diagrama de caixa) é uma ferramenta estatística visual que resume a distribuição de um conjunto de dados, destacando sua dispersão, mediana, quartis e valores discrepantes (outliers).

1. O que o Boxplot representa?
O boxplot divide os dados em cinco partes principais:

Mínimo (limite inferior, sem outliers) → O menor valor dentro da faixa aceitável.
Primeiro quartil (Q1 – 25%) → 25% dos dados estão abaixo desse valor.
Mediana (Q2 – 50%) → O valor central da distribuição.
Terceiro quartil (Q3 – 75%) → 75% dos dados estão abaixo desse valor.
Máximo (limite superior, sem outliers) → O maior valor dentro da faixa aceitável.

Valores Outliers → São representados por pontos isolados fora dos limites aceitáveis do boxplot. Esses valores são considerados anomalias ou valores extremos da distribuição.

2. Como ler o Boxplot do Salário?
A "caixa" do gráfico representa a faixa entre o primeiro quartil (Q1 - 25%) e o terceiro quartil (Q3 - 75%).
A linha dentro da caixa representa a mediana (Q2 - 50%), ou seja, o valor central da distribuição.
As "linhas" (bigodes) que saem da caixa indicam o intervalo esperado dos dados, sem considerar os valores discrepantes.
Os pontos fora da caixa (outliers) indicam salários muito baixos ou muito altos, que fogem da distribuição normal dos dados.

