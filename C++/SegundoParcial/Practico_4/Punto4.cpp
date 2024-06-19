#include <iostream>

using namespace std;

int main(){

    int numero;

    cout << "\nIngrese un numero: ";
    cin >> numero;
    cout << "Los divisores de " << numero << " son: " << endl;

    for (int i = 1; i <= numero; i++)
    {
        if (numero % i == 0) // Si el residuo es cero, significa que i es divisor de numero.
        {
            cout << i << " ";
        }
    }

    return 0;

}