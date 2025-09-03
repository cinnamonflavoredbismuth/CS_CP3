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
    // var[row][column]{{1,2,3}, {1,2,3}, {1,2,3}}
// how to sort an array
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
    

int sort(int list[],int size){
    for (int j = 0; j < size; j++){
        for (int i = 1; i < (size); i++){
            if (list[i] < list[i-1]){ // THIS IS WHERE YOU WANT IT IN ORDER OR REVERSE ORDER
                int a = list[i];
                list[i] = list[i-1];
                list[i-1] = a;
            }
        }
    }
    return 0;
}

int prnt_list(int list[],int size){
    for(int i = 0; i < size; i++){
         cout << list[i] << " ";}
    cout << "\n";
    return 0;
}

int main(){
    // cout << fam << endl;
    //search(fam, "Cecily");
    // for(int i = 0; i < size(fam); i++){
    //     cout << fam[i] << " Strong\n";
    //     search(sibs, size(sibs), fam[i]);
    //     // 
    //     //     cout << "They are a sibling!\n";
    // }

    // // SIZE OF T
    // cout << numeric_limits <long long>::min()<<endl;
    // cout << numeric_limits <long long>::max()<<endl;
    // cout << numeric_limits <size_t>::min()<<endl;
    // cout << numeric_limits <size_t>::max()<<endl;

    // //STRUCTURED BINDING
    // auto [q,w,e,r,t] = fam;
    // cout << e << endl;

    // // MULTI DIMENSIONAL LIST
    // int matrix[3][3] = {{1,2,3},
    //                     {4,5,6},
    //                     {7,8,9}};   
    int list[6]={3,1,5,4,7,9};
    prnt_list(list,size(list));

    sort(list,size(list));

    prnt_list(list,size(list));

    return 0;



}