/*Desarrolla un programa que genere dos arreglos de tamaño 5 y los llene con números
aleatorios entre 3 y 57. Luego, crea un tercer arreglo del mismo tamaño donde cada elemento
sea la suma de los elementos correspondientes de los dos primeros arreglos.*/

#include <iostream>
#include <cstdlib>
#include <ctime>

using namespace std;

int main(){

    //VARIABLES
    int arreglo1[5];
    int arreglo2[5];
    int arreglo3[5];

    //NUMEROS ALEATORIOS
    srand(time(NULL));

    //CARGAMOS EL ARREGLO 1 Y 2 CON NUMERO ALEATORIOS
    for (int i = 0; i < 5; i++){
        arreglo1[i] = rand() % 55 + 3;
        arreglo2[i] = rand() % 55 + 3;
    }

    //LA ARREGLO 3 VA A SEGUIR IGUAL AL ARREGLO1 + ARREGLO2
    for (int i = 0; i < 5; i++){
        arreglo3[i] = arreglo1[i] + arreglo2[i];
    }


    //MOSTRAMOS ARREGLO 1
    for (int i = 0; i < 5; i++){
        cout << arreglo1[i] << " ";
    }
    cout << endl;

    //MOSTRAMOS ARREGLO 2
    for (int i = 0; i < 5; i++){
        cout << arreglo2[i] << " ";
    }
    cout << endl;

    //MOSTRAMOS ARREGLO 3
    for (int i = 0; i < 5; i++){
        cout << arreglo3[i] << " ";
    }
    cout << endl;

    return 0;

}