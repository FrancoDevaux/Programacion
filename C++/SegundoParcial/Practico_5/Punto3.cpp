#include <iostream>
#include <cstdlib>
#include <ctime>

using namespace std;

int main(){

    srand(time(NULL));

    int numeros[8];

    for (int i = 0; i < 8; i++){
        numeros[i] = rand() % 10 + 1;  //generamos numeros randoms del 1 al 10
    }

    cout << "\nArreglo generado: ";
    for (int i = 0; i < 8; i++){
        cout << numeros[i] << " ";
    }
    cout << endl;


    int maximo = numeros[0];
    int minimo = numeros[0];

    for (int i = 1; i < 8; i++){
        if (numeros[i] > maximo){
            maximo = numeros[i];
        }
        if (numeros[i] < minimo){
            minimo = numeros[i];
        }
    }

    //Mostrar el maximo y minimo
    cout << "Valor maximo: " << maximo << endl;
    cout << "Valor minimo: " << minimo << endl;

    //Contar repeticiones
    int repetciones[10] = {0};  //Arreglo para contar repeticiones de cada numero del 1 al 10

    for (int i = 0; i < 8; i++){
        repetciones[numeros[i] - 1] ++;   //Incrementar contador para el numero correpsondiente
    }

    cout << "\nRepetciones de cada numero: "<< endl;
    for (int i=0; i < 10; i++){
        cout << "Numero " << i + 1 << ": " << repetciones[i] << " veces"  << "\n" << endl;
    }

    return 0;
}