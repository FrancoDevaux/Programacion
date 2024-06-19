/*Cargar una matriz de NxM con valores aleatorios entre [1,100] y comprobar si existen valores
repetidos.
*/

#include <iostream>
#include <cstdlib>
#include <ctime>

using namespace std;

int main(){

    //Declaramos variables
    int filas, columnas;
    //Preguntar cantidad de filas y columns
    cout << "\nIngrese cantidad de filas: ";
    cin >> filas;
    cout << "\nIngrese cantidad de columnas: ";
    cin >> columnas;

    //Verificar que no ponga numeros menores q cero
    if (filas <= 0 || columnas <= 0){
        cout << "\n[!]Error: Dimensiones invalidas";
        return 1;
    }

    //Semilla numeros aleatrorios
    srand(time(NULL));

    //Declaramos e Inicilaizamos la MATRZ
    int matriz[filas][columnas];

    //Bandera para verificar si se encontro un numero repetido
    bool encontrado = false;
   
    //Cargar la MATRIZ y verficar si se repite
    for (int i = 0; i < filas; i++){
        for (int j = 0; j < columnas; j++){
            int valroAleatorio = rand() % 100 +1;
            encontrado = false;

            for (int i_aux = 0; i_aux < i; i_aux++){
                for (int j_aux = 0; j_aux < j; j_aux++){
                    if (matriz[i_aux][j_aux] == valroAleatorio){
                        encontrado = true;
                        break;  //Salir del bucle si lo encuentra
                    }
                }
                if (encontrado){
                    break; //Salir del bucle principal si lo encuntra
                }
            }
            if (encontrado){
                cout << "\nExisten valores repetidos ---> " << valroAleatorio << endl;
            }
            else{
                matriz[i][j] = valroAleatorio;
            }
            
        }
    }
   
    cout << "\n---------------Matriz------------------\n";
    for (int i = 0; i < filas; i++){
        for (int j = 0; j < columnas; j++){
            cout << matriz[i][j] << " ";
        }
        cout << endl;
    }
   
}