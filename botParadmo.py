import pyautogui # Serve para presonar alguma tecla do seu teclado para você
import time # Macador de tempo
import threading # Faz com que as funções funcionem ao mesmo tempo

control = 1
time_attack = 1.34
time_skill_1 = 2.25
time_skill_2 = 2.25
time_skill_3 = 2.25
time_skill_4 = 2.25
time_drop = 1
time_wait = 1

# Função para pressionar a tecla 'A' a cada 1.9 segundos
def press_a_every():
    while True:
        pyautogui.press('a')
        time.sleep(time_attack)

# Função para pressionar a tecla 'V' a cada 10 segundos
def press_v_every():
    while True:
        pyautogui.press('v')
        time.sleep(time_drop)

def press_f1_every():
    while True:
        pyautogui.press('q')
        pyautogui.press('5') # Pressonando a tecla 5 ele ira parar de atacar e podera dar ataque fantasma
        time.sleep(time_skill_1)

def press_f2_every():
    while True:
        pyautogui.press('w')
        pyautogui.press('5')
        time.sleep(time_skill_2)

def press_f3_every():
    while True:
        pyautogui.press('e')
        pyautogui.press('5')
        time.sleep(time_skill_3)

def press_f4_every():
    while True:
        pyautogui.press('r')
        pyautogui.press('5')
        time.sleep(time_skill_4)

# Criação das threads para executar as funções simultaneamente
thread_a = threading.Thread(target=press_a_every)
thread_v = threading.Thread(target=press_v_every)
thread_f1 = threading.Thread(target=press_f1_every)
thread_f2 = threading.Thread(target=press_f2_every)
thread_f3 = threading.Thread(target=press_f3_every)
thread_f4 = threading.Thread(target=press_f4_every)

while control <=10:
    if control == 1:
        # Início das threads
        thread_a.start()
        thread_v.start()

        # Espera que as threads terminem (na verdade, isso não acontecerá porque os loops são infinitos)
        thread_a.join()
        thread_v.join()

    elif control == 2:
        thread_a.start()
        thread_v.start()
        thread_f1.start()

        thread_a.join()
        thread_v.join()
        thread_f1.join()
    
    elif control == 3:
        thread_a.start()
        thread_v.start()
        thread_f1.start()
        time.sleep(time_wait)
        thread_f2.start()

        thread_a.join()
        thread_v.join()
        thread_f1.join()
        thread_f2.join()
    
    else:
        print(f"O control está igua a {control}. O valor dessa variaável sera mandado para 11") # O f serve para colocar o valor de uma variável no texto. Para fazer isso a variável tem que estar entre {} 
        control == 11


# Início das threads
#thread_a.start()
#thread_v.start()

# Espera que as threads terminem (na verdade, isso não acontecerá porque os loops são infinitos)
#thread_a.join()
#thread_v.join()
