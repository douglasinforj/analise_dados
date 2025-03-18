import matplotlib.pyplot as plt 
import seaborn as sns
from data_set import df_result

#Histograma de Idade

plt.figure(figsize=(10,6))
sns.histplot(df_result['Idade'], kde=True)
plt.title('Distribuição da Idade')
plt.xlabel('Idade')
plt.ylabel('Frequência')
plt.show()