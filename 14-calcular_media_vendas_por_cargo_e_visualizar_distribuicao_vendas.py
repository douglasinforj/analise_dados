import matplotlib.pyplot as plt
import seaborn as sns
from data_set import df_result

# Calculando a média de vendas por cargo
media_vendas_por_cargo = df_result.groupby('Cargo')['Vendas'].mean()

# Criando a figura para os gráficos
fig, axes = plt.subplots(1, 2, figsize=(12, 5))

# Gráfico de barras - Média de vendas por cargo
sns.barplot(x=media_vendas_por_cargo.index, y=media_vendas_por_cargo.values, hue=media_vendas_por_cargo.index, palette="viridis", legend=False, ax=axes[0])
axes[0].set_title('Média de Vendas por Cargo')
axes[0].set_xlabel('Cargo')
axes[0].set_ylabel('Média de Vendas')
axes[0].tick_params(axis='x', rotation=45)

# Boxplot - Distribuição de Vendas por Cargo
sns.boxplot(x='Cargo', y='Vendas', hue='Cargo', data=df_result, palette="muted", legend=False, ax=axes[1])
axes[1].set_title('Distribuição de Vendas por Cargo')
axes[1].set_xlabel('Cargo')
axes[1].set_ylabel('Vendas')
axes[1].tick_params(axis='x', rotation=45)

# Ajustar layout e exibir os gráficos
plt.tight_layout()
plt.show()
