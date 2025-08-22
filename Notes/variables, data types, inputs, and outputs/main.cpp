// CS Variables, Data Types, Inputs, and outputs


// How are static and dynamically typed variables different?
    // dynamic tries to detective, static is where you tell the computer everything

// REMINDER: What is the difference between initializing and declaring a variable?
    // declare is data type and then name
    // initializing is giving it a value
    // best practice is initilizing and declare at same time, on own line

// data types:
    // short 2 bytes, -32768 -- 32768
    // int, 4 bytes, -2b to 2b
    // long, 4 bytes, -2b to 2b,
    // long long, 8 bytes, big #s
    // floats, 4 bytes, 3.4E38 both directions
    // double, 8 bytes, 1.7E308 both directions
    // long double, 8 bytes, 3.4E932 both directions
    // bool, 1 byte, True/False
    // char, 1 byte, one letter

// Variables are single quites, outputs are doube quites

// What case type should be used for c++ variables?
    // snake_case

// What is the C++ standard library?
    // <iostream>

// How do you access the standard library?
    // #include <iostream>

// How do you create an output in C++?
    // cout << [var]

// How do you create an input in C++?
    // cin >> ['input text]

// What is the stream in C++?
    // direction things are going

// What is a constant?
    // a value that will never change
    // const data type name

// Why do we write constants?
    // so you can have a constant number without it being able to change in case you forget
    
#include <iostream>
using namespace std;
int main(){
    int students = 11;
    long years = 255l; //if no l at end, long will convert to integer
    float pi = 3.14f; // float will compile to a double without an f at the end
    bool on = true;
    short days = 5;
    char name = 'g';
    cout << "tell me your age ";
    int age;
    cin >> age;
    cout << "you are " << age<<" years old";
    return 0;
}