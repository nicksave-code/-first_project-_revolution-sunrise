#include<iostream>
using std::string;
using std::cout;
using std::cin;
using std::endl;

int main() {

        string input_Password;
        string Password = "PeachMind2407";
        
        cout << "Hello father, type our password\n" << endl;
        cin >> input_Password;

        while (input_Password != Password) {
                cout << "Oh, a wrong" << endl;
                cin >> input_Password;
        }

        cout << "\nHi human!" << endl;
        cout <<"Hagamos un plan para hoy..." << endl;
        return 0;
}