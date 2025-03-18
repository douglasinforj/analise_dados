from data_set import df_result



# Desvio Padrão e Variância:

desvio_padrao_salario = df_result['Salario'].std()
variancia_salario = df_result['Salario'].var()

print(f'Desvio Padrão Salário: {desvio_padrao_salario}')
print(f'Variancia Salário: {variancia_salario}')


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