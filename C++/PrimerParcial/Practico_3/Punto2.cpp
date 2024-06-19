#include <iostream>

using namespace std;

int main(){

    int numero1, numero2, numero3;
    cout << "Ingrese el primer numero: ";
    cin >> numero1;
    cout << "Ingrese el segundo numero: ";
    cin >> numero2;
    cout << "Ingrese el tercer numero: ";
    cin >> numero3;

    int max = numero1;

    if (numero2 > max) {
        max = numero2;
    }
    if (numero3 > max) {
        max = numero3;
    }
    
    cout << "El numero mas grande es: " << max << endl;

    return 0;
}


