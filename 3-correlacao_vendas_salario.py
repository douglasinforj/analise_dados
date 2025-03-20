from data_set import df_result
import matplotlib.pyplot as plt 
import seaborn as sns 


#Correlação entre Vendas e Salário:

correlacao = df_result['Vendas'].corr(df_result['Salario'])
print(f'Correlação entre vendas e salário: {correlacao:.2f}')

# Criando o gráfico de dispersão
plt.figure(figsize=(10, 6))
sns.regplot(x=df_result['Vendas'], y=df_result['Salario'], scatter_kws={'alpha':0.5}, line_kws={'color':'red'})

# Personalizando o gráfico
plt.title(f'Correlação entre Vendas e Salário: {correlacao:.2f}', fontsize=14, fontweight='bold')
plt.xlabel('Número de Vendas', fontsize=12)
plt.ylabel('Salário (R$)', fontsize=12)
plt.grid(True, linestyle='--', alpha=0.6)
plt.show()


"""
Correlação em dados é uma medida estatística que indica a relação entre duas ou mais variáveis. 
Ela é utilizada para identificar e quantificar a associação entre as variáveis, e pode ser positiva, negativa ou inexistente. 

"""