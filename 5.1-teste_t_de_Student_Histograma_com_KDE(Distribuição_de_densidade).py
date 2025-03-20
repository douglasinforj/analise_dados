import seaborn as sns
import matplotlib.pyplot as plt
from data_set import df_result

# Filtrando os salários por cargo
analistas = df_result[df_result['Cargo'] == 'Analista']['Salario']
gerentes = df_result[df_result['Cargo'] == 'Gerente']['Salario']

plt.figure(figsize=(10, 6))
sns.histplot(analistas, kde=True, color="blue", label="Analistas", bins=20, alpha=0.6)
sns.histplot(gerentes, kde=True, color="red", label="Gerentes", bins=20, alpha=0.6)

plt.title('Distribuição de Salários: Analistas vs Gerentes', fontsize=14, fontweight='bold')
plt.xlabel('Salário (R$)', fontsize=12)
plt.ylabel('Frequência', fontsize=12)
plt.legend()
plt.grid(axis='y', linestyle='--', alpha=0.6)
plt.show()

