import matplotlib.pyplot as plt 
import seaborn as sns
from data_set import df_result


"""
Aqui, podemos analisar como a Data de Admissão dos funcionários 
está distribuída ao longo do tempo e também visualizar a tendência ao longo dos anos.

"""


#Extraindo o ano da Data de Admissão
df_result['Ano_Admissao'] = df_result['Data_Admissao'].dt.year

# Contagem de admissões por ano
admissoes_por_ano = df_result['Ano_Admissao'].value_counts().sort_index()

# Grafico de barras
plt.figure(figsize=(10,6))
sns.barplot(x=admissoes_por_ano.index, y=admissoes_por_ano.values, hue=admissoes_por_ano.index, palette="viridis", legend=False)
plt.title('Número de Admissões por Ano')
plt.xlabel('Ano de Admissão')
plt.ylabel('Número de Admissões')
plt.xticks(rotation=45)
plt.show()
