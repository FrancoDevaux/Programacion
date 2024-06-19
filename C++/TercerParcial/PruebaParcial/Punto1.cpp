/*Implementando subprogramas que devulevan un resultado y errors que impidan realizar calculos,
Escribir un programa que permita determinar su un numero es primo, el usuario debera tener la posibilidad de ingresar 
por teclado el numero.

Numero Primos: Aquellos que son disivisible entre ellos mismo y el 1.
*/

#include <iostream>
using namespace std;

bool esPrimo(int numero) {
    /*if (numero <= 1) {
        return false; //1 y los números menores que 1 no son primos.
    }*/ //No hace falta si hice el if despues

    for (int i = 2; i <= numero / 2; i++){
        if (numero % i == 0){
        return false;
        }
    }
    return true;
}


int main() {
    int numero;

    do{
        
        cout << "\nIngrese un numero: ";
        cin >> numero;

        if (numero < 0){
            cout << "\nIngresaste un numero negativo, vuelve a ingresar";
        }
    }while(numero < 0);

    bool es_primo = esPrimo(numero);

    if (es_primo){
        cout << "\nEl numero -> " << numero << " \n[+]Si es un numero primo." << endl;
    } else{
        cout << "\nEl numero -> " << numero << " \n[!]No es un numero primo." << endl;
    }

    return 0;
}

