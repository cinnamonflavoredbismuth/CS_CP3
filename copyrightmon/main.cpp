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

int input(){ 
    int input=0;   
    while(!(cin >> input)){
        cout<<"Please enter a number option: "<<endl;
        cin.clear();
        cin.ignore(10000);
    }
    return input;
    }

enum class Type{
    Fire = 0,
    Water = 1,
    Grass = 2,
    Ground = 3,
    Electric = 4
};

enum class Fire_attacks{
    Gender_reveal_party = 1,
    The_sun = 2,
    Firenado = 3,
};
enum class Water_attacks{
    Light_shower = 1,
    Erosion = 2,
    Evaporation = 3
};
enum class Grass_attacks{
    Allergic_reaction = 1,
    Pokey_grass = 2,
    Leaf = 3
};
enum class Ground_attacks{
    Trip_over_a_rock = 1,
    Falling_debris = 2,
    Dust_in_your_eyes = 3
};
enum class Electric_attacks{
    Exposed_wire = 1,
    Static_electricity = 2,
    Bzzt = 3
};


struct attack_options {
    string attack1;
    string attack2;
    string attack3;
};

struct Type_info{
    string name;
    int num;
    Types strengths;
    Types weaknesses;
    attack_options attacks;
};
struct Types{
    Type_info fire_type;
    Type_info water_type;
    Type_info grass_type;
    Type_info ground_type;
    Type_info electric_type;
    
};

int type_setup(){
    Types types;
    types.fire_type.name = "fire";
    types.fire_type.num = 0;
    types.fire_type.strengths=types.grass_type;
    
return 0;
};

int main(){
    type_setup();
    return 0;
}