#include <iostream>
#include <cmath>
using namespace std;

int main(){
    int numero, cifras;

    cout << "Ingrese un numero: ";
    cin >> numero;

    if (numero < 0){
        cout << "Por favor ingrese un numero POSITIVO: ";
        cin >> numero;
        
    }

    cifras = trunc(log10(numero)) + 1;

    cout << "El numero ingresado " << numero << " tiene ---> " << cifras << " cifras ";

    return 0;
}