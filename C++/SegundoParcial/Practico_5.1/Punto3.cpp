#include <iostream>
#include <cstdlib>
#include <ctime>

using namespace std;

int main(){

    //VARIABLES
    const int n = 6;
    int matriz[n][n];

    //Numeros RANDOMS
    srand(time(NULL));

    //Cargar la MATRIZ
    for (int i = 0; i < n; i++){
        for (int j = 0; j < n; j++){
            matriz[i][j] = rand() % 65 + 53;
        }
    }

    //Mostrar la MATRIZ
    for (int i = 0; i < n; i++){
        for (int j = 0; j < n; j++){
            cout << matriz[i][j] << "\t";
        }
        cout << endl;
    }


    for (int i = 0; i < n; i++){
        if (i < n/2)
        {
            for (int fila = n-1; fila >= (n/2)-1-i; fila++){
                cout << matriz[fila][i] << "\t";
            }
            for (int columna = i-1; columna > -1;  ){
                cout << matriz[n/2 -1 -i][columna] << "\t";
            }
        }
        else
        {
            for (int fila = 0; fila <= n-1-i-3; fila++){
                cout << matriz[fila][i] << "\t";
            }
            for (int columna = i+1; columna < n; columna++){
                cout << matriz[n-4-i][columna] << "\t";
            }
        }
        cout << endl;
    }

    return 0;

}