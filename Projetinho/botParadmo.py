import pyautogui # Serve para presonar alguma tecla do seu teclado para você
import time # Macador de tempo
import threading # Faz com que as funções funcionem ao mesmo tempo
import keyboard # É utilizado para capturar eventos do teclado, como pressionamento e soltura de teclas

control = 1
time_attack = 1.2
time_skill_1 = 7
time_skill_2 = 9
time_skill_3 = 10
time_skill_4 = 2.25
time_drop = 1
time_wait = 1

# Evento para controlar a execução da thread
stop_event = threading.Event()
thread_a = None  # Variável global para a thread
thread_v = None
thread_f1 = None
thread_f2 = None
thread_f3 = None
thread_f4 = None

# Função para pressionar a tecla 'A' a cada 1.9 segundos
def press_a_every():
    while not stop_event.is_set():
        pyautogui.press('a')
        time.sleep(time_attack)

# Função para pressionar a tecla 'V' a cada 10 segundos
def press_v_every():
    while not stop_event.is_set():
        pyautogui.press('v')
        time.sleep(time_drop)

def press_f1_every():
    while not stop_event.is_set():
        pyautogui.press('q')
        time.sleep(time_wait)
        pyautogui.press('5') # Pressonando a tecla 5 ele ira parar de atacar e podera dar ataque fantasma
        time.sleep(time_skill_1)

def press_f2_every():
    while not stop_event.is_set():
        pyautogui.press('w')
        pyautogui.press('5')
        time.sleep(time_skill_2)

def press_f3_every():
    while not stop_event.is_set():
        pyautogui.press('e')
        pyautogui.press('5')
        time.sleep(time_skill_3)

def press_f4_every():
    while not stop_event.is_set():
        pyautogui.press('r')
        pyautogui.press('5')
        time.sleep(time_skill_4)

# Criação das threads para executar as funções simultaneamente
# Função para iniciar a thread
def start_thread_a():
    global thread_a
    stop_event.clear()  # Reseta o evento de parada
    thread_a = threading.Thread(target=press_a_every)
    thread_a.start()

def start_thread_v():
    global thread_v
    stop_event.clear()  
    thread_v = threading.Thread(target=press_v_every)
    thread_v.start()

def start_thread_f1():
    global thread_f1
    stop_event.clear()  
    thread_f1 = threading.Thread(target=press_f1_every)
    thread_f1.start()

def start_thread_f2():
    global thread_f2
    stop_event.clear()  
    thread_f2 = threading.Thread(target=press_f2_every)
    thread_f2.start()

def start_thread_f3():
    global thread_f3
    stop_event.clear()  
    thread_f3 = threading.Thread(target=press_f3_every)
    thread_f3.start()

def start_thread_f4():
    global thread_f4
    stop_event.clear()  
    thread_f4 = threading.Thread(target=press_f4_every)
    thread_f4.start()

# Função para parar a thread
def stop_thread_a():
    stop_event.set()  # Sinaliza a thread para parar
    if thread_a is not None:
        thread_a.join()  # Espera que a thread termine

def stop_thread_v():
    stop_event.set()  
    if thread_v is not None:
        thread_v.join()  

def stop_thread_f1():
    stop_event.set()  
    if thread_f1 is not None:
        thread_f1.join()  

def stop_thread_f2():
    stop_event.set()  
    if thread_f2 is not None:
        thread_f2.join()  

def stop_thread_f3():
    stop_event.set()
    if thread_f3 is not None:
        thread_f3.join()

def stop_thread_f4():
    stop_event.set()
    if thread_f4 is not None:
        thread_f4.join()

# Função principal
def main():
    print("Pressione '-' para iniciar e ';' para parar.")

    while control <=10:
        #if control == 1:
        # Início das threads
            #thread_a.start()
            #thread_v.start()

        # Espera que as threads terminem (na verdade, isso não acontecerá porque os loops são infinitos)
            #thread_a.join()
            #thread_v.join()

        #elif control == 2:
            #thread_f1.start()
            #thread_a.start()
            #thread_v.start()

            #thread_f1.join()
            #thread_a.join()
            #thread_v.join()
    
        #elif control == 3:
            #thread_a.start()
            #thread_v.start()
            #thread_f1.start()
            #time.sleep(time_wait)
            #thread_f2.start()

            #thread_a.join()
            #thread_v.join()
            #thread_f1.join()
            #thread_f2.join()
    
        #else:
            #print(f"O control está igua a {control}. O valor dessa variaável sera mandado para 11") # O f serve para colocar o valor de uma variável no texto. Para fazer isso a variável tem que estar entre {} 
            #control == 11
        
        if control == 1:
            if keyboard.is_pressed('-'):
                if thread_a is None or not thread_a.is_alive():
                    print("Iniciando...")
                    start_thread_a()
                    start_thread_v()
                    print(f"Pressionando a tecla 'a' a cada {time_attack} segundos e a tecla 'v' a cada {time_drop} segundos.")
                    while keyboard.is_pressed('-'):  # Espera a tecla ser liberada
                        pass
            if keyboard.is_pressed(';'):
                if thread_a is not None and thread_a.is_alive():
                    print("Parando...")
                    stop_thread_a()
                    stop_thread_v()
                    print("Parado.")
                    while keyboard.is_pressed(';'):  # Espera a tecla ser liberada
                        pass
            time.sleep(0.1)  # Pequena pausa para evitar uso excessivo da CPU
        
        #if control ==2:
        #   if keyboard.is_pressed('-'):
        #        if thread_a is None or not thread_a.is_alive():
        #            print("Iniciando...")
        #            start_thread_f1()
        #            start_thread_a()
        #            start_thread_v()
        #            print(f"Pressionando a tecla 'a' a cada {time_attack} segundos e a tecla 'v' a cada {time_drop} segundos.")
        #            while keyboard.is_pressed('-'):  # Espera a tecla ser liberada
        #                pass
        #    if keyboard.is_pressed(';'):
        #        if thread_a is not None and thread_a.is_alive():
        #            print("Parando...")
        #            stop_thread_f1()
        #            stop_thread_a()
        #            stop_thread_v()
        #            print("Parado.")
        #            while keyboard.is_pressed(';'):  # Espera a tecla ser liberada
        #                pass
        #    time.sleep(0.1)  # Pequena pausa para evitar uso excessivo da CPU 

if __name__ == "__main__": # É uma convenção no Python usada para garantir que um bloco de código seja executado somente quando o script é executado diretamente, e não quando ele é importado como um módulo em outro script.
    main()

# Início das threads
#thread_a.start()
#thread_v.start()

# Espera que as threads terminem (na verdade, isso não acontecerá porque os loops são infinitos)
#thread_a.join()
#thread_v.join()