#include <iostream>

using namespace std;

int main(){

    int numero, factorial = 1;

    cout << "\nIngrese un numero: ";
    cin >> numero;

    if (numero < 0)
    {
        cout << "\nNo se puede con numeros NEGATIVOS." << endl;
        return 1;
    }

    for (int i = 1; i <= numero; i++)
    {
        factorial = factorial * i;
    }

    cout << "\nEl factorial de " << numero << " es: " << factorial << endl;

    return 0;

}