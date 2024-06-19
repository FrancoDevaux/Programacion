//Punto 2.a)

/*Tenes este arreglo-->(5, 53, 900, 54, 306, 2, 99)
. Ordenalo de forma DESCENDNETE con el metodo de Ordenacion Inserseccion*/

#include <iostream>
using namespace std;


int main(){

    int n = 7;
    int array[] = {5, 53, 900, 54, 306, 2, 99};
    
    int pos;
    int aux;

    //Recorrer el arreglo
    for (int i = 0; i < n; i++){
        pos = i;  //Almacena la posicion
        aux = array[i];  //Almacena el valor

        while ((pos > 0) && (array[pos - 1] < aux)){  //Aca se cambia si queres ASCENDENTE >
            array[pos] = array[pos - 1];
            pos--;
        }
        array[pos] = aux;

    }

    cout << "\nArreglo Ordenado forma Descendente: ";
    for (int j = 0; j < n; j++){
        cout << array[j] << " ";
    }

}



