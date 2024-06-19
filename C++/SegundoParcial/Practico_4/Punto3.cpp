#include <iostream>

using namespace std;

int main(){

    int numero, suma = 0;

    cout << "\nIngrese un numero: ";
    cin >> numero;
    cout << "A continuacion se mostrara la SUMA los primeros numeros naturales de --> " << numero << endl;


    int i = 1;
    while (i <= numero)
    {
        suma +=i;  // Se suma el valor actual de i a la variable suma
        i++;  // Se incrementa el valor i en 1
    }

    cout << "La suma de los primeros numeros naturales es: " << suma << endl;

    return 0;

}