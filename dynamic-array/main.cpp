// CS Dynamic Array 

// Write a program that asks the user to enter books, movies, shows, colors, comics, etc. until they can't think of anymore. 
// Start your array with only 5 spaces. Continue to increase the size of the array as your user hits the array cap. 
// THEN, print out each of the inputs they gave you!
#include <iostream>
#include <memory>
using namespace std;

 int capacity = 5;
// *list = {'a'};
shared_ptr<string[]> inputs(new string[capacity]);
//auto inputs = make_shared<string>(capacity);
//string* list = new string[capacity];
int entries = 0;

int print_all(string* arr, int size){
    if (size == 2) {
        cout << arr[0];
    }else{
    for (int i = 0; i < size - 1; i++){
        cout << arr[i] << ", ";
    }
    return 0;
    }
}

int get_items(){
        while (true){
        cout << "Enter a book (press 1 to stop): ";
        getline(cin, inputs[entries]);
        if (cin.fail()) break;
        if (inputs[entries] == "1") break;
        entries++;
        if (entries == capacity){
            capacity += 1;
            shared_ptr<string[]> temp(new string[capacity]);
            for (int i = 0; i < entries; i++)
                temp[i] = inputs[i];
            //delete[] inputs;
            inputs = temp;
        }
    }

    return 0;
}

int main(){
    while (true){
    int exit = 0;
    get_items();
    print_all(inputs[], capacity);
    cout << "press 1 to exit";
    cin >> exit;
    if (exit == 1) break;
    }
    return 0;
}