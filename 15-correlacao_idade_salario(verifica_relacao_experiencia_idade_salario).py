import matplotlib.pyplot as plt
import seaborn as sns
from data_set import df_result

# Calculando a correlação entre Idade e Salário
correlacao_idade_salario = df_result['Idade'].corr(df_result['Salario'])
print(f'Correlação entre Idade e Salário: {correlacao_idade_salario:.2f}')


# Criando um gráfico de dispersão com linha de tendência
plt.figure(figsize=(10, 6))
sns.regplot(x='Idade', y='Salario', data=df_result, scatter_kws={'alpha': 0.5}, line_kws={'color': 'red'})
plt.title('Correlação entre Idade e Salário')
plt.xlabel('Idade')
plt.ylabel('Salário')
plt.grid(True)

# Exibir gráfico
plt.show()


"""
Explicação das melhorias:
✅ Adicionado sns.regplot() → Esse gráfico de dispersão mostra os pontos individuais e inclui uma linha de regressão para visualizar a tendência da relação entre Idade e Salário.
✅ Usado scatter_kws={'alpha': 0.5} → Reduz a opacidade dos pontos para melhorar a visibilidade quando há sobreposição.
✅ Usado line_kws={'color': 'red'} → A linha de tendência (regressão) fica em vermelho para maior destaque.
✅ Melhoria na formatação do print() → Agora a correlação é exibida com duas casas decimais para facilitar a leitura.


"""