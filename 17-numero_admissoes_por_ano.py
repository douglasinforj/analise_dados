import matplotlib.pyplot as plt
import seaborn as sns
from data_set import df_result


#Extraindo ano
df_result['Ano_Admissao'] = df_result['Data_Admissao'].dt.year

admissoes_por_ano = df_result['Ano_Admissao'].value_counts().sort_index()
admissoes_por_ano.plot(kind='bar')
plt.title('Número de Admissões por Ano')
plt.xlabel('Ano de Admissão')
plt.ylabel('Número de Admissões')
plt.show()