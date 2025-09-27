// //CS Pokemon
// /*Write a program that creates a Pokémon battle game using structures for Pokémon and enumeration for the menu in C++. The game should allow users to explore (find Pokémon), battle, heal Pokémon, and exit the game. Implement structures for Pokémon that include names, max HP, attacks, and level. Use enumeration for the main menu options.

// The game must include the following features:

// 1. A main menu with options to explore, battle, heal, and exit.
// 2. Exploration feature to find and catch Pokémon.
// 3. Battle system where users can fight against wild Pokémon or other trainers.
// 4. Healing option to restore Pokémon HP.
// 5. Multiple attack options for each Pokémon during battles.
// 6. Different Pokémon types with associated weaknesses and strengths.
// 7. Type-based damage bonuses during battles.*/
// #include <iostream>
// #include <string>
// #include <vector>
// using namespace std;

// int input(){ 
//     int input=0;   
//     while(!(cin >> input)){
//         cout<<"Please enter a number option: "<<endl;
//         cin.clear();
//         cin.ignore(10000);
//     }
//     return input;
//     }



// enum class Fire_attacks{
//     Gender_reveal_party = 1,
//     The_sun = 2,
//     Firenado = 3,
// };
// enum class Water_attacks{
//     Light_shower = 1,
//     Erosion = 2,
//     Evaporation = 3
// };
// enum class Grass_attacks{
//     Allergic_reaction = 1,
//     Pokey_grass = 2,
//     Leaf = 3
// };
// enum class Ground_attacks{
//     Trip_over_a_rock = 1,
//     Falling_debris = 2,
//     Dust_in_your_eyes = 3
// };
// enum class Electric_attacks{
//     Exposed_wire = 1,
//     Static_electricity = 2,
//     Bzzt = 3
// };


// struct Type{
//     string name;
//     int num;
//     int strengths;
//     int weaknesses;

// };

// struct Types{
//     Type fire_type;
//     Type water_type;
//     Type grass_type;
//     Type ground_type;
//     Type electric_type;
    
// };
// Types types;

// int type_setup(){
//     //fire type
//     types.fire_type.name = "fire";
//     types.fire_type.num = 0;
//     types.fire_type.strengths=types.grass_type.num;
//     types.fire_type.weaknesses=types.water_type.num;
//     //water type
//     types.water_type.name = "water";
//     types.water_type.num = 1;
//     types.water_type.strengths=types.fire_type.num;
//     types.water_type.weaknesses=types.electric_type.num;
//     //grass type
//     types.grass_type.name = "grass";
//     types.grass_type.num = 2;   
//     types.grass_type.strengths=types.ground_type.num;
//     types.grass_type.weaknesses=types.fire_type.num;
//     //ground type
//     types.ground_type.name = "ground";
//     types.ground_type.num = 3;
//     types.ground_type.strengths=types.electric_type.num;
//     types.ground_type.weaknesses=types.grass_type.num;
//     //electric type
//     types.electric_type.name = "electric";
//     types.electric_type.num = 4;
//     types.electric_type.strengths=types.water_type.num;
//     types.electric_type.weaknesses=types.ground_type.num;

//     return 0;
    
// };

// struct Attack{
//     string name;
//     int power;
//     Type type;
// };


// struct Copyrightmon{
//     string name;
//     int max_hp;
//     int current_hp;
//     Type type;
//     int level;
//     Attack attacks[3];
// };

// Copyrightmon pikachu{
//     "Pikachu",
//     100,
//     100,
//     types.electric_type,
//     5,
//     {{"Exposed wire", 15, types.electric_type},
//     {"Static electricity", 20, types.electric_type},
//     {"Bzzt", 25, types.electric_type}}
// };

// int calculate_damage(Copyrightmon& attacker, Copyrightmon& defender, int attack_choice){
//     int base_damage = 10; // Base damage for all attacks
//     // Type effectiveness
//     base_damage += attacker.level * 2; // Increase damage based on level
//     if(attacker.type.strengths == defender.type.num){
//         base_damage *= 2; // Double damage for strengths
//     } else if(attacker.type.weaknesses == defender.type.num){
//         base_damage /= 2; // Half damage for weaknesses
//     }
//     return base_damage;
// }

// int battle(Copyrightmon& player, Copyrightmon& opponent){
//     cout << "A wild " << opponent.name << " appeared!" << endl;
//     while(player.current_hp > 0 && opponent.current_hp > 0){
//         cout << "Choose an attack:" << endl;
//         cout << "1. " << player.attacks[0].name << endl;
//         cout << "2. "<< player.attacks[1].name << endl;
//         cout << "3. "<< player.attacks[2].name << endl;
//         int attack_choice = input();
//         int damage = calculate_damage(player, opponent, attack_choice);
//         opponent.current_hp -= damage;
//         cout << player.name << " used attack " << attack_choice << " and dealt " << damage << " damage!" << endl;
//         if(opponent.current_hp <= 0){
//             cout << opponent.name << " fainted!" << endl;
//             break;
//         }
//         int opp_damage = calculate_damage(opponent, player, 1);
//         player.current_hp -= opp_damage; // Opponent uses first attack
//         cout << opponent.name << " attacked and dealt " << opp_damage << " damage!" << endl;
//         if(player.current_hp <= 0){
//             cout << player.name << " fainted!" << endl;
//             break;
//         }
//     }
//     return 0;
// }
#include <iostream>
#include <string>
#include <vector>

using namespace std;




int main(){
    return 0;
 }