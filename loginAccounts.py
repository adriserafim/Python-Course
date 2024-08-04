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
start_row = 5
end_row = 47

# Caminho da imagem da área vermelha
imagem_base = r"C:\Users\Usuario\Documents\Curso de Python\Projetos Autônomos\ImagemParaCodigo.png"

# Definindo as coordenadas de destino
pos= 0, 0
tempo_espera = 0.63

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

    # Passo 13: Apertar ESC
    pyautogui.press('esc')

    # Passo 14: Esperar 3 segundos
    wait_3_seconds()

    # Passo 15: Clicar na área (1076, 816)
    # Movendo o mouse até a posição (1076, 816) suavemente em 3 segundo
    pos = 1076, 816
    pyautogui.moveTo(pos, duration=3)
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

    # Passo 21: Apertar a tecla 'u'
    pyautogui.press('u')

    # Passo 22: Esperar 3 segundos
    wait_3_seconds()

    # Passo 23: Clicar na área (818, 183)
    pos = 818, 183
    pyautogui.moveTo(pos, duration=3)
    pyautogui.mouseDown()
    time.sleep(tempo_espera)
    pyautogui.mouseUp()

    # Passo 24: Esperar 3 segundos
    wait_3_seconds()

    # Passo 25: Clicar na área (588, 655)
    pos = 588, 655
    pyautogui.moveTo(pos, duration=3)
    pyautogui.mouseDown()
    time.sleep(tempo_espera)
    pyautogui.mouseUp()

    # Passo 26: Esperar 3 segundos
    wait_3_seconds()

    # Passo 27: Clicar na área (741, 658)
    pos = 741, 658
    pyautogui.moveTo(pos, duration=3)
    pyautogui.mouseDown()
    time.sleep(tempo_espera)
    pyautogui.mouseUp()

    # Passo 28: Esperar 3 segundos
    wait_3_seconds()

    # Passo 29: Clicar na área (658, 653)
    pos = 658, 653
    pyautogui.moveTo(pos, duration=3)
    pyautogui.mouseDown()
    time.sleep(tempo_espera)
    pyautogui.mouseUp()

    # Passo 30: Esperar 3 segundos
    wait_3_seconds()

    # Passo 31: Apertar ESC
    pyautogui.press('esc')

    # Passo 32: Clicar 2 vezes na área de cor vermelha da tela
    # Localizar a área com base na imagem fornecida
    pos = pyautogui.locateCenterOnScreen(imagem_base, confidence=0.8)
    pyautogui.moveTo(pos, duration=3)
    pyautogui.mouseDown()
    time.sleep(tempo_espera)
    pyautogui.mouseUp()
    pyautogui.mouseDown()
    time.sleep(tempo_espera)
    pyautogui.mouseUp()

    # Passo 33: Esperar 3 segundos
    wait_3_seconds()

    # Passo 34: Clicar na área (831, 174)
    pyautogui.click(831, 174)

    # Passo 35: Esperar 3 segundos
    wait_3_seconds()

    # Passo 36: Clicar na área (1185, 264)
    pyautogui.click(1185, 264)

    # Passo 37: Apertar espaço
    pyautogui.press('space')

    # Passo 38: Esperar 3 segundos
    wait_3_seconds()

    # Passo 39: Clicar na área (905, 148)
    pyautogui.click(905, 148)

    # Passo 40: Esperar 3 segundos
    wait_3_seconds()

    # Passo 41: Clicar na área (1181, 263)
    pyautogui.click(1181, 263)

    # Passo 42: Esperar 3 segundos
    wait_3_seconds()

    # Passo 43: Apertar 2 vezes o ESC
    pyautogui.press('esc')
    pyautogui.press('esc')

    # Passo 44: Esperar 3 segundos
    wait_3_seconds()

    # Passo 45: Clicar na área (1081, 540)
    pyautogui.click(1081, 540)

    # Passo 46: Esperar 10 segundos
    time.sleep(10)

    # Passo 47: Apertar ESC
    pyautogui.press('esc')

# Exibir mensagem de conclusão
print("Processo concluído!")
