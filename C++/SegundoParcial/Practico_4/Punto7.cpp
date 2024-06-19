#include <iostream>

using namespace std;

int main(){

    int numero;

    cout << "\nIngrese un numero: ";
    cin >> numero;

    while (numero % 2 == 0)
    {
        cout << "El numero " << numero << " es PRIMO." << endl;
        return 0;
    }

    cout << "El numero " << numero << " NO es primo." << endl;

    return 0;



}