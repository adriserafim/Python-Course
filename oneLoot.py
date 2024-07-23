import ctypes
import psutil

# Funções e constantes da API do Windows
OpenProcess = ctypes.windll.kernel32.OpenProcess
ReadProcessMemory = ctypes.windll.kernel32.ReadProcessMemory
PROCESS_ALL_ACCESS = 0x1F0FFF

def get_process_id(process_name):
    for proc in psutil.process_iter(['pid', 'name']):
        if proc.info['name'].lower() == process_name.lower():
            return proc.info['pid']
    return None

def read_memory(process_handle, address, size):
    buffer = ctypes.create_string_buffer(size)
    bytesRead = ctypes.c_size_t()
    if ReadProcessMemory(process_handle, ctypes.c_void_p(address), buffer, size, ctypes.byref(bytesRead)):
        return buffer.raw
    else:
        return None

def list_processes():
    for proc in psutil.process_iter(['pid', 'name']):
        print(f"Processo: {proc.info['name']} (PID: {proc.info['pid']})")

# Listar todos os processos em execução
print("Processos em execução:")
list_processes()

process_name = "GDMO.exe"  # Altere para o nome do seu processo, incluindo .exe
address = 0x7FF6D0A00000  # Endereço de memória a ser lido (exemplo)
size = 1024  # Tamanho dos dados a serem lidos (exemplo)

pid = get_process_id(process_name)
if pid:
    process_handle = OpenProcess(PROCESS_ALL_ACCESS, False, pid)
    if process_handle:
        data = read_memory(process_handle, address, size)
        if data:
            print("Dados lidos:", data)
        else:
            print("Falha ao ler a memória")
    else:
        print(f"Não foi possível obter o handle do processo {pid}")
else:
    print(f"Processo '{process_name}' não encontrado")

