// CS Strings, Arrays, conditionals
#include <iostream>
#include <cstdlib>
#include <ctime>
using namespace std;
// What is Narrowing?
    // you take a variable that already exists and moves its contents into a variable that takes up a smaller amount of space. you will loose information bc theres not enough space

// for big numnbers, use apostrophies instead of commas

// What is a basic way to generate random numbers in C++?
    // seed the random
// What is an array?
    // 
// How do I create an array?
    // 
// How do you make strings in C?
    // 
// How did C++ improve creating strings? 
    // 
// How do I search a string?
    // 
// How do I modify a string?
    // 
// What are some string methods? 
    // 

int main(){
    int sec = time(nullptr);
    srand(sec) ;
    int my_num = rand() % 11;
    cout << my_num;
    return 0; 
}