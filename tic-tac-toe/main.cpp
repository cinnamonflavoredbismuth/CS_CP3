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

int prnt_board(){
    cout << endl;
    for(int row = 0; row < 3; row++){
        cout << "| ";
        for (int col = 0; col < 3; col++){
            cout << board[row][col] << " | ";
        }
        cout << endl << "-------------" << endl;
    }
    cout << endl;
    return 0;
}

int check (string board){
    for (int i = 0; i < 3; i++){
        if (a[i]==b[i] and b[i]==c[i]){
            return 1;
        };
    };
    return 0;
}

int win_check(){
    int win = 0;
    int player = 0;
    while (win == 0){
        for (int i = 0; i < 3; i++){
            if (a[i]==b[i] and b[i]==c[i]){
            if (a[i] == "X"){
                    win = 1;
                    player = 1;
                break;}
            else if (a[i] == "O"){
                    win = 1;
                    player = 2;
                break;}
                else{
                    win = 0;
                }
            }else{
                win = 0;
            };
        }
    

        for (int i = 0; i < 3; i++){
            if (board[i][0]==board[i][1] and board[i][1]==board[i][2]){
                if (board[i][0] == "X"){
                    win = 1;
                    player = 1;
                break;}
                else if (board[i][0] == "O"){
                    win = 1;
                    player = 2;
                    break;
                    }
                else{
                    win = 0;
                }
            }else{
                win = 0;
            };}


        if (board[0][0]==board[1][1] and board[2][2]==board[1][1]){
            if (board[0][0] != " "){
                win = 1;} else{
                    win = 0;
                }
        }else{
            win = 0;
        }}

        if (board[0][2]==board[1][1] and board[0][2]==board[1][1]){
            if (board[0][2] != " "){
                win = 1;} else{
                    win = 0;
                }
        }else{
            win = 0;
    };

    if (win == 1){
        if (player == 1){
            cout << "You win!\n";}
        else{
            cout << "The computer wins!\n";
        }
        return 1;}
    else{return 0;}
}

int random_number(int max){
    int sec = time(nullptr);
    srand(sec) ;
    int my_num = rand() % (max+1); //generates a number between 0 and the number you put in
    //cout << my_num << endl;
    return my_num;
}

int add_board(string player, int input){
    if (input == 1){
        board[0][0] = player;
    }
    else if (input == 2){
        board[0][1] = player;
    }
    else if (input == 3){
        board[0][2] = player;
    }
    else if (input == 4){
        board[1][0] = player;
    }
    else if (input == 5){
        board[1][1] = player;
    }
    else if (input == 6){
        board[1][2] = player;
    }
        else if (input == 7){
        board[2][0] = player;
    }
    else if (input == 8){
        board[2][1] = player;
    }
    else if (input == 9){
        board[2][2] = player;
    }
    prnt_board();
    return 0;
}

int valid_move(int input){
    if (input < 1 or input > 9){
        return 0;
    }else{
    if (input == 1){
        if (board[0][0] != " "){
            return 0;
        }
    }
    else if (input == 2){
        if (board[0][1] != " "){
            return 0;
        }
    }
    else if (input == 3){
        if (board[0][2] != " "){
            return 0;
        }
    }
    else if (input == 4){
        if (board[1][0] != " "){
            return 0;
        }
    }
    else if (input == 5){
        if (board[1][1] != " "){
            return 0;
        }
    }
    else if (input == 6){
        if (board[1][2] != " "){
            return 0;
        }
    }
        else if (input == 7){
        if (board[2][0] != " "){
            return 0;
        }
    }
    else if (input == 8){
        if (board[2][1] != " "){
            return 0;
        }
    }
    else if (input == 9){
        if (board[2][2] != " "){
            return 0;
        }
    }else{
        return 1;}
    return 1;}
    
}

int computer_move(string player = "O"){
    int move;
    move = random_number(9);
    //cout << move <<  endl;
    //cout << valid_move(move) << endl;
    if (valid_move(move) == 1){
        add_board(player, move);}
    else{
        computer_move();}
    return 0;
}

int player_move(){
    int move;
    cout << "Enter your move (1-9): ";
    cin >> move;
    if (valid_move(move) == 1){
        add_board("X", move);
        //prnt_board();
    }
    else{
        cout << "Invalid move, try again" << endl; 
        player_move();}
    return 0;
}



int play_game(){
    int won = 0;
    prnt_board();
    while (won == 0){
        player_move();
        //computer_move("X");
        won = win_check();
        computer_move();
        won = win_check();
        cout << won << endl;
    }
    cout << won << endl;
    return 0;
}

int main(){
    play_game();
    return 0;
}