#include <iostream>
#include <cmath>
using namespace std;

int main(){
    float Nota1, Nota2, Nota3, promedio;

    cout << "Ingrese la nota del primer parcial: ";
    cin >> Nota1;
    cout << "Ingrese la nota del segundo parcial: ";
    cin >> Nota2;
    cout << "Ingrese la nota del tercer parcial: ";
    cin >> Nota3;

    promedio = ((Nota1 + Nota2 + Nota3) /3);
    promedio = round(promedio);
    promedio = trunc(promedio);

    cout << "El promedio final es de ---> " << promedio;

    return 0;
}