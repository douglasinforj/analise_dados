from data_set import df_result
import seaborn as sns
import matplotlib.pyplot as plt 

# Estatistica Descritiva

desvio_padrao_salario = df_result['Salario'].std()
variancia_salario = df_result['Salario'].var()

print(f'Desvio Padrão Salário: {desvio_padrao_salario}')
print(f'Variancia Salário: {variancia_salario}')


#Criando o gráfico
plt.figure(figsize=(12, 5))


# Histograma com desvio padrão
sns.histplot(df_result['Salario'], bins=30, kde=True, color='blue')

#Adicionando linhas da média e faizas de desvio padrão
media_salario = df_result['Salario'].mean()
plt.axvline(media_salario, color='red', linestyle='dashed', linewidth=2, label='Média')
plt.axvline(media_salario + desvio_padrao_salario, color='green', linestyle='dashed', linewidth=2, label='+1 Desvio Padrão')
plt.axvline(media_salario - desvio_padrao_salario, color='green', linestyle='dashed', linewidth=2, label='-1 Desvio Padrão')

plt.title('Distribuição de Salários com Desvio Padrão')
plt.xlabel('Salário')
plt.ylabel('Frequência')
plt.legend()
plt.show()





"""
Variância e desvio padrão são medidas de dispersão que indicam a variabilidade de um conjunto de dados. 
São usadas na estatística para calcular o quanto os dados variam em relação à média. 

Variância
É uma medida de dispersão que mostra a distância que cada dado está da média 
Para calcular a variância, calcula-se a diferença de cada valor em relação à média e eleva-se o resultado ao quadrado 
Quanto maior a variância, mais os valores estão distantes da média 


Desvio padrão
É a raiz quadrada da variância 
É uma medida de dispersão que determina um intervalo, centrado na média aritmética, no qual a maior parte dos dados está concentrada 
Quanto maior o desvio-padrão, maior a irregularidade dos dados 
O desvio padrão é expresso na mesma unidade dos dados, o que facilita a comparação 
"""