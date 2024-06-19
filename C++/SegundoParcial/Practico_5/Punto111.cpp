/*Escribe un programa donde la cantidad de filas y columnas de la matriz estén definidas por
constantes distintas. Luego, completa los elementos de la matriz siguiendo estas reglas: si la
suma de los índices de un lugar es par, ese lugar se llenará con la raíz cuadrada de la suma de
los índices. En caso de que la suma de los índices sea impar, ese lugar se llenará con un valor
de 0.
*/

#include <iostream>
#include <cmath>

using namespace std;

int main(){

    //Decalarmos VARIABLES
    const int fila = 5;
    const int columna = 4;

    //Declaramos MATRIZ
    int matriz[fila][columna];

    //Cargar la MATRIZ
    for (int i = 0; i < fila; i++){
        for (int j = 0; j < columna; j++){
            int suma_indices = i+j;

            if (suma_indices %2 == 0){
                matriz[i][j] = sqrt(suma_indices);
            }
            else{
                matriz[i][j] = 0;
            }
        }
    }


    //Mostrar MATRIZ
    for (int i = 0; i < fila; i++){
        for (int j = 0; j < columna; j++){
            cout << matriz[i][j] << " ";
        }
        cout << endl;
    }

    return 0;

}