file_path = r'D:\MoveInteractive\GDMO\GDMO.exe'

try:
    with open(file_path, 'rb') as file:
        dll_content = file.read()
        # Aqui você pode manipular o conteúdo da DLL conforme necessário
        print(f"Conteúdo da DLL: {dll_content[:100]}")  # Exemplo de impressão dos primeiros 100 bytes
except IOError as e:
    print(f"Erro ao abrir o arquivo: {e}")
except Exception as ex:
    print(f"Erro inesperado: {ex}")
