import seaborn as sns
import matplotlib.pyplot as plt
from data_set import df_result

plt.figure(figsize=(10, 6))
sns.boxplot(x='Cargo', y='Salario', data=df_result, palette="coolwarm")

plt.title('Comparação de Salários', fontsize=14, fontweight='bold')
plt.xlabel('Cargo', fontsize=12)
plt.ylabel('Salário (R$)', fontsize=12)
plt.grid(axis='y', linestyle='--', alpha=0.6)
plt.show()



"""
O que o Boxplot vai mostrar?
- Diferença de mediana entre Analistas e Gerentes.
- Distribuição dos salários e presença de outliers.
- Se há grande variação salarial dentro de cada cargo.
"""

"""
O teste t de Student é uma ferramenta estatística que permite comparar as médias de dois grupos.
É um teste de hipóteses que pode ser usado para tirar conclusões sobre um grupo inteiro com base em uma amostra pequena. 


A função ttest_ind vem da biblioteca SciPy, especificamente do módulo scipy.stats. Ela é usada para realizar um teste t de Student para duas amostras independentes. 
Esse teste é útil quando queremos comparar as médias de duas amostras e verificar se elas são estatisticamente diferentes uma da outra.

"""