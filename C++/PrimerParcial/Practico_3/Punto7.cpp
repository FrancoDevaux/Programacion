#include <iostream>
#include <cmath>

using namespace std;

int main (){

    double nota1, nota2, nota3, promedio;

    cout << "Ingrese la nota del primer parcial: ";
    cin >> nota1;
    cout << "Ingrese la nota del segundo parcial: ";
    cin >> nota2;
    cout << "Ingrese la nota del tercer parcial: ";
    cin >> nota3;

    promedio = (nota1 + nota2 + nota3) / 3;

    if (promedio < 6)
    {
        cout << "Tu promedio es de: " << promedio << " por lo tanto estas DESAPROBADO";
    }
    else
    {
        cout << "Tu promedio es de: " << promedio << " por lo tanto estas APROBADO!";
    }

    return 0;

}