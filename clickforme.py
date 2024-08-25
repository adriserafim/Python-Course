import pyautogui
import time
import openpyxl

while True:
    # Clique com o botão direito do mouse na posição atual do cursor
    pyautogui.rightClick()

    # Aguarda 3,5 segundos
    time.sleep(3.5)

    # Pressiona a tecla Enter
    pyautogui.press('enter')
