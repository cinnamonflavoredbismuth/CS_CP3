/* CS Enumeration Notes

What is enumeration?
A more convinent way to work with sets of input options.

How do you build enumeration?
enum Action{
    List = 1,
    Add = 2,
    Update = 3
};

How do we display our enumerator? 
cout << "1: List invoices" << endl <<
    "2: Add invoices" << endl <<
    "3: Update invoices" << endl <<
    "Select: ";

Why does it matter that enumerators are constants?
So that we don't accidentally change the values.

What is the default beginning enumerator? 
0,1,2,3,etc

How do you give a different default value?
enum Action{
    List = 1,
    Add = 2,
    Update = 3
};

What is a strongly typed enumerator?
enum class Emu{
    List = 1,
    Add = 2,
    Update = 3
};

How are strongly typed enumerators different from a normal one?
We have to specifically cast them to compare stuff.


*/

#include <iostream>
#include <string>
#include <vector>

using namespace std;
enum Action{
    List = 1,
    Add = 2,
    Update = 3
};

enum class Emu{
    List = 1,
    Add = 2,
    Update = 3
};

int main() {
    int input;

    cout << "1: List invoices" << endl <<
    "2: Add invoices" << endl <<
    "3: Update invoices" << endl <<
    "Select: ";
    cin >> input;
    if (input == Action::List) {
        cout << "List invoices" << endl;
    }else if (input == Action::Add) {
        cout << "Add invoices" << endl;
    }else if (input == static_cast<int>(Emu::Update)) {
        cout << "Deciever, deciever, slice thine pantaloons with a cleaver!" << endl;
    }else{
        cout << "Womp womp." << endl; 
    }
    return 0;
}