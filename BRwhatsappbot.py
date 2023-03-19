#Importa as bibliotecas para navegar na Web
import pyautogui
from selenium import webdriver
import time
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys

#O que fazer antes de rodar o codigo:
    # -Ter o WhatssApp instalado no PC
    # -Estar com o WhatsApp logado na sua conta
    # -Começar o código com o WhatsApp aberto (Para o passo a seguir)
    # -Clique na barra de digitar no WhatsApp (Pode ser qualquer conversa)

#Função para mandar a mensagem
def mandar_msg(contato):
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.get('https://api.whatsapp.com/send?phone=55%s' %contato)           
    time.sleep(5)
    pyautogui.hotkey('left')
    time.sleep(5)
    pyautogui.keyDown("enter")
    time.sleep(5)
    pyautogui.write("Adicione sua mensagem aqui!")
    #Caso queira mandar a mensagem em mais linhas, descomente as linhas abaixo para dar o enter no WhatsApp e repita o processo se quiser
    #pyautogui.hotkey('shift','enter')
    #pyautogui.write("Adicione o resto da sua mensagem aqui!")
    time.sleep(3)
    pyautogui.keyDown("enter")

# -- Coloque na lista contatos os números para os quais deseja enviar a mensagem, separados por virgula --
# Código regional e depois o número
# Exemplo: São Paulo (11) ; Número: 9xxxxyyyy -> 119xxxxyyyy
contatos = []

for i in range(len(contatos)):
   contato=contatos[i]
   mandar_msg(contato)



