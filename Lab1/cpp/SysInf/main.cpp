#include <sysinfoapi.h>
#include <stdio.h>

int main() {
     // Заполняем структуру SYSTEM_INFO информацией о системе.
    MEMORYSTATUSEX ramInfo;
    GlobalMemoryStatusEx(&ramInfo);
    printf("Total Physical RAM in bytes: %u\n", ramInfo.ullTotalPhys);
    return 0;
}

