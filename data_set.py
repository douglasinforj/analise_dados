import pandas as pd
import numpy as np

#definindo o tamanho da base de dados
n = 10000

#gerando dados fictícios
np.random.seed(42)

#Gerando as variaveis dos dados
idades = np.random.randint(18, 65, n)                  # idade entre 18 e 65
salarios = np.random.normal(5000, 1000, n).round(2)   # salrio com média 5000 e devio padrão
vendas = np.random.randint(100, 500, n)               # numero de vendas realizadas por mes
cargo = np.random.choice(['Analista', 'Gerente', 'Coordenador', 'Diretor'], n)  #Cargos na empresa
data_admissao = pd.to_datetime(np.random.choice(pd.date_range('2010-01-01', '2023-01-01', freq='D'), n))  # Datas aleatórias de admissão

#Criando o DataFrame
df = pd.DataFrame({
    'Idade': idades,
    'Salario': salarios,
    'Vendas': vendas,
    'Cargo':cargo,
    'Data_Admissao': data_admissao
})

# Mostrando as primeiras linhas
df_result = df.head(10000)
print(df_result)
