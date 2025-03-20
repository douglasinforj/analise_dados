import seaborn as sns
import matplotlib.pyplot as plt
from data_set import df_result

# Criando o gráfico
plt.figure(figsize=(10, 6))
sns.boxplot(x=df_result['Salario'], color="skyblue", width=0.6, flierprops={"marker": "o", "markersize": 5})

# Personalizando o gráfico
plt.title('Distribuição dos Salários (Boxplot)', fontsize=14, fontweight='bold')
plt.xlabel('Salário (R$)', fontsize=12)
plt.grid(axis='x', linestyle='--', alpha=0.6)
plt.xticks(fontsize=10)

# Exibindo o gráfico
plt.show()


"""

Explicação Completa do Gráfico Boxplot (Box Plot) de Salário
O boxplot (ou diagrama de caixa) é uma ferramenta estatística visual que resume a distribuição de um conjunto de dados,
destacando sua dispersão, mediana, quartis e valores discrepantes (outliers).


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

"""


"""
O boxplot, também conhecido como diagrama de caixa, é uma ferramenta gráfica que permite visualizar a distribuição de dados quantitativos. 
Ele pode ser usado para comparar a variação de uma variável entre diferentes grupos de dados. 

O boxplot é composto por cinco estatísticas: Mínimo, Primeiro quartil (Q1), Mediana (Q2), Terceiro quartil (Q3), Máximo. 

Esses valores também são chamados de resumo dos cinco números. 

O boxplot pode ser usado para: 
Identificar a existência de possíveis outliers (valores discrepantes) no conjunto de dados
Desenvolver uma perspectiva sobre o caráter dos dados
Comparar a variação de uma variável entre diferentes grupos de dados
Explorar a distribuição de uma variável contínua
O boxplot pode ser feito em programas de computador como Excel e Minitab. 

"""