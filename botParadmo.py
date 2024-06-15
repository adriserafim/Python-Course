import pyautogui # Serve para presonar alguma tecla do seu teclado para você
import time # Macador de tempo
import threading # Faz com que as funções funcionem ao mesmo tempo

# Função para pressionar a tecla 'A' a cada 1.9 segundos
def press_a_every_1_9_seconds():
    while True:
        pyautogui.press('a')
        time.sleep(1.34)

# Função para pressionar a tecla 'V' a cada 10 segundos
def press_v_every_1_second():
    while True:
        pyautogui.press('v')
        time.sleep(1)

# Criação das threads para executar as funções simultaneamente
thread_a = threading.Thread(target=press_a_every_1_9_seconds)
thread_v = threading.Thread(target=press_v_every_1_second)

# Início das threads
thread_a.start()
thread_v.start()

# Espera que as threads terminem (na verdade, isso não acontecerá porque os loops são infinitos)
thread_a.join()
thread_v.join()
