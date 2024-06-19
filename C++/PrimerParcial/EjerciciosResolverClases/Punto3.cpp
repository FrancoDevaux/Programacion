#include <iostream>
#include <string>

using namespace std;

int main(){

    string palabra1, palabra2;
    int caracter1, caracter2;

    cout << "\nIngrese una palabra: ";
    cin >> palabra1;
    cout << "Ingrese otra palabra: ";
    cin >> palabra2;


    caracter1 = palabra1.length();
    caracter2 = palabra2.length();

   if (caracter1 > caracter2)
   {
        cout << "\nLa palabra " << palabra1 << " tiene mas letras que la palabra " << palabra2 << endl;
        cout << palabra1 << " tiene " << caracter1 << " letras" << " y " << palabra2 << " tiene " << caracter2 << endl;
   }
   else
   {
        cout << "\nLa palabra " << palabra2 << " tiene mas letras que la palabra " << palabra1 << endl;
        cout << palabra2 << " tiene: " << caracter2 << " letras" << " y " << palabra1 << " tiene: " << caracter1 << endl;
   }

    return 0;

}