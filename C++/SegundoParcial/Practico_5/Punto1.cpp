#include <iostream>

using namespace std;

int main(){

    int numeros[10];

    for (int i = 0; i < 10; i++){
        cout << "\nIngrese el numero: " << i + 1 << ": ";
        cin >> numeros[i];
    }

    int suma = 0;
    for (int i = 0; i < 10; i++){
        suma += numeros[i];
    }

    cout << "\t\tLa suma de los numeros ingresados es: " << suma << endl;

    return 0;

}