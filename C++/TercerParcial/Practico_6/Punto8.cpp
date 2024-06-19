/*
Escribe una función llamada "intercambiar" que reciba dos variables de tipo string y las
intercambie entre sí.
*/

#include <iostream>
#include <string>
using namespace std;

//PROTOTIPO
void Intercambiar(string &string1, string &string2);


//MAIN
int main(){

    string string1, string2;

    cout << "\nIngrese palabra 1: ";
    cin >> string1;
    cout << "Ingrese palabra 2: ";
    cin >> string2;

    Intercambiar(string1, string2);
    cout << "\n-----------Cambie Palabra 1 por Palabra 2---------------";
    cout << "\nAhora palabra 1 es ---> " << string1 << endl;
    cout << "Ahora palabra 2 es ---> " << string2 << endl;

}

//FUNCION
void Intercambiar(string &string1, string &string2){
    string temp = string1;
    string1 = string2;
    string2 = temp;
}

