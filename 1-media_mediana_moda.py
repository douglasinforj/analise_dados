from data_set import df_result     #importando dataframe na variavel result


media_salario = df_result['Salario'].mean()  
mediana_salario = df_result['Salario'].median()
moda_salario =  df_result['Salario'].mode()[0]

print(f'Média Salário: {media_salario}')
print(f'Mediana Salário: {mediana_salario}')
print(f'moda Salário: {moda_salario}')




"""
Média, mediana e moda são medidas estatísticas que resumem um conjunto de dados em um único valor. São conhecidas como medidas de tendência central. 
Média 
É calculada somando todos os valores do conjunto e dividindo pelo número de valores
É uma medida sensível aos valores da amostra
É mais adequada quando os dados são distribuídos mais ou menos uniformemente
Mediana
É o valor do meio quando o conjunto de dados está ordenado do menor para o maior 
Se o conjunto tiver um número par de elementos, a mediana é a média aritmética dos dois elementos centrais 
Moda
É o valor que aparece mais vezes em um conjunto de dados 
É útil quando há muitos valores repetidos num conjunto de dados 
Pode não haver moda, haver uma moda, ou haver várias modas num conjunto 
Essas medidas são expressas na mesma unidade dos dados originais. 
"""