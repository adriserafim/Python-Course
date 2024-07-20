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
    if ReadProcessMemory(process_handle, address, buffer, size, ctypes.byref(bytesRead)):
        return buffer.raw
    else:
        return None

def list_processes():
    for proc in psutil.process_iter(['pid', 'name']):
        print(f"Processo: {proc.info['name']} (PID: {proc.info['pid']})")

def list_memory_maps(pid):
    process = psutil.Process(pid)
    for mmap in process.memory_maps():
        print(mmap)

# Listar todos os processos em execução
print("Processos em execução:")
list_processes()

process_name = "GDMO.exe"  # Altere para o nome do seu processo, incluindo .exe

pid = get_process_id(process_name)
if pid:
    list_memory_maps(pid)
else:
    print(f"Processo '{process_name}' não encontrado")
