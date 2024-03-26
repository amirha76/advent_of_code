#include <iostream>
#include <fstream> // need for file operations 
#include <string>
#include <cctype> // for converting variables 
#include <vector> 
#include <typeinfo> // to get the type of variable typeid(variable).name()
using namespace std;


int main(){
    
    // ofstream     Creates and writes to files
    // ifstream     Reads from files
    // fstream      A combination of ofstream and ifstream: creates, reads, and writes to files

    string line;
    string digits ="";
    vector<int> numbers = {}; // a vector like list in python which you can append to it; need <vector> header
    int n;
    string first_digit, second_digit;
    double sum = 0;

    // read a file 
    ifstream myfile ("text.txt");
    if (myfile.is_open()){
        while (getline (myfile, line)){
            digits = "";
            // how to loop in string 
            for (char c:line){
                if (isdigit(c)){
                    digits.push_back(c);
                }
            }
            
            if (digits.size() == 0){
                numbers.push_back(digits.size());
            }
            else if (digits.size() == 1){ // **
                numbers.push_back(stoi(digits) * 11); // convert from string to int 
            }
            else {
                first_digit = digits[0];
                second_digit = digits[digits.size() - 1];
                numbers.push_back(stoi(first_digit + second_digit)); // **
            }
        }
        myfile.close();
    }

    else cout << "Unable to open the file";
    
    for (int i=0; i<numbers.size(); ++i) {
        sum += numbers[i];
    }

    cout << "sum of all data is: " << sum <<endl;
    return 0;
}