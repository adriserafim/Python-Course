import pyautogui
import time
import openpyxl

looping = 0
MAXlooping = 2500 
tipo = 2
pos = 0, 0
tempo_click = 0.1

def wait_loading():
    time.sleep(0.5)

def wait_screen_loading():
    time.sleep(10)

# Essa parte do código é para abrir loots na bolsa ou banco
if tipo == 1:
    # Um tempo antes de começar
    time.sleep(5)
    
    while looping < MAXlooping:
        looping += 1 # Isso é para adicionar 1 ao numero para uma hora acabar com o looping

        # Clique simples com o botão direito do mouse na posição atual do cursor
        #pyautogui.rightClick() # Não funcionou então não mantivemos o projeto

        # Pressiona o botão direito do mouse
        pyautogui.mouseDown(button='right')

        # Aguarda um pouco para simular o tempo que o botão direito está pressionado (pode ser 0 se não quiser um delay aqui)
        time.sleep(tempo_click)

        # Solta o botão direito do mouse
        pyautogui.mouseUp(button='right')

        # Aguarda alguns segundos
        time.sleep(0.2)

        # Pressiona a tecla Enter
        pyautogui.press('enter')

        # Aguarda alguns segundos
        time.sleep(1.2)

    # Exibir mensagem de conclusão
    print("Processo concluído!")

elif tipo == 2:
    # Um tempo antes de começar
    time.sleep(5)

    while looping < MAXlooping:
        looping += 1 # Isso é para adicionar 1 ao numero para uma hora acabar com o looping

        # Pressione espaço para conversar com o NPC
        pyautogui.press('space')

        # Clicar para visualizar a missão
        pos = 932, 153
        pyautogui.moveTo(pos, duration=1)
        #pyautogui.click(932, 153)
        pyautogui.mouseDown() # Pressionando e segurando o botão do mouse
        time.sleep(tempo_click) # Esperando por tempo_click segundos
        pyautogui.mouseUp() # Soltando o botão do mouse

        # Cliecar para aceitar a missão
        pos = 1174, 265
        pyautogui.moveTo(pos, duration=1)
        pyautogui.mouseDown()
        time.sleep(tempo_click)
        pyautogui.mouseUp()

        # Espere carregar o temino da missão
        wait_loading()

        # Cliecar para completar a missão
        pyautogui.mouseDown()
        time.sleep(tempo_click)
        pyautogui.mouseUp()

        # Clique para abrir a mudança de channel
        pos = 1717, 15
        pyautogui.moveTo(pos, duration=1)
        pyautogui.mouseDown()
        time.sleep(tempo_click)
        pyautogui.mouseUp()

        # Clique no channel desejado
        pos = 1675, 102
        pyautogui.moveTo(pos, duration=1)
        pyautogui.mouseDown()
        time.sleep(tempo_click)
        pyautogui.mouseUp()

        # Pressione enter
        time.sleep(0.2)
        pyautogui.press('enter')

        # Esperar a tela carregar
        wait_screen_loading()

        # Pressione espaço para conversar com o NPC
        pyautogui.press('space')

        # Clicar para visualizar a missão
        pos = 932, 153
        pyautogui.moveTo(pos, duration=1)
        pyautogui.mouseDown()
        time.sleep(tempo_click)
        pyautogui.mouseUp()

        # Cliecar para aceitar a missão
        pos = 1174, 265
        pyautogui.moveTo(pos, duration=1)
        pyautogui.mouseDown()
        time.sleep(tempo_click)
        pyautogui.mouseUp()

        # Espere carregar o temino da missão
        wait_loading()

        # Cliecar para completar a missão
        pyautogui.mouseDown()
        time.sleep(tempo_click)
        pyautogui.mouseUp()

        # Clique para abrir a mudança de channel
        pos = 1717, 15
        pyautogui.moveTo(pos, duration=1)
        pyautogui.mouseDown()
        time.sleep(tempo_click)
        pyautogui.mouseUp()

        # Clique no channel desejado
        pos = 1674, 45
        pyautogui.moveTo(pos, duration=1)
        pyautogui.mouseDown()
        time.sleep(tempo_click)
        pyautogui.mouseUp()

        # Pressione enter
        time.sleep(0.2)
        pyautogui.press('enter')

        # Esperar a tela carregar
        wait_screen_loading()
    
    # Exibir mensagem de conclusão
    print("Processo concluído!")
