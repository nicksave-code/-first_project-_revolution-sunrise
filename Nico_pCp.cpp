#include <iostream>
using namespace std;
using std::string;

int main() {
    char ch = 'n';
    int myAge = 0x11;
    bool value = true;
    string name = "Sand";
    // Printing the corresponding ASCII of a character 
    // Notice the use of int() to get an integer
    cout << "ASCII value = " << int(ch) << endl;
    cout << "My age is: " << myAge << "\nValue is: " << value << endl;
    cout << "Hello " << name << endl;
    return 0;
}