import matplotlib.pyplot as plt 
import seaborn as sns 
import numpy as np
from data_set import df_result
from sklearn.linear_model import LinearRegression



# Criando um gráfico para visualizar a regressão linear entre Idade e Salário usando o matplotlib e o seaborn.

# Regressao linear entre idade e Salário
X = df_result[['Idade']]
y = df_result['Salario']

modelo = LinearRegression()
modelo.fit(X, y)

# Criando valores previstos
df_result['Salario_Previsto'] = modelo.predict(X)

#Plotando dados reais e a linha de regressão
plt.figure(figsize=(10,6))
sns.scatterplot(x=df_result['Idade'], y=df_result['Salario'], label="Dados reais", color='blue')
plt.plot(df_result['Idade'], df_result['Salario_Previsto'], color='red', linewidth=2, label='Regressão Linear')


# Configuração do gráfico
plt.xlabel('Idade')
plt.ylabel('Salário')
plt.title('Regressão Linear: Idade vs. Salário')
plt.legend()
plt.show()

# Exibindo coeficientes
print(f'Coeficiente: {modelo.coef_[0]}, Interceptação: {modelo.intercept_}')


"""

Treina um modelo de regressão linear entre Idade e Salário.
Gera os valores previstos de salário com base na idade.
Plota um gráfico:
Os pontos azuis representam os dados reais.
A linha vermelha representa a linha da regressão linear.

"""





