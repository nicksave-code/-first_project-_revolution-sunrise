#include <iostream>
using std::string;

class Box {
public:
    string Space;
    string Name;
    string Company;
    int Age;
    string Birthday;

    void Inf(){
        std::cout << "Name - " << Name << std::endl;
        std::cout << "Project - " << Company << std::endl;
        std::cout << "Age - " << Age << std::endl;
        std::cout << "Your birthday is - " << Birthday << std::endl;
        std::cout << "" << Space << std::endl;
    }
    Box(string naMe, string comPany, int aGe, string birthDay, string spAce) {
        Name = naMe;
        Company = comPany;
        Age = aGe;
        Birthday = birthDay;
        Space = spAce;
    }
};
int main()
{
    Box Box1 = Box("Nick", "Revolution Sunrise", 0x11, "july 24", "\n");
    /*Box1.Name = "Nick";
    Box1.Company = "Revolution Sunrise";
    Box1.Age = 0x1;
    Box1.Space = "\n";
    Box1.Birthday = "july 24";*/
    Box1.Inf();

    Box Box2 = Box("Dany", "Your Age", 0xff, "august 24", "\n");
    /*Box2.Name = "Sand";
    Box2.Company = "Your Sunrise is pretty";
    Box2.Age = 0x12;
    Box2.Birthday = "february 20";*/
    Box2.Inf();
}