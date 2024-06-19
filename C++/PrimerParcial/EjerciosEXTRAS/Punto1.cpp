#include <iostream>

using namespace std;

int main(){

    int numero1, numero2;

    cout << "\nIngrese el primer numero: ";
    cin >> numero1;
    cout << "Ingrese el segundo numero: ";
    cin >> numero2;

    if (numero1 > numero2 ){

        cout << "Los numeros son: " << numero2 << " y " << numero1 << endl;
    }
    else {
        cout << "Los numeros son: " << numero1 << " y " << numero2 << endl;
    }

    return 0;
}