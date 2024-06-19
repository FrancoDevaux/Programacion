
#include <iostream>

using namespace std;

int main(){

    //Declaramos la MATRIZ
    const int n = 6;
    int matriz[n][n];

    //Cargamos la MATRIZ
    for (int filas = 0; filas < n; filas++){
        for (int columnas = 0; columnas < n; columnas++){
            cout << "\nIngrese un valor: ";
            cin >> matriz[filas][columnas];
        }
    }

    //Mostrar MATRIZ
    for (int filas = 0; filas < n; filas++){
        for (int columnas = 0; columnas < n; columnas++){
            cout << matriz[filas][columnas] << "\t";
        }
        cout << endl;
    }   



    for (int filas = 0; filas < n; filas++){
        if (filas %2 == 0)
        {
            for (int columnas = 0; columnas < n; columnas++){
                cout << matriz[filas][columnas] << "\t";
            }
        }
        else
        {
            for (int columnas = n-1; columnas >= 0; columnas--){
                cout << matriz[filas][columnas] << "\t";
            }
        }
        cout << endl;
    }
    


}