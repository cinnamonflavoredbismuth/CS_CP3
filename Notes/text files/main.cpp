//CS Text files
/*
What are the 3 main sources of data for a program
    terminal - cout, cin (user data)
    file - txt, csv, binary
    network - internet
What are streams?

What are the different streams we might need to include in a program? 
    istream (read), ostream (write), iostream (input and output)
What is the base class for all streams?
    ios
What is buffer?
    a temporary storage in memory for reading values
How do you clear the buffer?
    cin.ignore()
How do you handle invalid inputs from the terminal
    cin.fail()
What streams are for files specifically
    ifstream - input filestream
    ofstream - output file stream
    fstream - combines functionality of both
    iomanip - manipulation
How do you write to a text file?
    file << "words"
What do stream manipulators let us do?
    let you use columns and stuff
How do you write to a CSV?
    basically the same
How do you read a text file?
    file >> variable
How do you read a CSV file?
    basically the same
What is a delimiter?
    a seperator of values, such as a comma
How do you read an entire CSV?
for line in csv:
    split line by delimiter
    store values in object
How do you turn items from a CSV into objects of a structure?
    create a structure that matches the data
    read each line, split by delimiter, store in structure
*/

#include <iostream>
#include <limits>
#include <fstream>
#include <iomanip>
#include <vector>

using namespace std;

int get_number(const string& prompt)   {
    int num;
    while(true){
        cout << prompt <<endl;
        cin >> num;
        if(cin.fail()){
            cout  << "give me a valid number: "<<endl;
            cin.clear();
            cin.ignore(numeric_limits<streamsize>::max(),'\n'); //clears buffer
        }else break;
    }
    cin.clear();
    cin.ignore(numeric_limits<streamsize>::max(),'\n');
    return num;
}

struct Movie {
    int id;
    string title;
    int year;
};
int main(){
    int first = 1;
    int second = 1;
    /*first = get_number("first: ");
    second = get_number("second: ");*/
    cout << "you enetered " << first << " and " << second << endl;
     
    //WRITE
    ofstream file;
    file.open("data.txt"); //create or open file
    if (file.is_open()){
        file << setw(10) << "Hello" << setw(10) << "world";
        file.close();
    }
    file.open("data.csv"); //create or open file
    if (file.is_open()){
        file << "id, title, year\n";
        file << "1, terminator 1, 1984\n";
        file << "2, terminator 2, 1984\n";
        file.close();
    }

    //READ
    ifstream ifile;
    ifile.open("data.csv");
    string str;
    vector<Movie> movies;
    if (ifile.is_open()){
        while(!ifile.eof()){
            getline(ifile, str,',');
                if (str.empty()) continue;;
            Movie movie;
            movie.id = stoi(str);

            getline(ifile, str,',');
            movie.title = str;

            getline(ifile, str,',');
            movie.year = stoi(str);

            movies.push_back(movie);
        }
        file.close();
    }
    for (Movie i:movies){
            cout << "Title: " << i.title << "Year: " << i.year << endl;
        }
        
    return 0;
}