import pandas as pd
import numpy as np
import dash
from dash import dcc, html, dash_table
from data_set import df_result


# Criando a aplicação Dash
app = dash.Dash(__name__)

app.layout = html.Div([
    html.H1("Tabela Interativa de Dados", style={'textAlign': 'center'}),
    
    dash_table.DataTable(
        id='tabela-dados',
        columns=[{"name": i, "id": i} for i in df_result.columns],
        data=df_result.to_dict('records'),
        filter_action="native",                          # Habilita filtros nos cabeçalhos das colunas
        sort_action="native",                            # Permite ordenar colunas
        page_size=20,                                    # Define o número de linhas por página
        style_table={'overflowX': 'auto'},               # Adapta a tabela ao tamanho da tela
        style_cell={'textAlign': 'center'},              # Alinha os textos ao centro
    )
])

if __name__ == '__main__':
    app.run(debug=True)