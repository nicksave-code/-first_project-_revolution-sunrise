#include <iostream>
#include <cstdlib>
#include <Windows.h>
using namespace std;

int main()
{
    std::string test = u8"Hola Sandra\n";
       SetConsoleOutputCP(CP_UTF8);
       std::cout << test;
    system("pause");
    return 0;
}