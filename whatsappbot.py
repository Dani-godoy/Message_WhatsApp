#Imports libraries for web browsing and keyboard control
import pyautogui
from selenium import webdriver
import time
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys

#What to do before running the code:
    # -Have WhatsApp installed on the PC
    # -Be with WhatsApp logged into your account
    # -Start the code with WhatsApp open (For the next step)
    # -Click on the WhatsApp typing bar (Can be any conversation)

#For global numbers -- Não mexa nessa parte--
def send_msg(contact):
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.get('https://api.whatsapp.com/send?phone=%s' %contact)           
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
   send_msg(contact)
