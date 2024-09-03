import pyautogui
import time
import openpyxl

# Função para esperar o carregamento
def wait_loading():
    time.sleep(1)

def wait_screen_loading():
    time.sleep(10)

# Carregar o arquivo Excel
wb = openpyxl.load_workbook(r"C:\Users\Usuario\OneDrive\Documentos\Arquivos Fúteis\E-mail&Senha.xlsx")
sheet = wb.active

# Número de linhas a serem processadas
start_row = 26
end_row = 49

# Caminho da imagem da área vermelha
imagem_base = r"C:\Users\Usuario\Documents\Curso de Python\Projetos Autônomos\ImagemParaCodigo.png"

# Definindo as coordenadas de destino
pos= 0, 0
tempo_click = 0.1
tipos = 2
event = True
contador= 0
N_notif = 0
notif= False

# Esperar para iniciar
time.sleep(5)

# Clicar na área (808, 437)
pyautogui.click(808, 437)

# Esperar para iniciar
wait_loading()

# Loop para cada linha do arquivo Excel
for row in range(start_row, end_row + 1):
    # Ler dados do Excel
    login = sheet[f'C{row}'].value
    password = sheet[f'E{row}'].value

    # Clicar para colocar o login
    pyautogui.doubleClick(808, 437)

    # Digitar o login
    pyautogui.typewrite(login)

    # Apertar TAB
    pyautogui.press('tab')

    # Digitar a senha
    pyautogui.typewrite(password)

    # Apertar ENTER para entrar
    pyautogui.press('enter')

    # Esperar a tela carregar
    wait_screen_loading()

    # Apertar ENTER para entrar no servidor
    pyautogui.press('enter')

    # Esperar a tela carregar
    wait_screen_loading()

    # Apertar ENTER para entrar no personagem
    pyautogui.press('enter')

    # Esperar a tela carregar
    time.sleep(15)

    # Retire as notificações apertando ESC Enter
    if N_notif > 0:
        notif = True  # Isso vai fazer com que a retirada das notificações seja habilitada
        contador = 0
    
    while notif and contador < N_notif:
        contador += 1
        pyautogui.press('enter') # isso ira retirar as notificações adicinais
        time.sleep(1.5)
    
    pyautogui.press('esc')

    # Clicar para coletar o item
    # Movendo o mouse até a posição (1076, 816) suavemente em 3 segundo
    pos = 1076, 816
    pyautogui.moveTo(pos, duration=2)
    wait_loading()
    #pyautogui.click(1076, 816)
    pyautogui.mouseDown() # Pressionando e segurando o botão do mouse
    time.sleep(tempo_click) # Esperando por tempo_click segundos
    pyautogui.mouseUp() # Soltando o botão do mouse

    # Esperar carregar a mensagem
    wait_loading()

    # Apertar ENTER para aceitar o item
    pyautogui.press('enter')
    wait_loading()

    # Eventos especiais de login
    if event:
        # Mostrar as abas de recompensa de login
        pos = 680, 367
        pyautogui.moveTo(pos, duration=1)
        wait_loading()
        pyautogui.mouseDown()
        time.sleep(tempo_click)
        pyautogui.mouseUp()

        # Abrir das moedas de login
        pos = 680, 405
        pyautogui.moveTo(pos, duration=0.3)
        wait_loading()
        pyautogui.mouseDown()
        time.sleep(tempo_click)
        pyautogui.mouseUp()

        # Resgatar o item do evento
        pos = 1076, 816
        pyautogui.moveTo(pos, duration=1)
        wait_loading()
        pyautogui.mouseDown()
        time.sleep(tempo_click)
        pyautogui.mouseUp()

        # Esperar carregar a mensagem
        wait_loading()

    # Apertar ESC para fechar a tela de evento
    pyautogui.press('esc')
    
    if tipos == 2:
        # Apertar a tecla 'u' para coletar itens dados na atualização
        pyautogui.press('u')

        # Clicar para abrir a pastas com os e-mails
        pos = 818, 183
        pyautogui.moveTo(pos, duration=1)
        pyautogui.mouseDown()
        time.sleep(tempo_click)
        pyautogui.mouseUp()

        # Clicar para selecionar todos os e-mails
        pos = 588, 655
        pyautogui.moveTo(pos, duration=1)
        pyautogui.mouseDown()
        time.sleep(tempo_click)
        pyautogui.mouseUp()

        # Clicar para receber os itens anexados aos e-mails
        pos = 741, 658
        pyautogui.moveTo(pos, duration=0.5)
        pyautogui.mouseDown()
        time.sleep(tempo_click)
        pyautogui.mouseUp()

        # Clicar para deletar os e-mails
        pos = 658, 653
        pyautogui.moveTo(pos, duration=3.5) # O tempo dessa locomoção tem que ser grande por conta do carregamento do jogo
        pyautogui.mouseDown()
        time.sleep(tempo_click)
        pyautogui.mouseUp()

        # Apertar ESC para fechar a tela de e-mails
        pyautogui.press('esc')
        wait_loading()

    # Clicar 2 vezes na área de cor vermelha da tela
    # Localizar a área com base na imagem fornecida
    #pos = pyautogui.locateCenterOnScreen(imagem_base, confidence=0.8)
    #pyautogui.moveTo(pos, duration=3)
    #pyautogui.mouseDown()
    #time.sleep(tempo_click)
    #pyautogui.mouseUp()
    #pyautogui.mouseDown()
    #time.sleep(tempo_click)
    #pyautogui.mouseUp()

    if tipos >= 1:
        # Pressione espaço para conversar com o NPC
        pyautogui.press('space')

        # Clicar para visualizar a missão
        pos = 907, 170
        pyautogui.moveTo(pos, duration=1)
        #pyautogui.click(932, 153)
        pyautogui.mouseDown()
        time.sleep(tempo_click)
        pyautogui.mouseUp()

        # Cliecar para aceitar a missão
        pos = 1181, 261
        pyautogui.moveTo(pos, duration=1)
        pyautogui.mouseDown()
        time.sleep(tempo_click)
        pyautogui.mouseUp()

        # Espere carregar o temino da missão
        wait_loading()

        # Pressione espaço para conversar com o NPC
        pyautogui.press('space')

        # Clicar para visualizar a missão
        pos = 907, 170
        pyautogui.moveTo(pos, duration=1)
        #pyautogui.click(932, 153)
        pyautogui.mouseDown()
        time.sleep(tempo_click)
        pyautogui.mouseUp()

        # Cliecar para aceitar a missão
        pos = 1181, 261
        pyautogui.moveTo(pos, duration=1)
        pyautogui.mouseDown()
        time.sleep(tempo_click)
        pyautogui.mouseUp()

        # Espere carregar o temino da missão
        wait_loading()

    # Apertar ESC para aparecer o menu principal
    pyautogui.press('esc')

    # Clicar para deslogar do jogo
    pos = 1081, 540
    pyautogui.moveTo(pos, duration=2)
    pyautogui.mouseDown()
    time.sleep(tempo_click)
    pyautogui.mouseUp()

    # Esperar a tela carregar
    wait_screen_loading()

    # Apertar ESC para sair da conta e espere a tela carregar
    pyautogui.press('esc')
    time.sleep(3)

# Exibir mensagem de conclusão
print("Processo concluído!")
