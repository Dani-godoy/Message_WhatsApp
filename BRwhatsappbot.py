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
    pyautogui.write("Add your message here!")
    #If you want to send the message in more lines, uncomment the lines below to enter in WhatsApp and repeat the process if you want
    #pyautogui.hotkey('shift','enter')
    #pyautogui.write("Add the rest of your message here!")
    time.sleep(3)
    pyautogui.keyDown("enter")

# --Put here the list of numbers you want to send a message to--
# Don't forget to put the international code, Regional Code and then the Number
# Exemple: Brazil code +55 ; São Paulo city (11) ; number: 9xxxxyyyy -> 55119xxxxyyyy
contacts = [11941399819, 11964742609]

for i in range(len(contacts)):
   contact=contacts[i]
   mandar_msg(contact)


