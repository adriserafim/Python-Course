import pyautogui
import time
import openpyxl

looping = 0
MAXlooping= 150

# Um tempo antes de começar
time.sleep(5)
while looping < MAXlooping:
    looping += 1 # Isso é para adicionar 1 ao numero para uma hora acabar com o looping

    # Clique simples com o botão direito do mouse na posição atual do cursor
    #pyautogui.rightClick() # Não funcionou então não mantivemos o projeto

    # Pressiona o botão direito do mouse
    pyautogui.mouseDown(button='right')

    # Aguarda um pouco para simular o tempo que o botão direito está pressionado (pode ser 0 se não quiser um delay aqui)
    time.sleep(0.5)

    # Solta o botão direito do mouse
    pyautogui.mouseUp(button='right')

    # Aguarda 3,5 segundos
    time.sleep(0.5)

    # Pressiona a tecla Enter
    pyautogui.press('enter')

    # Aguarda alguns segundos
    time.sleep(1.5)
