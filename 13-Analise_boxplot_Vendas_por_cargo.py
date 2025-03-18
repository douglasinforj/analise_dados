import matplotlib.pyplot as plt 
import seaborn as sns
from data_set import df_result


# Boxplot para Vendas por Cargo

plt.figure(figsize=(10, 6))
sns.boxenplot(x='Cargo', y='Vendas', data=df_result)
plt.title('Distribuição de Vendas por Cargo')
plt.xlabel('Cargo')
plt.ylabel('Vendas')
plt.show()