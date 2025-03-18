import matplotlib.pyplot as plt
import seaborn as sns
from data_set import df_result

# Use o boxplot para comparar como os salários se distribuem para diferentes cargos na empresa.(Salário por Cargo)

plt.figure(figsize=(10,6))
sns.boxenplot(x='Cargo', y='Salario', data=df_result)
plt.title('Distribuição de Salário por cargo')
plt.xlabel('Cargo')
plt.ylabel('Salário')
plt.show()