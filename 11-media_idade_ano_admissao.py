import matplotlib.pyplot as plt 
import seaborn as sns
from data_set import df_result


#Calculando a média de idade por ano de admissao

#criando a coluna 'Ano_Admissão' não existe no data_set
df_result['Ano_Admissao'] = df_result['Data_Admissao'].dt.year

media_idade_por_ano = df_result.groupby('Ano_Admissao')['Idade'].mean()

#Plotando o grafico de linhas
plt.figure(figsize=(10, 6))
media_idade_por_ano.plot(kind='line')     #grafico em linha
plt.title('Média de idade por Ano de Admissão')
plt.xlabel('Ano de Admissão')
plt.ylabel('Média de Idade')
plt.show()