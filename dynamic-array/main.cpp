// CS Dynamic Array 

// Write a program that asks the user to enter books, movies, shows, colors, comics, etc. until they can't think of anymore. 
// Start your array with only 5 spaces. Continue to increase the size of the array as your user hits the array cap. 
// THEN, print out each of the inputs they gave you!
#include <iostream>
using namespace std;

int capacity = 5;
string* list = new int[capacity];

int entries = 0;

int print_all(string* arr, int size){
    for (int i = 0; i < size; i++){
        cout << arr[i] << endl;
    }
    return 0;
}

int get_items(){
        while (true){
        cout << "Enter a number: ";
        cin >> list[entries];
        if (cin.fail()) break;
        entries++;
        if (entries == 5){
            capacity += 5;
            int* temp = new int[capacity];
            for (int i = 0; i < entries; i++)
                temp[i] = list[i];
            delete[] list;
            list = temp;
        }
    }

    return 0;
}

int main(){
    return 0;
}