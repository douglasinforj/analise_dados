import seaborn as sns
import matplotlib.pyplot as plt
from data_set import df_result
import numpy as np

#separando os dados
analistas = df_result[df_result['Cargo'] == 'Analista']['Salario']
gerentes = df_result[df_result['Cargo'] == 'Gerente']['Salario']

medias = [analistas.mean(), gerentes.mean()]
cargos = ['Analistas', 'Gerentes']

plt.figure(figsize=(8, 5))
plt.bar(cargos, medias, color=['blue', 'red'], alpha=0.7)

plt.title('Média Salarial: Analistas vs Gerentes', fontsize=14, fontweight='bold')
plt.xlabel('Cargo', fontsize=12)
plt.ylabel('Média Salarial (R$)', fontsize=12)
plt.grid(axis='y', linestyle='--', alpha=0.6)
plt.show()


