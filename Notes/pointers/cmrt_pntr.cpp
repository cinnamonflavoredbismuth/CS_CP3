// CS Spart pointers
// unique 
    // owns that piece of memory. generic, can work with diff data types
// shared
    // multiple pointers pointing to the same thing. generic. clean up after itself
#include <iostream>
#include <memory>
using namespace std;

int main(){
    unique_ptr<int> x(new int);
    auto y = make_unique<int>();
    *x = 10;
    *y = 7;
    cout << *x << endl;
    cout << *y << endl;

    //shared pointers
    
    auto z = make_shared<int>();
    *z = 4;

    cout << '(' << *x << ", " << *y << ", " << *z << ')' << endl;

    return 0;
}