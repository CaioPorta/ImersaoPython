# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

from selenium import webdriver # Pesquisar no google por chrome driver. Baixar a versão compatível com o Google Chrome instalado.
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

import pandas as pd

# BCrypto e Sha256 são bibliotecas de criptografias para senhas

# Passo 1: Pegar a cotação do dólar
# abrir o navegador
navegador = webdriver.Chrome()
# entrar no google
navegador.get("https://www.google.com.br/")
# pesquisar no google a cotação do dólar
navegador.find_element("xpath", '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input').send_keys("Cotação dólar") # Escreve no campo de busca
# navegador.find_element("xpath", '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input').send_keys(Keys.ENTER)
navegador.find_element("xpath", '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[3]/center/input[1]').click()
# pegar a cotação
CotacaoDolar = float(navegador.find_element("xpath", '//*[@id="knowledge-currency__updatable-data-column"]/div[1]/div[2]/span[1]').get_attribute('data-value'))
print(CotacaoDolar)

# Passo 2: Pegar a cotação do euro
# entrar no google
navegador.get("https://www.google.com.br/")
# pesquisar no google a cotação do dólar
navegador.find_element("xpath", '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input').send_keys("Cotação euro") # Escreve no campo de busca
navegador.find_element("xpath", '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input').send_keys(Keys.ENTER)
# pegar a cotação
CotacaoEuro = float(navegador.find_element("xpath", '//*[@id="knowledge-currency__updatable-data-column"]/div[1]/div[2]/span[1]').get_attribute('data-value'))
print(CotacaoEuro)

# Passo 3: Pegar a cotação do ouro
navegador.get("https://www.melhorcambio.com/ouro-hoje")
CotacaoOuro = float(navegador.find_element("xpath", '//*[@id="comercial"]').get_attribute('value').replace(",","."))
print(CotacaoOuro)
navegador.quit()

# Passo 4: Puxar a DB
tabela = pd.read_excel(r".\Material Didático\Produtos.xlsx")

# Passo 5: Recalcular os preços
tabela.loc[tabela["Moeda"]=="Dólar", "Cotação"] = CotacaoDolar
tabela.loc[tabela["Moeda"]=="Euro", "Cotação"] = CotacaoEuro
tabela.loc[tabela["Moeda"]=="Ouro", "Cotação"] = CotacaoOuro

tabela["Preço de Compra"] = tabela["Preço Original"] * tabela["Cotação"]
tabela["Preço de Venda"] = tabela["Preço de Compra"] * tabela["Margem"]

# Passo 6: Exportar a DB
tabela.to_excel("ProdutosAtualizados.xlsx", index=0)