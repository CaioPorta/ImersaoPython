# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import pandas as pd
import plotly.express as px
from plotly.offline import plot

# Passo 1: Importar a DB
tabela = pd.read_csv(".\\Material didático\\telecom_users.csv")
# Passo 2: Visualizar a DB
# Entender as informações que vc tem disponível
# print(tabela)
# Descobrir as cagadas da DB
# print(tabela.info())
# Passo 3: Tratamento dos dados
# linha -> axis=0; coluna -> axis=1
tabela = tabela.drop("Unnamed: 0", axis=1) # Retira coluna que não é interessante para a análise.
tabela["TotalGasto"] = pd.to_numeric(tabela["TotalGasto"], errors="coerce") # Converte os dados dessa coluna em float. Se nao for possível converter, ele deixa NAN no lugar.
tabela = tabela.dropna(how="all", axis=1) # Retira todas as colunas que tiverem completamente preenchidas com NAN.
tabela = tabela.dropna(how="any", axis=0) # Retira todas as linhas que tiverem algum dado com NAN.
# Passo 4: Analise inicial dos dados
# Como estão os cancelamentos?
# print(tabela)
# print(tabela["Churn"].value_counts()) # Apresentação nominal
# print(tabela["Churn"].value_counts(normalize=True)) # Apresentação percentual
print(tabela["Churn"].value_counts(normalize=True).map("{:.1%}".format)) # Apresentação percentual formatada
# Passo 5: Descobrir os motivos do cancelamento
for coluna in tabela.columns:
    if not coluna == "Churn": grafico = px.histogram(tabela, x=coluna, color="Churn")
    plot(grafico)