#include <iostream>
#include <fstream> // need for file operations 
#include <string>
#include <cctype> // for converting variables 
#include <vector> 
#include <typeinfo> // to get the type of variable typeid(variable).name()
#include <map>

using namespace std;


map<string, char> words {
    {"one", '1'},
    {"two", '2'},
    {"three", '3'},
    {"four", '4'},
    {"five", '5'},
    {"six", '6'},
    {"seven", '7'},
    {"eight", '8'},
    {"nine", '9'}
    };

void first_problem(vector<string> &lines){
    int sum = 0;
    for (int i = 0; i < lines.size(); i++){
        string line = lines[i];
        vector<char> numbers;
        for (int j = 0; j < line.length(); j++){
            if (isdigit(line[j])){
                numbers.push_back(line[j]);
            }
        }
        string combined = "";
        combined += numbers[0];
        combined += numbers[numbers.size()-1];

        sum += stoi(combined);
    }
    cout << "======== Part One ========" << endl;
    cout << "The answer: " << sum << endl;
}

void second_problem(vector<string> &lines){
    int sum = 0;
    for (int i=0; i < lines.size();i++){
        string line = lines[i];
        vector<char> numbers;

        for (int k=0; k<line.length(); k++){
            if (isdigit(line[k])){
                numbers.push_back(line[k]);
            }
            for (int j=1; j < line.length(); j++){
                string sub = line.substr(k, j); // string substr (size_t pos, size_t len)
                map<string, char>::iterator map_iterator = words.find(sub);
                
                if (map_iterator != words.end()){
                    numbers.push_back(map_iterator->second);
                    break;
                }
            }
        }
        string combined = "";
        combined += numbers[0];
        combined += numbers[numbers.size()-1];

        sum += stoi(combined);
    }
    cout << "======== Part Two ========" << endl;
    cout << "The answer: " << sum << endl;
}
int main()
{
    
    // ofstream     Creates and writes to files
    // ifstream     Reads from files
    // fstream      A combination of ofstream and ifstream: creates, reads, and writes to files

    // read a file 
    ifstream my_file;

    my_file.open("input.txt");
    if (!my_file.is_open()){
        cout << "Unable to open the file" << endl;
        return 1;
    }

    string line;
    vector<string> lines;

    while (getline (my_file, line)){
        if (line.empty()){
            break;
        }
        lines.push_back(line);
    }

    first_problem(lines);
    second_problem(lines);
    

    return 0;
}