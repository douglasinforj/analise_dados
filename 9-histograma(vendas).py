import matplotlib.pyplot as plt 
import seaborn as sns
from data_set import df_result

#histograma de vendas
plt.figure(figsize=(10,6))
sns.histplot(df_result['Vendas'], kde=True)
plt.title('Distribuição de Vendas')
plt.xlabel('Vendas')
plt.ylabel('Frequência')
plt.show()