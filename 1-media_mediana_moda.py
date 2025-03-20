from data_set import df_result     #importando dataframe na variavel result
import matplotlib.pyplot as plt
import seaborn as sns


# Estatistica Descritiva

media_salario = df_result['Salario'].mean()  
mediana_salario = df_result['Salario'].median()
moda_salario =  df_result['Salario'].mode()[0]

print(f'Média Salário: {media_salario}')
print(f'Mediana Salário: {mediana_salario}')
print(f'moda Salário: {moda_salario}')

# Criando gráficos
plt.subplot(1,2,1)
sns.histplot(df_result['Salario'], bins=30, kde=True, color='blue')
plt.axvline(media_salario, color='red', linestyle='dashed', label='Média')
plt.axvline(mediana_salario, color='green', linestyle='dashed', label='Mediana')
plt.axvline(moda_salario, color='orange', linestyle='dashed', label='Moda')
plt.title('Distribuição de Salário')
plt.xlabel('Salário')
plt.ylabel('Frequencia')
plt.legend()

#Boxplot
plt.subplot(1,2,2)
sns.boxenplot(x=df_result['Salario'], color='blue')
plt.title('Boxplot dos Salários')

plt.tight_layout()
plt.show()

'''
Esse código irá gerar dois gráficos:

Histograma: mostra a distribuição dos salários e inclui as linhas para a média, mediana e moda.
Boxplot: ajuda a visualizar possíveis outliers e a distribuição dos dados.

'''



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