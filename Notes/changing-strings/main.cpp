// CS Changing Strings

// How do I get a substring from within a string?
    // var.substr(starting index,number of characters you want to use)
// How do I create an escape character in C++
    // \" \" add quotes,\n newline \t tab. raw string R"()""
// How do I convert a string to another data type?
    // 
// What is a raw string and when would I use it?
    // 
#include <iostream>
#include <string>
using namespace std;

string name = "cecily Strong";
string sentence = "The quick brown fox jumps over the lazy dog";

int main(){
    auto index = name.find(' ');
    string first_name = name.substr(0,index);
    string last_name = name.substr(index+1);
    first_name[0]=toupper(first_name[0]);
    //first_name[0]=tolower(first_name[0]);

    cout << first_name << endl << last_name << endl;

    for (int i = 0; i < size(sentence); i++){
        if (isspace(sentence[i])){
            sentence[i] = 'ඞ';
        }else if (isupper(sentence[i])){
            sentence[i] = tolower(sentence[i]);
        }else {
            sentence[i] = char(int(sentence[i] + 4) % 26 + 97);
        }
    }
    cout << sentence << endl;

    cout << R"(This is a \"question\"\n\t ...I think)";

    return 0;
}