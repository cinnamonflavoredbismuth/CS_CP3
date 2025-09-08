//CS Pointers notes

// What is a pointer?
    // A specific variable that holds the address of a variable in the memory
// Why do we use pointers?
    // hold address instead of information
// How do I create a pointer
    // int* pvar = &var;
// What is indirection or de-referencing?
    // when you use * and the var to return the value
// What are constant pointers? How are the different types used?
    // data constant, location diff
// How do you pass a pointer into a function?
    // you use type* var
// Why would you pass a pointer to a function?
    // sometimes you have a very large piece of data you need to pass into a function and you don't want to pass all of it in there
// How do you compare pointers?
    // compaison operators, see if they point to the same location
// What is dynamic memory allocation?
    // you can overwite how much memory you want to use for an array. delete when done
// What is the Stack?
    // Stack of plates, last in first out
// What is the Heap?
    // box of stuff, you have to organize it yourself
// What are smart pointers?
    // unique: owns that piece of memory. shared:
#include <iostream>
using namespace std;

int numbers[] = {4, 2, 6, 8, 14, 24, 65};
void divide(int* list, int size){
    for(int i = 0; i < size; i++){
        
        list[i] = list[i]/2;
        cout << list[i] << endl;
        
    }
    cout << "this is my numbers list " << *list << endl;
}

int capacity = 5;
int* goop = new int[capacity]; // 5 slots for goop levels
int entries = 0;



int main(){


    int num = 4;
    int* pnum = &num;
    int day = 5;
    *pnum = 8;
    int month = 9;


    const double pi = 3.14;
    const double gpa = 3.999999;

    const double* ppi = &pi; // can change location, can't change val
    ppi = &gpa;

    int* const pday = &day; // change val, cant change location
    *pday = 6;

    const int* const pmonth = &month; // cant change location or value

    cout << "The number is " << num << endl;
    cout << "the location of num is " << *pnum << endl;

    divide(numbers, size(numbers) );

    cout << (pnum == pday) << endl;
    cout << (pnum > pday) << endl;

    if (pnum != nullptr){
        cout << *pnum << endl;
        pnum++;
    }
    cout << *pnum << endl;

    while (true){
        cout << "Enter a number: ";
        cin >> goop[entries];
        if (cin.fail()) break;
        entries++;
        if (entries == 5){
            capacity += 5;
            int* temp = new int[capacity];
            for (int i = 0; i < entries; i++)
                temp[i] = goop[i];
            delete[] goop;
            goop = temp;
        }
    }

    for (int i = 0; i < entries; i++){
        cout << goop[i] << ", ";
    }
    delete[] goop;

    return 0;
}