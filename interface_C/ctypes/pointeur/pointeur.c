#include <stdio.h>
#include <stdlib.h>

__declspec(dllexport) void modification_ptr_int(int* ptr) {
    *ptr = 100;
}