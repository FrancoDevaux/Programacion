#include <iostream>
#include <cmath>
using namespace std;

int main (){
    int numero;

    cout << "Ingrese un numero: ";
    cin >> numero;

    if (numero % 2 == 0)
    {
        cout << "El numero es PAR";
    }

    else
    {
        cout << "El numero es IMPAR";
    }

    return 0;
}