import matplotlib.pyplot as plt 
import seaborn as sns
from data_set import df_result

# Criar Histogramas para Entender as Distribuições (Salário)

plt.figure(figsize=(10,6))
sns.histplot(df_result['Salario'], kde=True)
plt.title('Distribuição do Salário')
plt.xlabel('Salário')
plt.ylabel('Frequência')
plt.show()