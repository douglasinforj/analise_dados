from data_set import df_result


#Correlação entre Vendas e Salário:

correlacao = df_result['Vendas'].corr(df_result['Salario'])
print(f'Correlação entre vendas e salário: {correlacao}')