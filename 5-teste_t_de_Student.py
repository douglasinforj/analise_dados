from data_set import df_result

from scipy import stats


# Comparando salários entre Analistas e Gerentes

analistas = df_result[df_result['Cargo'] == 'Analista']['Salario']
gerentes = df_result[df_result['Cargo'] == 'Gerente']['Salario']


t_stat, p_value = stats.ttest_ind(analistas, gerentes)

print(f'T-statistic: {t_stat}, p-value: {p_value}')


"""
O teste t de Student é uma ferramenta estatística que permite comparar as médias de dois grupos.
É um teste de hipóteses que pode ser usado para tirar conclusões sobre um grupo inteiro com base em uma amostra pequena. 


A função ttest_ind vem da biblioteca SciPy, especificamente do módulo scipy.stats. Ela é usada para realizar um teste t de Student para duas amostras independentes. 
Esse teste é útil quando queremos comparar as médias de duas amostras e verificar se elas são estatisticamente diferentes uma da outra.

"""