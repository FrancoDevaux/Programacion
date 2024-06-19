#include <iostream>
#include <cmath>
using namespace std;

int main(){

    int numero, cifras;

    cout << "\nIngrese un numero entero: ";
    cin >> numero;

    if (numero % 2 == 0){

        cout << "\nEl numero " << numero << " es PAR" << endl;

        cifras = trunc(log10(numero)) + 1;
        cout << "El numero ingresado: " << numero << " tiene ---> " << cifras << " cifras." << endl;
    }
    else{

        cout << "\nEl numero " << numero << " es IMPAR" << endl;

        cifras = abs(numero); // abs te devuelve el valor absoluto de un numero

        while (cifras >= 10) 
        {
            cifras /= 10;
        }

        cout << "\nLa primera cifra del numero ingresado: " << numero << " es ---> " << cifras;
    }



}
