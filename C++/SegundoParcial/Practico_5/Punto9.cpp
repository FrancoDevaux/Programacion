/*Matriz y búsqueda.

a) Escribir un programa que complete una matriz de 10x10 con números aleatorios entre el
1 y el 100. Luego en un arreglo debe guardar el resultado de sumar cada una de las filas,
por lo tanto, va a tener 10 lugares. Mostrar el contenido del arreglo.

b) Debe permitir que el usuario ingrese un número y realizar la búsqueda de este en la matriz.
Si lo encuentra debe mostrar un mensaje que indique que lo encontró y la posición donde
está ubicado en la matriz. Si no lo encuentra que muestre un mensaje de que la búsqueda
finalizo sin éxito. Esto debe repetirse hasta que el usuario ingrese de alguna forma que
no quiere realizar más búsquedas.
*/

#include <iostream>
#include <cstdlib>
#include <ctime>

using namespace std;

int main(){

    //Declaramos las variables
    int matriz[10][10], arreglo[10], sumaFila = 0, num_i, num_j;
    int numero;

    //Busqueda de la MATRIZ
    bool encontrado = false;

    //Numero ALEATORIOS
    srand(time(NULL));


    //Cargamos la MATRIZ con numeros ALEATORIOS
    for (int i = 0; i < 10; i++){
        for (int j = 0; j < 10; j++){
            matriz[i][j] = rand() % 100 + 1;
        }
    }

    for (int i = 0; i < 10; i++){
        for (int j = 0; j < 10; j++){
            sumaFila += matriz[i][j];
        }
    }

    //Mostramos la MATRIZ
    cout << "\nMatriz 10x10 con numeros ALEATRIOS\n";
    for (int i = 0; i < 10; i++){
        for (int j = 0; j < 10; j++){
            cout << matriz[i][j] << " ";
        }
        cout << endl;
    }


    cout << "\nArreglo con el resultado de sumar cada una de las filas\n";
    for (int i = 0; i < 10; i++){
        cout << arreglo[i] << " ";
    }
    cout << endl;

    do {
        cout << "\nIngrese un numero distinto de 0: ";
        cin >> numero;

        if (numero == 0){
            cout << "\n[!] Error de programa";
            break;
        }

            for (int i = 0; i < 10; i++){
                for (int j = 0; j < 10; j++){
                    if (matriz[i][j] == numero){
                        encontrado = true;
                        num_i = i+1;
                        num_j = j+1;
                        break;
                    }
                    if (encontrado) break;
                }
                if (encontrado) break;
            }
        
        if (encontrado){
            cout << "\nEl numero " << numero << " se ecnuentra en la fila " << num_i << " columna " << num_j << endl;
            break;
        }
        else{
            cout <<"El numero " << numero << " NO se encontro.";
        }
    } while (true);

    return 0;
    
}