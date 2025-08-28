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
    // you have to have the square brackets on the argiments
// What is type_t
    //  a data type that is used to represent the size of data types
// Why would we use type_t
    // you use it instead of specifying data types
// How do you search an array
    // using for loops and checking each item
// How do you make a multi-dimensional array
    // 
#include <iostream>
#include <limits>
using namespace std;

string fam[5] = { "Jeremy","Cecily","Simon", "Oliver", "Coco"};
string sibs[3] = {"Simon", "Oliver", "Coco"};

int search(string list[], size_t len, string item){
    for(int i=0; i < len; i++){
        if (list[i] == item){
            cout << "you are a sibling\n";
            return 1;
        }
    } 
    cout << "you are a parent\n";
    return 0;
}
    

int main(){
    // cout << fam << endl;
    //search(fam, "Cecily");
    for(int i = 0; i < size(fam); i++){
        cout << fam[i] << " Strong\n";
        search(sibs, size(sibs), fam[i]);
        // 
        //     cout << "They are a sibling!\n";
    }

    // SIZE OF T
    cout << numeric_limits <long long>::min()<<endl;
    cout << numeric_limits <long long>::max()<<endl;
    cout << numeric_limits <size_t>::min()<<endl;
    cout << numeric_limits <size_t>::max()<<endl;

    //STRUCTURED BINDING
    auto [q,w,e,r,t] = fam;
    cout << e << endl;
    

    return 0;


    // MULTI DIMENSIONAL LIST
    int matrix = {{1,2,3},
                  {1,2,3},
                  {1,2,3}};
}