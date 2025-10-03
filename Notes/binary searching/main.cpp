//CS Binary Searching

/*What is a potential issue with converting values to strings without control?
    you might get unwanted formatting, like extra zeros
How can you control the way a value is converted to a string?
    stringstream
Why is it useful to create a reusable function for converting values to strings?
    so you dont have to rewrite the same code
What is parsing in the context of working with strings?
    extracting a piece of information from a string
How do you extract specific information from a string in programming?
    using stringstream and getline
When a title contains a space, which function should you use to read it properly?
    getline()
Why might extra zeros be added to a string when converting a value without control?
    because of default formatting
How does controlling the string conversion process benefit your program?
    it makes it more predictable and easier to read
Give an example scenario where parsing a string would be necessary in a program.
    putting a csv line into an object
When writing to a binary file, what does the first parameter (reinterpret_cast<char*>(&numbers)) represent?

Why does the binary file only take 12 bytes while the array of integers might be larger?

What is the main difference between sequential search and binary search?

In which type of data structure is binary search most efficient?

What is a key requirement for binary search to work correctly on a list?

How does sequential search find an item in a list?

Why is binary search generally faster than sequential search for large, sorted lists?

*/
#include <iostream>
#include <fstream>
#include <iomanip>
#include <sstream>
/* Convert other data types to strings
istringstream => reading a string
ostringstream => writing a string
stringstream => both
*/

using namespace std;

string to_string(double number, int precision){
    stringstream stream;
    stream << fixed << setprecision(precision) << number; // method in setprecision is how many decimal places
    string str = stream.str();
    return str;
};

struct Movie {
    string title;
    int year;
};

Movie challenge(string str){
    stringstream stream;
    stream.str(str);

    Movie movie;
    getline(stream, movie.title,',');
    stream >> movie.year;

    return movie;
};

int main(){
    double number = 3.14;
    cout << to_string(number,2) << endl;

    //parsing
    string users = "10 20";
    stringstream fix;
    fix.str(users);
    int first;
    fix >> first;
    
    int second;
    fix >> second;

    cout << "first: " << first << endl << "second: " << second << endl;

    auto movie = challenge( "A New Hope,1977");
    cout << "Title: " << movie.title << endl << "Year: " << movie.year << endl;

    fstream file;
    file.open("file.txt",ios::in | ios::out | ios::app); //how opening a file
    if (file.is_open()){
        
        file.close();
    }

    return 0;
}