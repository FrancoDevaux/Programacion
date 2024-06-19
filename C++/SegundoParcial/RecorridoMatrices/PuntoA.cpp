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


    //MOSTRAR la matriz
    for (int fila = 0; fila < n; fila++){
        for (int columna = 0; columna < n; columna++){
            cout << matriz[fila][columna] << "\t";
        }
        cout << endl;
    }

    cout << endl << endl;

//------------------------------------------------------------------------------------------------------------------------

    //Recorrido matriz
    for (int columna = n - 1; columna > -1; columna--){
        for (int fila = 0; fila < n; fila++){
            cout << matriz[fila][columna] << "\t";
        }
        cout << endl;
    }

    return 0;

}

    