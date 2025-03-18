import matplotlib.pyplot as plt 
import seaborn as sns
from data_set import df_result


# Boxplot para salário por cargo

plt.figure(figsize=(10,6))
sns.boxenplot(x='Cargo', y='Salario', data=df_result)
plt.title('Distribuição de Salário por Cargo')
plt.xlabel('Cargo')
plt.ylabel('Salário')
plt.show()