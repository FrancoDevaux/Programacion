/* Escribir un programa que le permita al usuario ingresar la diagonal principal de una matriz
de 5x5 y que los otros lugares se completen con una X.*/

#include <iostream>

using namespace std;

int main(){

    int matriz[5][5]; 
    
    //Cargamos la MATRIZ con un condicional 
    for (int i = 0; i < 5; i++){
        for (int j = 0; j < 5; j++){
            if (i == j){
                cout << "\nIngrese numero para la matriz diagonal: ";
                cin >> matriz[i][j];
            }
        }
    }


    //Mostramos la MATRIZ
    for (int i = 0; i < 5; i++){
        for (int j = 0; j < 5; j++){
            if (i == j)
            {
                cout << matriz[i][j] << " ";
            }
            else
            {
                cout << "X "; 
            }
        }
        cout << endl;
    }

    return 0;

}