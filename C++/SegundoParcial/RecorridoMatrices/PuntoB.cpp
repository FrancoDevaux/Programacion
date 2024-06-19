/*------------------------ESTRATEGIA---------------------------
Los TRAMOS son las direcciones y en este caso tiene 2
n = 6;
INICIO: Varia fila, desde 0 a n-1 (fila < n), fla++
TRAMO 1: Varia columna, desde  0 a n-1(columna < n), columna++
TRAMO 2: Varia columna, desde n-1 hasta 0(columna > -1), columna-- (porque va de derecha hacia izquierda)
DATO: Si es par hacer tramo 1 sino si es impar hacer tramo 2
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

    //MOSTAR la matriz
    for (int fila = 0; fila < n; fila++){
        if (fila %2 == 0){
            for (int columna = 0; columna < n; columna++){
                cout << matriz[fila][columna] << "\t";
            }
        }
        else{
            for (int columna = n -1; columna > -1; columna--){
                cout << matriz[fila][columna] << "\t";
            }
        }
        cout << endl;
    }

    return 0;
}