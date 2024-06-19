/* -------------------------------------ESTRATEGIA------------------------------------------
n = 6;
INICIO: Varia filaInicio, desde n-1 hasta filaInicio > -1, filaInicio--
TRAMO 1: Varia columna, desde n-1 hasta columna >= n - filaInicio, columna--
TRAMO 2: Varia fila, desde FilaInicio hasta fila > -1; fila --
*/

#include <iostream>

using namespace std;

int main(){

    const int n = 6;
    int matriz[n][n];

    //LLenar la matriz
    for (int i = 0; i < n; i++){
        for (int j = 0; j < n; j++){
            cout << "\nIngrese un valor: ";
            cin >> matriz[i][j];
        }
    }

    //Mostrar matriz en forma matricial
    for (int fila = 0; fila < n; fila++){
        for (int columna = 0; columna < n; columna++){
            cout << matriz[fila][columna] << "\t";
        }
        cout << endl;
    }
    cout << endl;

    // Matriz matrical y el recorrido indicado
    for (int FilaInicio = n-1; FilaInicio > -1; FilaInicio--){
        //TRAMO 1
        for (int col = n-1; col >= n-FilaInicio; col--){
            cout << matriz[FilaInicio][col] << "\t";
        }
        //TRAMO 2
        for (int fila = FilaInicio; fila > -1; fila--){
            cout << matriz[fila][n-FilaInicio] << "\t";
        }
        cout << endl;
    }
    return 0;
}