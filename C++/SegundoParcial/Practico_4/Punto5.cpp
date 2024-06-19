#include <iostream>
#include <string>

using namespace std;

int main(){

    string palabra;

    cout << "\nIngrese una palabra: ";
    cin >> palabra;

    int i = 0;
    while (i < palabra.length())
    {
        cout << palabra[i] << " \n";
        i++;
    }

    return 0;


}