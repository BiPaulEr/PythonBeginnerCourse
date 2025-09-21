#include <stdio.h>
#include <stdlib.h>

typedef struct {
    char name[20];
    int health;
    int mana;
} Monster;

// Fonction pour booster les monstres
void boost_monsters(Monster* monsters, int length) {
    for (int i = 0; i < length; i++) {
        monsters[i].health += 10; // boost health
        monsters[i].mana += 5;    // boost mana
    }
}
