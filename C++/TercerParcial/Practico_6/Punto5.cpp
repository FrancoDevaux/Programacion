//Crea una funcion que tome dos matrices cuadradas y almacene su suma en una tercera matriz.

#include <iostream>
#include <cstdlib>
#include <ctime>
using namespace std;

const int n = 2;
//PROTOTIPOS
void sumarMatrices(int mat1[n][n], int mat2[n][n], int matSuma[n][n]);
void mostrarMatriz(int matriz[n][n]);


int main(){
    int matriz1[n][n], matriz2[n][n], matrizResultado[n][n];

    srand(time(NULL));
    for (int i = 0; i < n; i++){
        for (int j = 0; j < n; j++){
            matriz1[i][j] = rand() % 10 + 1;
            matriz2[i][j] = rand() % 10 + 1;
        }
    }

    cout << "Matriz 1:\n";
    mostrarMatriz(matriz1);

    cout << "\nMatriz 2:\n";
    mostrarMatriz(matriz2);

    sumarMatrices(matriz1, matriz2, matrizResultado);  //LLamo a la funcion
    cout << "\nMatriz resultado:\n";
    mostrarMatriz(matrizResultado);

    return 0;

}


//FUNCIONES
void sumarMatrices(int mat1[n][n], int mat2[n][n], int matSuma[n][n]){
    for (int i = 0; i < n; i ++){
        for (int j = 0; j < n; j++){
            matSuma[i][j] = mat1[i][j] + mat2[i][j];
            
        }
    }
}


void mostrarMatriz(int matriz[n][n]){
    for (int i = 0; i < n; i++){
        for (int j = 0; j < n; j++){
            cout << matriz[i][j] << "\t";
        }
        cout << endl;
    }
}

