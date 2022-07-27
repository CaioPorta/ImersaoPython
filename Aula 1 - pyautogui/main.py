# -*- coding: utf-8 -*-
"""
Created on Mon Jul 25 20:21:35 2022

@author: caiop

Alguns comandos básicos:
pyautogui.hotkey("ctrl", "t")
pyautogui.click
pyautogui.copy
pyautogui.press("win")
pyautogui.write("chrome")
pyautogui.press("enter")
etc...
time.sleep(5)
pyautogui.position()
"""

import pyautogui
import pyperclip
import time
import win32gui, win32con # Para maximizar a janela do navegador
import pandas as pd

# Declaração de variáveis iniciais
pyautogui.PAUSE = .2 # isso equivale a time.sleep(1) a cada comando

# Passo 1: Entrar no sistema (clicar no link)
pyautogui.press("win")
pyautogui.write("opera")
pyautogui.press("enter")
time.sleep(1)
hwnd = win32gui.GetForegroundWindow()
win32gui.ShowWindow(hwnd, win32con.SW_MAXIMIZE)
pyperclip.copy("https://drive.google.com/drive/folders/149xknr9JvrlEnhNWO49zPcw0PW5icxga?usp=sharing")
pyautogui.hotkey("ctrl", "v")
pyautogui.press("enter")
# Passo 2: Navegar no sistema e encontrar a DB (entrar na pasta exportar)
time.sleep(3)
pyautogui.click(x=394, y=281, clicks=2)
time.sleep(3)
# Passo 3: Download DB
pyautogui.click(x=404, y=286, button="right")
time.sleep(3)
pyautogui.click(x=537, y=731)
time.sleep(4)
for i in range(6):
    pyautogui.press("tab")
pyautogui.press("enter")
pyautogui.write(r"C:\Users\caiop\OneDrive\Documentos\- Estudos\Cursos\Hashtag intensivo python\Download do arquivo da aula")
pyautogui.press("enter")
for i in range(7):
    pyautogui.press("tab")
pyautogui.write("Arquivo da aula")
pyautogui.press("enter")
time.sleep(3)
pyautogui.hotkey("alt", "F4")

# Passo 4: Calcular os indicadores (faturamento, quantidade de produtos)
Tabela = pd.read_excel(r"C:\Users\caiop\OneDrive\Documentos\- Estudos\Cursos\Hashtag intensivo python\Download do arquivo da aula\Arquivo da aula.xlsx")
Quantidade = Tabela["Quantidade"].sum()
Valor_Final = Tabela["Valor Final"].sum()

# Passo 5: Entrar no email
# Instruções são repetição do que foi ensinado anteriormente

# Passo 6: Mandar um email para a diretoria com os indicadores
CorpoDoEmail = f"""Prezados, boa noite
A quantidade somada foi {Quantidade:,.2f}
O valor final somado foi R${Valor_Final:,.2f}

Atenciosamente,
remetente
"""
# pyautogui.hotkey("ctrl", "enter") # Envia email