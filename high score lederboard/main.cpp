// CS High score leaderboard
/*Write a program that manages a high score leaderboard for a game using file I/O in C++. 
The program should allow the user to add new high scores, view the existing leaderboard, and save the data to a text file. 
It should also read data from the file when the program starts. 
The user menu should include options to add a new score, display the high scores, and exit. 
The program must handle invalid inputs gracefully and continue running until the user chooses to exit.*/
#include <iostream>
#include <limits>
#include <fstream>
#include <vector>
#include <iomanip>

using namespace std;

int int_input(string message = "Please enter a number: "){ 
    int input=0;   
    while(!(cin >> input)){
        cout<<message<<endl;
        cin.clear();
        cin.ignore(10000);
    }
    return input;
    }


struct UserScore {
    int id;
    string name;
    int score;
};

vector<UserScore> scores;

void write(const vector<UserScore>& scores){
    ofstream file;
    file.open("leaderboard.csv"); //create or open file
    if (file.is_open()){
        file << "id, name, score\n";
    for (UserScore i:scores){
        file << i.id << ','<< i.name << "," << i.score << "\n";
    }
    file.close();}
}

vector<UserScore> read(){
    ifstream file;
    string line;
    vector<UserScore> scores;

    file.open("leaderboard.csv");

    if (file.is_open()){
        getline(file, line); //skip header line
        while(getline(file,line)){
            istringstream iss(line);
            string item;
            UserScore score;

            getline(iss, item,',');
            score.id = stoi(item);

            getline(iss, item,',');
            score.name = item;

            getline(iss, item,',');
            score.score = stoi(item);

            scores.push_back(score);
        }
        file.close();
    }
    return scores;
}

void display_scores(const vector<UserScore>& scores){
    cout << "High Score Leaderboard:\n";
    for (UserScore i:scores){
        cout  << setw(7)<< i.name << " |  "  << i.score << endl;
    }
    cout << "\n";
}

void add_score(vector<UserScore>& scores){
    UserScore newScore;
    newScore.id = scores.size() + 1;
    cout << "Enter player name: ";
    cin.ignore();
    getline(cin, newScore.name);
    //cin >> newScore.name;
    cout << "Enter player score: ";
    cin >> newScore.score;
    scores.push_back(newScore);
    cout << "Score added successfully!\n\n";
    write(scores);
}

enum Action{ 
    Add = 1,
    View,
    Exit
};

int main(){
    while (true) {
        scores = read();
        cout << "Menu:\n1. Add New Score\n2. View Leaderboard\n3. Exit\nChoose an option: ";
        int choice;
        choice = int_input();

        if (choice == Action::Add) {
            add_score(scores);
        } else if (choice == Action::View) {
            display_scores(scores);
        } else if (choice == Action::Exit) {
            cout << "Exiting program.\n";
            break;
        } else {
            cout << "Invalid choice. Please try again.\n";
        }
    }
    return 0;
}