// CS User Structure
// Write a program that takes in a username, password, and admin status (you can do more but that is the minimum). The program then uses that information to create a user object from a structure. 

// It then needs to compare that user with a list of already existing users (10 users minimum) to see if the user already exists.

#include <iostream>
#include <string>
#include <vector>
using namespace std;

struct User {
    string username;
    string password;
    bool isAdmin = false;
};


bool operator==(const User& first, const User& second){
        return (first.username == second.username && 
            first.password == second.password &&
            first.isAdmin == second.isAdmin
        );
    }

ostream& operator << (ostream& stream, User& user){
    stream << user.username;
    return stream;
}

void showUser(User* user) {
    cout << user -> username << endl;
}

string check_user(auto users, int size){ 
    string name;
    cout << "Enter username: ";
    getline(cin, name);
    for (int i = 0; i < users.size(); i++){
        if (users[i].username == name){
            cout << "User already exists!" << endl;
            check_user(users, size);

        } 
    }
    return name;
}

int main(){
    // setup existing users
    vector<User> users;
    string usernames[10] = {"admin", "user1", "user2", "user3", "user4", "user5", "user6", "user7", "user8", "user9"};
    string passwords[10] = {"password123", "mypassword", "letmein", "qwerty", "123456", "password1", "abc123", "iloveyou", "admin123", "welcome"};
    bool adminStatus[10] = {true, false, false, false, false, false, false, false, false, false};
    for (int i = 0; i < 10; i++){
        users.push_back({usernames[i], passwords[i], adminStatus[i]});
    }
    /*
    }*/

    // get new user info
    User newUser;
    string name = check_user(users, users.size());
    cout << name;
    newUser.username = name;
    cout << "Enter password: "; 
    cin >> newUser.password;
    cout << "are you an admin? (1 for yes, 0 for no): ";
    cin >> newUser.isAdmin;
    users.push_back(newUser);
    cout << "Hello " << newUser.username;
    cout << "Users:";
    for (int i = 0; i < users.size(); i++){
        showUser(&users[i]);}
    return 0;
}