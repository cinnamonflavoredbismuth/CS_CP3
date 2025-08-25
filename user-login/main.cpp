// CS User Login
// Write a program that takes in a user name and checks to see if that user is an admin, returning user, or a new user and then says hello to them accordingly. 
/*EXAMPLE:
Hello Admin Ms.LaRose
Welcome back Andrew
Lets get you signed up Katie*/

#include <iostream>
#include <string>
using namespace std;

int main(){
    string admins[2] = {"cecily","mrs.larose"};
    string returning_users[2]= {"andrew","john"};
    string username = "";
    cout << "Enter your username: ";
    cin >> username;
    int num=0;
    bool found = false;
    while (found == false && num < 2) {
        if (username == admins[num]) {
            cout << "Hello Admin " << username;
            found = true;
        }
        else if (username == returning_users[num]) {
            cout << "Welcome back " << username;
            found = true;
        }
        else if (num == 1) {
            string new_user;
            cout << "Lets get you signed up " << username;
            cout << "\nPlease enter a new username: ";
            cin >> new_user;
            cout << "You are now signed up, " << new_user;


            found = true;
        }
        num++;
    }
    
    /*cin >> username;
    if username in admins {
        cout << "Hello Admin " << username;
    } else {
        cout << "Welcome back " << username;
    };"*/
    return 0;
}