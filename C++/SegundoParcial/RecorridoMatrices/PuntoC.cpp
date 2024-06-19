/*----------------------ESTRATEGIA---------------------------------------
n = 6;
INICIO: Varia columnaInicio, desde 0 hasta columnaInicio < n, columnaInicio++
TRAMO 1: Varia fila, desde n -1 hasta  n/2 -1 -columnaInicio, fila--
TRAMO 2: Varia columna, desde  columnaInicio -1 hasta columna >= 0, columna--
TRAMO 3: Varia fila, desde 0 hasta n -1 - (columnaInicio -3), fila++
TRAMO 4: Varia columna, desde columnaInicio +1 hasta columna < n, columna++
*/

#include <iostream>

using namespace std;

int main(){

    const int n = 6;
    int matriz[n][n];

    //CARGAR/LLENAR matriz
    for (int i = 0; i < n; i++){
        for (int j = 0; i < n; j++){
            matriz[i][j] = i *10 + j;  //Sirve para LLENAR una matriz
        }
    }

    //MOSTRAR la matriz
    for (int columnaInicio = 0; columnaInicio < n; columnaInicio++){
        if (columnaInicio < n/2)
        {   
            //tramo 1
            for (int fila = n -1; fila >= (n/2 -1 -columnaInicio); fila--){
                cout << matriz[fila][columnaInicio] << "\t";
            }
            //tramo 2
            for (int columna = columnaInicio -1; columna >= 0; columna--){
                cout << matriz[n/2 -1 -columnaInicio][columna] << "\t";
            }
        }
        else
        {
            //tramo 3
            for (int fila = 0; fila <= n -1 - (columnaInicio -3); fila++){
                cout << matriz[fila][columnaInicio] << "\t";
            }
            //tramo 4
            for (int columna = columnaInicio +1; columna < n; columna ++){
                cout << matriz[n -1 - (columnaInicio -3)][columna] << "\t";
            }
        }
        cout << endl;
    }

    return 0;

}