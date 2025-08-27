// CS Tic Tac Toe
// Create a tic tac toe game where the user plays against a random number generator. Save the locations on the board as a multidimensional array.
#include <iostream>
#include <cstdlib>
#include <ctime>
using namespace std;
/*
   |   |   |
   |   |   |
   |   |   |*/

int random_number(int max){
    int sec = time(nullptr);
    srand(sec) ;
    int my_num = rand() % (max+1); //generates a number between 0 and the number you put in
    cout << my_num << endl;
    return my_num;
}

int main(){
    cout << "" ;
    return 0;
}