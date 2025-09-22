//CS Calculator
/*Write a program that creates a user menu for a basic calculator using enumeration in C++. The calculator should be able to perform addition, subtraction, multiplication, and division. The program should display a menu of options, allow the user to select an operation, input two numbers, perform the calculation, and display the result. The program must continue to run till the user chooses to exit and have proper input handling. */
#include <iostream>
#include <string>
#include <vector>
using namespace std;
enum Calculate{
    Add=1,
    Subtract=2,
    Multiply=3,
    Divide=4,
    Exit=5
};

int main(){
    int input;
    float num1;
    float num2;
    int finalNum;
    bool running = 1;

    while (running == 1){
    cout << "What operation do you want to perform?"<<endl
    <<"1: Add"<<endl
    <<"2: Subtract"<<endl
    <<"3: Multiply"<<endl
    <<"4: Divide"<<endl
    <<"5: Exit"<<endl;

    while(!(cin >> input)){
        cout<<"Please enter a number option: "<<endl;
        cin.clear();
        cin.ignore(10000);
    }

    if(input == Calculate::Exit){
        running=0;
        }

    else{
        
        cout<<"Input your first number: ";
        cin>>num1;
        cout<<"Input your second number: ";
        cin>>num2;
        if (input == Calculate::Add){
            finalNum = num1+num2;
            }
        else if (input == Calculate::Subtract){
            finalNum = num1-num2;
            }
        else if (input == Calculate::Multiply){
            finalNum = num1*num2;
            }
        else if (input == Calculate::Divide){
            finalNum = num1/num2;
            }
        
        cout<<"Your number is: "<<finalNum<<endl<<endl;
        }
    }
    return 0;
    
}