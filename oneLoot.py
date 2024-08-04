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

def find_address(process_handle, pattern, size):
    base_address = ctypes.c_void_p(0)
    while True:
        memory_basic_info = ctypes.c_ulong()
        result = ctypes.windll.kernel32.VirtualQueryEx(process_handle, base_address, ctypes.byref(memory_basic_info), ctypes.sizeof(memory_basic_info))
        if result == 0:
            break
        memory = ctypes.create_string_buffer(memory_basic_info.value)
        bytesRead = ctypes.c_size_t()
        if ReadProcessMemory(process_handle, base_address, memory, memory_basic_info.value, ctypes.byref(bytesRead)):
            for i in range(memory_basic_info.value - size + 1):
                if memory[i:i+size] == pattern:
                    return base_address.value + i
        base_address.value += memory_basic_info.value
    return None

# Listar todos os processos em execução
print("Processos em execução:")
for proc in psutil.process_iter(['pid', 'name']):
    print(f"Processo: {proc.info['name']} (PID: {proc.info['pid']})")

process_name = "GDMO.exe"  # Altere para o nome do seu processo, incluindo .exe
pattern = b'\x90\x00\x03\x00\x00'  # Padrão de bytes que você está procurando
size = len(pattern)

pid = get_process_id(process_name)
if pid:
    process_handle = OpenProcess(PROCESS_ALL_ACCESS, False, pid)
    if process_handle:
        address = find_address(process_handle, pattern, size)
        if address:
            print(f"Endereço encontrado: 0x{address:08X}")
        else:
            print("Endereço não encontrado")
    else:
        print(f"Não foi possível obter o handle do processo {pid}")
else:
    print(f"Processo '{process_name}' não encontrado")

