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
    // basically a list of things with the same data type
// How do I create an array?
    // name[side] = {values};
// How do you make strings in C?
    // char name[7] = "cecily";
// How did C++ improve creating strings? 
    // string name = "cecily";
// How do I search a string?
    // .length(), > check alphabetical order, .starts_with(), .ends_with(), .empty(), .front() <= returns the first character, .back() <= returns the last character
// How do I modify a string?
    //  .append(), .insert(), .erase(), .replace(), .pop_back(), .push_back(), .clear()
// What are some string methods? 
    // .length(), > check alphabetical order, .starts_with(), .ends_with(), .empty(), .front() <= returns the first character, .back() <= returns the last character, .find_first_of(), .find_first_not_of(), find_last_of(), .find_last_not_of()

int random_number(){
    int sec = time(nullptr);
    srand(sec) ;
    int my_num = rand() % 11;
    cout << my_num << endl;
    return my_num;
}

int main(){
    random_number();

    int grades[11] = {0,1,2,3,4,5,6,7,8,9,10};
    cout << grades[1] << endl;

    char inferior_name[7] = "Cecily";
    cout << inferior_name << endl;

    string sentence = "the quick brown fox jumps over the lazy dog";
    cout << sentence << endl;
    cout << sentence.length() << endl;
    cout << (sentence > inferior_name) << endl;
    return 0; 
}