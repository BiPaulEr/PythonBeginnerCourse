#include <stdio.h>

// Fonction qui additionne deux nombres
__declspec(dllexport) double somme(int a, float b) {
    return a + b;
}

// Fonction qui affiche un message
__declspec(dllexport) void afficher_message() {
    printf("Bonjour depuis la bibliotheque C !\n");
}
