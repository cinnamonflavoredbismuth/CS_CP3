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
    string admins[2] = {"Cecily","Mrs. LaRose"};
    string returning_users[6]= {"Edward","Jon","Jervis","Darius","Waylon"};
    string username = "";
    cout << "Enter your name (please capitalize accordingly): " << endl;
    cin >> username;
    int num=0;
    bool found = false;
    while (found == false && num < 3) {
        if (username == admins[num]) {
            cout << "Hello Admin " << username << endl;
            found = true;
        }
        else if (username == returning_users[num]) {
            cout << "Welcome back " << username;
            found = true;
        }
        else if (num == 1) {
            //string new_user;
            cout << "Lets get you signed up " << username << endl;
            cout << "Please enter a new username: ";
            cin >> username;
            returning_users[3]=(username);
            cout << "You are now signed up, " << username << endl;
            found = true;
        }
        else {
        num++;
        }
    }
    cout << "Admins:" << endl;
    for ( int x = 0; x < 2; x++ ) {
        cout << "   "<< admins[x] << endl;
    }
    cout << "Returning Users:" << endl;
    for ( int x = 0; x < 3; x++ ) {
        cout << "   "<< returning_users[x] << endl;
    }
    return 0;
}