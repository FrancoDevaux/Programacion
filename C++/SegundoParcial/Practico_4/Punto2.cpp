#include <iostream>

using namespace std;

int main(){

    int numero;

    cout << "\nIngrese un numero: ";
    cin >> numero;
    cout << "A continuacion se va a mostrar su tabla de multiplicar." << endl;

    for (int contador = 1; contador <= 10; contador++)
    {
        cout << numero << " x " << contador << " = " << numero*contador << endl;
    }
        
    return 0;

}