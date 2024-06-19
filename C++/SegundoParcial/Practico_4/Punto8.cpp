#include <iostream>

using namespace std;

int main(){

    int cantidad_numeros, numero;
    double media, suma = 0;

    cout << "\nIngrese la cantidad de numeros que va a ingresar: ";
    cin >> cantidad_numeros;


    int i = 1;
    do{
        cout << "Ingrese el numero " << i << ": ";
        cin >> numero;

        suma += numero;
        i++;
    } while (i <= cantidad_numeros);

    media = suma / cantidad_numeros;

    cout << "La media de los numeros ingresados es ---> " << media << "\n"<< endl;

    return 0;



}