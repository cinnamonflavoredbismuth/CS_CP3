//CS Pokemon
/*Write a program that creates a Pokémon battle game using structures for Pokémon and enumeration for the menu in C++. The game should allow users to explore (find Pokémon), battle, heal Pokémon, and exit the game. Implement structures for Pokémon that include names, max HP, attacks, and level. Use enumeration for the main menu options.

The game must include the following features:

1. A main menu with options to explore, battle, heal, and exit.
2. Exploration feature to find and catch Pokémon.
3. Battle system where users can fight against wild Pokémon or other trainers.
4. Healing option to restore Pokémon HP.
5. Multiple attack options for each Pokémon during battles.
6. Different Pokémon types with associated weaknesses and strengths.
7. Type-based damage bonuses during battles.*/
#include <iostream>
#include <string>
#include <vector>
using namespace std;

enum class Types{
    Fire = 1,
    Water = 2,
    Grass = 3,
    Ground = 4,
    Electric = 5
};
enum class Fire_Attacks{
    Gender_reveal_party = 1,
    The_sun = 2,
    Firenado = 3,
};
enum class Water_attacks{
    Light_shower = 1,
    Erosion = 2,
    Evaporation = 3
};
struct copyrightmon {
    int type;
    string name;
    int weakness;
    int strength;
    int attacks[];
};