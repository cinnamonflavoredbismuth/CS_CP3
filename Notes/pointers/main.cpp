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
    // 
// What is dynamic memory allocation?
    // 
// What is the Stack?
    // 
// What is the Heap?
    // 
// What are smart pointers?
    // 
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



    return 0;
}