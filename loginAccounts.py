import pyautogui
import time
import openpyxl

# Função para esperar 3 segundos
def wait_3_seconds():
    time.sleep(3)

# Carregar o arquivo Excel
wb = openpyxl.load_workbook(r"C:\Users\Usuario\OneDrive\Documentos\Arquivos Fúteis\E-mail&Senha.xlsx")
sheet = wb.active

# Número de linhas a serem processadas
start_row = 3
end_row = 46

# Caminho da imagem da área vermelha
imagem_base = r"C:\Users\Usuario\Documents\Curso de Python\Projetos Autônomos\ImagemParaCodigo.png"

# Definindo as coordenadas de destino
pos= 0, 0
tempo_espera = 0.63
tipos = 0
contador= 0
N_notif = 0
notif= False

# Loop para cada linha do arquivo Excel
for row in range(start_row, end_row + 1):
    # Ler dados do Excel
    email = sheet[f'C{row}'].value
    password = sheet[f'E{row}'].value

    # Passo 1: Clicar na área (808, 437)
    pyautogui.click(808, 437)

    # Passo 2: Esperar 3 segundos
    wait_3_seconds()

    # Passo 3: Clicar 2 vezes na área (808, 437)
    pyautogui.doubleClick(808, 437)

    # Passo 4: Digitar o email
    pyautogui.typewrite(email)

    # Passo 5: Apertar TAB
    pyautogui.press('tab')

    # Passo 6: Digitar a senha
    pyautogui.typewrite(password)

    # Passo 7: Apertar ENTER
    pyautogui.press('enter')

    # Passo 8: Esperar 10 segundos
    time.sleep(10)

    # Passo 9: Apertar ENTER
    pyautogui.press('enter')

    # Passo 10: Esperar 10 segundos
    time.sleep(10)

    # Passo 11: Apertar ENTER
    pyautogui.press('enter')

    # Passo 12: Esperar 20 segundos
    time.sleep(20)

    # Passo 13: Retire as notificações apertando ESC Enter
    if N_notif > 0:
        notif = True  # Isso vai fazer com que a retirada das notificações seja habilitada
        contador = 0
    
    while notif and contador < N_notif:
        contador += 1
        pyautogui.press('enter') # isso ira retirar as notificações adicinais
        time.sleep(1.5)
    
    pyautogui.press('esc')


    # Passo 14: Esperar 3 segundos
    wait_3_seconds()

    # Passo 15: Clicar na área (1076, 816)
    # Movendo o mouse até a posição (1076, 816) suavemente em 3 segundo
    pos = 1076, 816
    pyautogui.moveTo(pos, duration=2)
    wait_3_seconds()
    #pyautogui.click()
    pyautogui.mouseDown() # Pressionando e segurando o botão do mouse
    time.sleep(tempo_espera) # Esperando por tempo_espera segundos
    pyautogui.mouseUp() # Soltando o botão do mouse

    # Passo 16: Esperar 3 segundos
    wait_3_seconds()

    # Passo 17: Apertar ENTER
    pyautogui.press('enter')

    # Passo 18: Esperar 3 segundos
    wait_3_seconds()

    # Passo 19: Apertar ESC
    pyautogui.press('esc')

    # Passo 20: Esperar 3 segundos
    wait_3_seconds()

    if tipos > 1:
        # Passo 21: Apertar a tecla 'u'
        pyautogui.press('u')

        # Passo 22: Esperar 3 segundos
        wait_3_seconds()

        # Passo 23: Clicar na área (818, 183)
        pos = 818, 183
        pyautogui.moveTo(pos, duration=2)
        pyautogui.mouseDown()
        time.sleep(tempo_espera)
        pyautogui.mouseUp()

        # Passo 24: Clicar na área (588, 655)
        pos = 588, 655
        pyautogui.moveTo(pos, duration=1.5)
        pyautogui.mouseDown()
        time.sleep(tempo_espera)
        pyautogui.mouseUp()

        # Passo 25: Clicar na área (741, 658)
        pos = 741, 658
        pyautogui.moveTo(pos, duration=1)
        pyautogui.mouseDown()
        time.sleep(tempo_espera)
        pyautogui.mouseUp()

        # Passo 26: Clicar na área (658, 653)
        pos = 658, 653
        pyautogui.moveTo(pos, duration=0.65)
        pyautogui.mouseDown()
        time.sleep(tempo_espera)
        pyautogui.mouseUp()

        # Passo 27: Esperar 3 segundos
        wait_3_seconds()

        # Passo 28: Apertar ESC
        pyautogui.press('esc')

    # Passo 29: Clicar 2 vezes na área de cor vermelha da tela
    # Localizar a área com base na imagem fornecida
    #pos = pyautogui.locateCenterOnScreen(imagem_base, confidence=0.8)
    #pyautogui.moveTo(pos, duration=3)
    #pyautogui.mouseDown()
    #time.sleep(tempo_espera)
    #pyautogui.mouseUp()
    #pyautogui.mouseDown()
    #time.sleep(tempo_espera)
    #pyautogui.mouseUp()

    # Passo 30: Esperar 3 segundos
    #wait_3_seconds()

    # Passo 31: Clicar na área (831, 174)
    #pyautogui.click(831, 174)

    # Passo 32: Esperar 3 segundos
    #wait_3_seconds()

    # Passo 33: Clicar na área (1185, 264)
    #pyautogui.click(1185, 264)

    # Passo 34: Apertar espaço
    #pyautogui.press('space')

    # Passo 35: Esperar 3 segundos
    #wait_3_seconds()

    # Passo 36: Clicar na área (905, 148)
    #pyautogui.click(905, 148)

    # Passo 37: Esperar 3 segundos
    #wait_3_seconds()

    # Passo 38: Clicar na área (1181, 263)
    #pyautogui.click(1181, 263)

    # Passo 39: Esperar 3 segundos e apertar ESC
    #wait_3_seconds()
    #pyautogui.press('esc')

    # Passo 41: Apertar ESC
    pyautogui.press('esc')

    # Passo 42: Esperar 3 segundos
    wait_3_seconds()

    # Passo 43: Clicar na área (1081, 540)
    pos = 1081, 540
    pyautogui.moveTo(pos, duration=2)
    pyautogui.mouseDown()
    time.sleep(tempo_espera)
    pyautogui.mouseUp()

    # Passo 44: Esperar 10 segundos
    time.sleep(10)

    # Passo 45: Apertar ESC e esperar 3 segundos
    pyautogui.press('esc')
    wait_3_seconds()

# Exibir mensagem de conclusão
print("Processo concluído!")
