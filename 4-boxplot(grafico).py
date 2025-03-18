from data_set import df_result

import seaborn as sns
import matplotlib.pyplot as plt

# Boxplot para Salário:

plt.figure(figsize=(10, 6))
sns.boxenplot(data=df_result['Salario'])
plt.title('Boxplot do Salário')
plt.show()


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