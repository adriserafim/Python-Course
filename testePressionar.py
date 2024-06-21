import pyautogui
import time
import threading
import keyboard

# Intervalo de tempo para pressionar a tecla '7'
time_interval = 60  # 1 minuto

# Evento para controlar a execução da thread
stop_event = threading.Event()
thread_7 = None  # Variável global para a thread

# Função para pressionar a tecla '7' a cada intervalo definido
def press_7_every():
    while not stop_event.is_set():
        pyautogui.press('7')
        time.sleep(time_interval)

# Função para iniciar a thread
def start_thread():
    global thread_7
    stop_event.clear()  # Reseta o evento de parada
    thread_7 = threading.Thread(target=press_7_every)
    thread_7.start()

# Função para parar a thread
def stop_thread():
    stop_event.set()  # Sinaliza a thread para parar
    if thread_7 is not None:
        thread_7.join()  # Espera que a thread termine

# Função principal
def main():
    print("Pressione '-' para iniciar e '.' para parar.")

    while True:
        if keyboard.is_pressed('-'):
            if thread_7 is None or not thread_7.is_alive():
                print("Iniciando...")
                start_thread()
                print("Pressionando a tecla '7' a cada 1 minuto.")
                while keyboard.is_pressed('-'):  # Espera a tecla ser liberada
                    pass
        if keyboard.is_pressed('.'):
            if thread_7 is not None and thread_7.is_alive():
                print("Parando...")
                stop_thread()
                print("Parado.")
                while keyboard.is_pressed('.'):  # Espera a tecla ser liberada
                    pass
        time.sleep(0.1)  # Pequena pausa para evitar uso excessivo da CPU

if __name__ == "__main__":
    main()
