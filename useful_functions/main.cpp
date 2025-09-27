//Useful functions
#include <iostream>
#include <vector>
#include <string>
using namespace std;


// RANDOM FUNCTION

#include <ctime>
#include <chrono>
#include <thread>

int random_number(int max){
    int sec = time(nullptr);
    this_thread::sleep_for(chrono::seconds(1));
    srand(sec) ;
    int my_num = rand() % (max+1); //generates a number between 0 and the number you put in
    //cout << my_num << endl;
    return my_num;
}


// INPUT
int input(){ 
    int input=0;   
    while(!(cin >> input)){
        cout<<"Please enter a number option: "<<endl;
        cin.clear();
        cin.ignore(10000);
    }
    return input;
    }

    
// Main :3
int main(){
    return 0;
}