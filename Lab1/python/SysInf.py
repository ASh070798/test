import sys
from ctypes import windll, byref, Structure, Array, wintypes

# Опишем структуру SYSTEM_INFO в виде класса, с помощью типов данных Windows, описанных в ctypes.wintypes 

class MEMORYSTATUSEX(Structure):
    _fields_ = [("dwLength", wintypes.DWORD),
                ("dwMemoryLoad", wintypes.DWORD),
                ("ullTotalPhys", wintypes.DWORD),
                ("ullAvailPhys", wintypes.DWORD),
                ("ullTotalPageFile", wintypes.DWORD),
                ("ullAvailPageFile", wintypes.DWORD),
                ("ullTotalVirtual", wintypes.DWORD),
                ("ullAvailVirtual", wintypes.DWORD),
                ("ullAvailExtendedVirtual", wintypes.DWORD)]


# создаём переменную, являющуюся экзкмпляром класса SYSTEM_INFO
si = MEMORYSTATUSEX()

# загружаем динамическую библиотеку kernel32.dll
kernel32 = windll.kernel32
si.dwLength = sys.getsizeof (si)
# вызываем функцию GetSystemInfo, передавая ей переменную si по ссылке 
kernel32.GlobalMemoryStatusEx(byref(si))

# после вызова функции выводим содержимое полей структуры SYSTEM_INFO
print("%s: %s (0x%x)" % ("Total Physical RAM in bytes", si.ullTotalPhys, si.ullTotalPhys))

