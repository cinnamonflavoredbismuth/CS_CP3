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


// RANDOM FUNCTION

#include <ctime>
#include <chrono>
#include <thread>

int random_number(int max){
    int sec = time(nullptr);
    this_thread::sleep_for(chrono::seconds(1));
    srand(sec) ;
    int my_num = rand() % (max+1); //generates a number between 0 and the number you put in
    //cout << my_num << endl;
    return my_num;
}




Fakemon choose_fakemon(Player player){
    cout << "Choose your Fakemon:\n1. Flamester (Fire)\n2. Aquatail (Water)\n3. Leafy (Grass)\n4. Rocko (Ground)\n5. Sparky (Electric)" << endl;
    int choice = input();
    Fakemon fakemon_choice = player.team[choice - 1];
    return fakemon_choice;
}
Attack attack_chooser(Fakemon fakemon){
    for (int x; x < 4; x++){
        cout<<x<<". " << fakemon.attacks[x].name<<endl;
    }
    int num = input();
    Attack choice = fakemon.attacks[num - 1]; // edit later for multiple fakemon
    return choice;
}

Attack random_attack(Fakemon fakemon){
    int num = random_number(2);
    Attack choice = fakemon.attacks[num];
    return choice;
}

bool battle(Fakemon attacker, Fakemon defender){
    while (attacker.current_hp > 0 and defender.current_hp > 0){
        
        Attack attack_choice = attack_chooser(attacker);
        calculate_damage(attacker, defender, attack_choice);
        if(defender.current_hp <= 0){
            cout << defender.name << " fainted!" << endl;
            return true;
        }
        calculate_damage(defender, attacker, random_attack(defender));
        if(attacker.current_hp <= 0){
            cout << attacker.name << " fainted!" << endl;
            return false;
        }
    }
}

// try to make a random player/fakemon function. if not have 5 presets


// edit these players

Fakemon random_player(){
    Player players[5] = {
        {"Ash", {charmander, squirtle, bulbasaur}},
        {"Misty", {squirtle, pikachu, geodude}},
        {"Brock", {geodude, bulbasaur, charmander}},
        {"Gary", {pikachu, charmander, squirtle}},
        {"Jessie", {bulbasaur, geodude, pikachu}}
    };
    int index = random_number(4);
    Fakemon encounter=players[index].team[random_number(players[index].team.size() - 1)];
    return encounter;
}

Fakemon random_fakemon(){
    int index = random_number(4);
    Fakemon encounter=wild_fakemon[index];
    return encounter;
}

void battle_player(Player player ){
    cout << "Someone has challenged you to a battle!" << endl;
    Fakemon encounter = random_player();
    Fakemon attacker = choose_fakemon(player);
    bool outcome = battle(attacker, encounter);
    if (outcome == true){
        cout << "You have defeated the trainer!" << endl;
        int number = random_number(5);
        if (number == 1){
            attacker.level += 1;
            cout << player.name << " has leveled up to level " << attacker.level;
        }
        //add fakemon to player's collection
    }else{
        cout << "You failed!" << endl;
    }
}

void explore(Player player){
    Fakemon encounter = random_player();
    Fakemon choice = choose_fakemon(player); // edit later
    cout << "You explore the area and find a wild Fakemon!" << endl;
    cout << "you have encountered a Wild" << encounter.name << endl;
    bool outcome = battle(choice, encounter);
    if (outcome == true){
        cout << "You have defeated the wild Fakemon!" << endl;
        //add fakemon to player's collection
    }else{
        cout << "You failed!" << endl;
    }


}


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
        explore(player);
    } else if (choice == MenuOption::Battle) {
        battle(player.team[0], random_player());
    } else if (choice == MenuOption::Heal) {
        heal();
    } else if (choice == MenuOption::Exit) {
        cout << "Exiting game. Goodbye!\n";
        return 1;
    }
}