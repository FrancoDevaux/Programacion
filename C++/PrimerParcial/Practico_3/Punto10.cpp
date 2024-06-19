#include <iostream>
#include <cmath>

using namespace std;

int main(){

    int respuesta;
    double numero1, numero2;


    cout << "\nEstas son las siguintes operaciones: "; 
    cout << "\n1 ---> SUMA \n2 ---> RESTA \n3 ---> MULTIPLICACION \n4 ---> DIVISION ";
    cout << "\n\nElija una operacion con el numero asignado: ";
    cin >> respuesta;

    if (respuesta > 4){
        cout << "Ingresaste un numero sin ASIGNACION!";
        return 0;
    }

    cout << "Ahora elija el PRIMER numero: ";
    cin >> numero1;
    cout << "Ahora elija el SEGUNDO numero: ";
    cin >> numero2;

    switch (respuesta){
        
        case 1:
            cout << "La suma de los numeros " << numero1 << " + "<< numero2 << " es ---> " << numero1 + numero2;
            break;

        case 2:
            cout << "La resta de los numeros " << numero1 << " - "<< numero2 << " es ---> " << numero1 - numero2;
            break;

        case 3:
            cout << "La multiplicacion de los numeros " << numero1 << " * "<< numero2 << " es ---> " << numero1 * numero2;
            break;

        case 4:
            cout << "La division de los numeros " << numero1 << " / "<< numero2 << " es ---> " << numero1 / numero2;
            break;

        default:
            cout << "Ingresaste otra ves un numero sin asignacion HACKER";

        return 0;


    }

}