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

struct Type{
    string name;
    int num;
    int strengths;
    int weaknesses;
    
};
Type types[5] = {{"fire", 0}, 
                {"water", 1}, 
                {"grass", 2}, 
                {"ground", 3}, 
                {"electric", 4}};

struct Attack{
    string name;
    int power;
    Type type;
};

struct Fakemon{
    string name;
    int max_hp;
    float current_hp;
    Type type;
    int level;
    Attack attacks[3];
};

struct Player{
    string name;
    vector<Fakemon> team;
};

// Example Fakemon
Fakemon charmander{
    "Charmander",
    100,
    100,
    types[0], // fire type
    5,
    {{"Ember", 15, types[0]},
    {"Flame Tail", 20, types[0]},
    {"Fire Spin", 25, types[0]}}
};
Fakemon squirtle{
    "Squirtle",
    100,
    100,
    types[1], // water type
    5,
    {{"Water Gun", 15, types[1]},
    {"Bubble", 20, types[1]},
    {"Aqua Tail", 25, types[1]}}
};
Fakemon bulbasaur{
    "Bulbasaur",
    100,
    100,
    types[2], // grass type
    5,
    {{"Vine Whip", 15, types[2]},
    {"Razor Leaf", 20, types[2]},
    {"Seed Bomb", 25, types[2]}}
};
Fakemon pikachu{
    "Pikachu",
    100,
    100,
    types[4], // electric type
    5,
    {{"Exposed wire", 15, types[4]},
    {"Static electricity", 20, types[4]},
    {"Bzzt", 25, types[4]}}
};
Fakemon geodude{
    "Geodude",
    100,
    100,
    types[3], // ground type
    5,
    {{"Rock Throw", 15, types[3]},
    {"Earthquake", 20, types[3]},
    {"Mud-Slap", 25, types[3]}}
};

Fakemon wild_fakemon[5] = {charmander, squirtle, bulbasaur, pikachu, geodude};

void show_fakemon(const Fakemon &p) {
    cout << p.name << " (Level " << p.level << ") - HP: " << p.current_hp << "/" << p.max_hp << '\n';
}
void show_all_fakemon(const vector<Fakemon> &fakemon_list) {
    for (int i = 0; i < fakemon_list.size(); i++) {
        show_fakemon(fakemon_list[i]);
    }
}
void show_attacks(const Fakemon &p) {
    cout << p.name << "'s attacks:\n";
    for (int i = 0; i < 3; i++) {
        cout << i + 1 << ". " << p.attacks[i].name << " (Power: " << p.attacks[i].power << ", Type: " << p.attacks[i].type.name << ")\n";
    }
}


void calculate_damage(Fakemon &attacker, Fakemon &defender, const Attack &attack) {
    float damage  = attack.power;
    if (attack.type.num == defender.type.weaknesses) {
        damage = damage * 2 / 5;
    }else if (attack.type.num == defender.type.strengths) {
        damage = damage * 8 / 5;
    }
    damage += attacker.level;
    defender.current_hp -= damage;
}

void heal() {
    for (int i = 0; i < player.team.size(); i++) {
            player.team[i].current_hp = player.team[i].max_hp;}
        cout << "Fully healed!" << '\n';
        return;
    }


void battle(){

};

void explore(){

};


enum MenuOption {
    Explore = 1,
    Battle = 2,
    Heal = 3,
    Exit = 4
};
Player player = {"Ash", {}};
int main_menu(){
    cout << "Main Menu:\n"
         << "1. Explore\n"
         << "2. Battle\n"
         << "3. Heal\n"
         << "4. Exit\n";
    int choice = input();
    if (choice == MenuOption::Explore) {
        explore();
    } else if (choice == MenuOption::Battle) {
        battle();
    } else if (choice == MenuOption::Heal) {
        heal();
    } else if (choice == MenuOption::Exit) {
        cout << "Exiting game. Goodbye!\n";
        return 1;
    }
}