import pyautogui # Serve para presonar alguma tecla do seu teclado para você
import time # Macador de tempo
import threading # Faz com que as funções funcionem ao mesmo tempo

# Função para pressionar a tecla 'A' a cada 1.9 segundos
def press_a_every():
    while True:
        pyautogui.press('a')
        time.sleep(1.34)

# Função para pressionar a tecla 'V' a cada 10 segundos
def press_v_every():
    while True:
        pyautogui.press('v')
        time.sleep(1)

def press_f1_every():
    while True:
        pyautogui.press('q')
        time.sleep(2.5)

def press_f2_every():
    while True:
        pyautogui.press('w')
        time.sleep(2.5)

def press_f3_every():
    while True:
        pyautogui.press('e')
        time.sleep(2.5)

def press_f4_every():
    while True:
        pyautogui.press('r')
        time.sleep(2.5)

# Criação das threads para executar as funções simultaneamente
thread_a = threading.Thread(target=press_a_every)
thread_v = threading.Thread(target=press_v_every)
thread_f1 = threading.Thread(target=press_f1_every)
thread_f2 = threading.Thread(target=press_f2_every)
thread_f3 = threading.Thread(target=press_f3_every)
thread_f4 = threading.Thread(target=press_f4_every)

# Início das threads
thread_a.start()
thread_v.start()

# Espera que as threads terminem (na verdade, isso não acontecerá porque os loops são infinitos)
thread_a.join()
thread_v.join()
