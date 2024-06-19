/*Escribe un programa donde la cantidad de filas y columnas de la matriz estén definidas por
constantes distintas. Luego, completa los elementos de la matriz siguiendo estas reglas: si la
suma de los índices de un lugar es par, ese lugar se llenará con la raíz cuadrada de la suma de
los índices. En caso de que la suma de los índices sea impar, ese lugar se llenará con un valor
de 0.
*/

#include <iostream>
#include <cmath>

using namespace std;

int main(){

    const int fila = 3;
    const int columna = 3;

    float matriz[fila][columna];

    for (int i = 0; i < fila; i++){
        for (int j = 0; j < columna; j++){
            cout << "(" << i+1 << " " << j+1 << ")";
        }
        cout << endl;
    }

    for (int i = 0; i < fila; i++){
        for (int j = 0; j < columna; j++){
            if ((i+j) %2 == 0){
                matriz[i][j] = sqrt(i+j+2);  // +2 para que arranque en 1 los indices
            }
            else{
                matriz[i][j] = 0;
            }
        }
    }


    for (int i = 0; i < fila; i++){
        for (int j = 0; j < columna; j++){
            cout << matriz[i][j] << " ";
        }
        cout << endl;
    }

    return 0;


}