#include <stdio.h>
#include <stdlib.h>

void sum_and_max_and_min(int* array, int length, int* sum, int* max, int* min) {
    *sum = 0;
    *max = array[0]; // initialisation
    *min = array[0];
    for (int i = 0; i < length; i++) {
        *sum += array[i];
        if (array[i] > *max) {
            *max = array[i];
        } 
        else if (array[i] < *min){
            *min = array[i];
        }
    }
}
