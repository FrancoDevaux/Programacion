/*Escribir un programa que complete una matriz de 10x10 con el número 1 para los índices que
se encuentren por encima de la diagonal principal y con 0 los que estén por debajo. Los
valores de la diagonal principal deben ir en forma descendente desde el 10 hasta el 1.*/

#include <iostream>

using namespace std;

int main(){

    //Declaramos la MATRIZ
    int matriz[10][10];

    //Cragar la MATRIZ
    for (int i = 0; i < 10; i++){
        for (int j = 0; j < 10; j++){
            if (i > j){
                matriz[i][j] = 0;   //Por debajo de la diagonal
            }
            else if (i < j){
                matriz[i][j] = 1;   //Por encima de la diagonal
            }
            else{
                matriz[i][j] = 10 -i;  //Valor descendente desde 10 hasta 1
            }
        }
    }


    //Mostar la MATRIZ
    for (int i = 0; i < 10; i++){
        for (int j = 0; j < 10; j++){
            cout << matriz[i][j] << " ";
        }
        cout << endl;
    }

    return 0;

}