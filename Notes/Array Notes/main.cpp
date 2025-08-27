//CS Array Notes
// How are for loops constructed in C++
    // for (int i = 0; i < #; i++) {
// How do you loop through an array
    // for (int i = 0; i < size(array); i++) {
// When do you need to use curly brackets in C++
    // When you have more than one line of code in a conditional or loop
// How do you compare items in arrays
    // you have to go through a for loop and compare each item individually
// How do you use an array as an argument in a function
    //
// What is type_t
    //  
// Why would we use type_t
    //
// How do you search an array
    //
// How do you sort an array
    //
// How do you make a multi-dimensional array
    //
#include <iostream>
using namespace std;

string fam[5] = { "Jeremy","Cecily","Simon", "Oliver", "Coco"};
string sibs[3] = {"Simon", "Oliver", "Coco"};

void search(string list, string item){
    cout << list << endl;}

int main(){
    search(fam, "Cecily");
    for(int i = 0; i < size(fam); i++){
        cout << fam[i] << " Strong\n";
        if (fam[i] == sibs[i-2])
            cout << "They are a sibling!\n";
    }

    return 0;
}