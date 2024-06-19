/*Escribe un programa que genere un arreglo de 8 lugares y lo llene con números aleatorios.
Luego, crea otro arreglo del mismo tamaño y llena este segundo arreglo con los valores del
primero, pero en orden inverso. Finalmente, muestra ambos arreglos en pantalla.*/

#include <iostream>
#include <cstdlib>
#include <ctime>

using namespace std;

int main(){

    //VARIABLES
    int arreglo1[8];
    int arreglo2[8];

    //SEMILLA
    srand(time(NULL));

    //NUMERO ALEATORIOS del 1 al 10
    for (int i = 0; i < 8; i++){
        arreglo1[i] = rand() % 10 + 1;
    }

    int b = 7;
    for (int i = 0; i < 8; i++){
        arreglo2[i] = arreglo1[b];
        b--;
    }

    cout << "\nArrgelo original" << endl;
    for (int i = 0; i < 8; i++){
        cout << arreglo1[i] << " ";
    }
    cout << endl;

    cout << "\nArreglo invertido" << endl;
    for (int i = 0; i < 8; i++){
        cout << arreglo2[i] << " ";
    }
    cout << endl;

    return 0;
}