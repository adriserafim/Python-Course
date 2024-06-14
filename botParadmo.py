import pyautogui
import time

# Função para pressionar a tecla 'v' a cada 10 segundos
def press_v_every_10_seconds():
    while True:
        pyautogui.press('v')
        time.sleep(1)

# Chama a função
press_v_every_10_seconds()