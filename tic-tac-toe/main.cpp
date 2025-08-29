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
string board[3][3] = { 
    {" "," "," "}, 
    {" "," "," "}, 
    {" "," "," "}
 };

auto [a,b,c] = board;

int check (string board){
    for (int i = 0; i < 3; i++){
        if (a[i]==b[i] and b[i]==c[i]){
            return 1;
        };
    };
    return 0;
}

int random_number(int max){
    int sec = time(nullptr);
    srand(sec) ;
    int my_num = rand() % (max+1); //generates a number between 0 and the number you put in
    cout << my_num << endl;
    return my_num;
}

int prnt_board(auto board){
    for(int row = 0; row < 3; row++){
        string item[3] = board[row]
        for (int i = 0; i < 3; i++){
            cout << item[i] << " ";
        }
        cout << '\n';
    }
    return 0 
}


int main(){
    prnt_board(board);
    cout << "" ;
    return 0;
}