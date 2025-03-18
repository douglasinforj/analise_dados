import matplotlib.pyplot as plt
import seaborn as sns
from data_set import df_result



df_result['Ano_Admissao'] = df_result['Data_Admissao'].dt.year

# Contagem de cargos por ano de admissão
cargos_por_ano = df_result.groupby(['Ano_Admissao', 'Cargo']).size().unstack().fillna(0)


# Plotando gráfico de barras empilhadas
cargos_por_ano.plot(kind='bar', stacked=True, figsize=(10, 6))
plt.title('Distribuição de Cargos ao Longo dos Anos')
plt.xlabel('Ano de Admissão')
plt.ylabel('Número de Funcionários')
plt.xticks(rotation=45)
plt.show()