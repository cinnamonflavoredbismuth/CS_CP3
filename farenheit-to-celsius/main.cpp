// CS Farenheit to Celsius

// Write a program that takes in a temperature in Fahrenheit, converts it to Celcius and then prints for your user that the given temperature in Fahrenheit is the new amount in Celsius.

// OUTPUT EXAMPLE: 

// 50 degrees Fahrenheit is 10 degrees Celsius

// KEY REMINDERS:
// Remember you have to set your variable types
// Division will not give you a decimal unless at least 1 of your input numbers is a decimal type
// You have to get the standard library to create your inputs and outputs
// Make sure your arrows are pointing the right way for the input/output stream. 

// °C = (°F - 32) × 5/9
#include <iostream>
using namespace std;

int main(){
    int number = 0;
    cout << "What tempature in Farenheit do you want to convert to Celsius? ";
    cin >> number;
    float final = (number - 32) / (9.0/5.0);
    //float num_times = 5/9;
    cout << number << " degrees Farenheit is " << final << " degrees Celsius";

    //number = cin >> "what";
    return 0;
}