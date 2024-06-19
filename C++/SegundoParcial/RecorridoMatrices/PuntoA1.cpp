/*---------------------------ESTRATEGIA-------------------------
n = 6;
INICIO: Varia columnas, desde n-1(6), hasta 0, columnas-- (porque la figura esta en forma descendente)
TRAMO 1: Varia filas, desde 0, hasta filas < n, filas++ (porque lo hace de forma ascendente)*/


#include <iostream>

using namespace std;

int main(){

    const int n = 6;
    int matriz[n][n];

    //CARGAR matriz
    for (int i = 0; i < n; i++){
        for (int j = 0; i < n; j++){
            matriz[i][j] = i *10 + j;  //Sirve para LLENAR una matriz
        }
    }

    //MOSTAR matriz
    for (int columna = n - 1; columna > -1; columna--){
        for (int fila = 0; fila < n; fila++){
            cout << matriz[fila][columna] << "\t";
        }
        cout << endl;
    }

    return 0;

}