# -*- coding: utf-8 -*-
"""
Created on Fri Jul 29 17:56:28 2022

@author: caiop

Projeto Ciencia de dados - Previsão de vendas
"""

# Passo 1: Entendimento do desafio
# Passo 2: Entendimento da Área/Empresa
# Passo 3: Extração/Obtenção dos dados
# Passo 4: Ajuste de dados (tratamento/limpeza)
# Passo 5: Análise Exploratória
# Passo 6: Modelagem + Algoritmos (Aqui que enra a IA, se necessário)
# Passo 7: Interpretação dos resultados


import pandas as pd
import numpy
import openpyxl
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split

from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor

from sklearn.metrics import r2_score

tabela = pd.read_csv(r"C:\Users\caiop\OneDrive\Documentos\- Estudos\- Cursos\Python - Hashtag intensivo\Imersao-Python\Aula 4 - ML\Material Didático\advertising.csv")
# print(tabela.corr())

sns.heatmap(tabela.corr(), cmap="Wistia", annot=True)
plt.show()

x = tabela[["TV", "Radio", "Jornal"]]
y = tabela["Vendas"]

x_treino, x_teste, y_treino, y_teste = train_test_split(x, y)

Modelo_regressaoLinear = LinearRegression()
Modelo_arvoreDecisao = RandomForestRegressor()

Modelo_regressaoLinear.fit(x_treino, y_treino)
Modelo_arvoreDecisao.fit(x_treino, y_treino)

previsao_regressaoLinear = Modelo_regressaoLinear.predict(x_teste)
previsao_arvoreDecisao = Modelo_arvoreDecisao.predict(x_teste)

print(r2_score(y_teste, previsao_regressaoLinear))
print(r2_score(y_teste, previsao_arvoreDecisao))
# O melhor modelo é o Modelo_arvoreDecisao

# Previsao para novos dados entrantes
novos = pd.read_csv(r"Material Didático/novos.csv")
print(Modelo_arvoreDecisao.predict(novos))