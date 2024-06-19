/*Escribe una función que tome un arreglo de enteros y lo ordene de mayor a menor.
• Inserción. • Inserción con intercambios. • Selección directa. • Burbujeo. */


#include <iostream>
#include <cstdlib>
#include <ctime>
using namespace std;

void menu();
void mostrarArreglo(int array[], int n);
void inserccion(int array[], int n);
void inserccionIntercambios(int array[], int n);
void selccionDirecta(int array[], int n);
void burbujeo(int array[], int n);


int main(){

    //Numeros aletorios
    srand(time(NULL));
    int n = 10, array[n], opcion;
    for (int i = 0; i < n; i++){
        array[i] = rand() % 10;    //100 + 1;
        
    }


    mostrarArreglo(array, n);   //Mustra los numeros aleatorios que elegio
    menu();
    cin >> opcion;

    switch (opcion){
        case 1: 
            inserccion(array,n);
            break;
        case 2:
            inserccionIntercambios(array,n);
            break;
        case 3:
            selccionDirecta(array,n);
            break;
        case 4:
            burbujeo(array,n);
            break;

        default:
            cout << "\n[!]Opcion incorrecta." << endl;
    }
    mostrarArreglo(array,n);

}


void menu(){ //Los menus simpre van vacion en los parentesis
    cout << "\nEstos son los tipo de ordenamiento que hay\n";
    cout << "1 - Inserccion\n";
    cout << "2 - Insercion con intercambios\n";
    cout << "3 - Seleccion directa\n";
    cout << "4 - Burbujeo\n";
    cout << "5 - Salir del menu\n";
    cout << "Elija una opcion: ";
}

void mostrarArreglo(int array[], int n){
    for (int i = 0; i < n; i ++){
        cout << array[i] << "\t";
    }
    cout << endl;
}

void inserccion(int array[], int n){
    int posicion, auxiliar;
    for (int i = 0; i < n; i++){
        posicion = i;
        auxiliar = array[i];
        while ((posicion > 0) && (array[posicion - 1] > auxiliar)){  //De forma ASCENDENTE
            array[posicion] = array[posicion - 1];
            posicion --;
        }
        array[posicion] = auxiliar;
    }
}

void inserccionIntercambios(int array[], int n){
    int pos, tmp;
    for (int i = 0; i < n; i++){
        pos = i;
        while ((pos > 0) && (array[pos - 1] > array[pos])){ //Aca cambia de forma ASCENDENTE 
            tmp = array[pos];
            array[pos] = array[pos - 1];
            array[pos -1] = tmp;
            pos --;
        }
    }
}

void selccionDirecta(int array[], int n){
    int x, menor;
    for (int i = 0; i < n-1; i++){
        menor = array[i];
        x = i;
        for (int j = i; j < n; j++){
            if (array[j] < menor){ //Aca cambia de forma ASCENDENTE
                menor = array[j];
                x = j;
            }
        }
        array[x] = array[i];
        array[i] = menor;
    }
}


void burbujeo(int array[], int n){
    int temp;
    for (int i = 0; i < n-1; i++){ //Recorrer hasta que sea necesario y quede ordenado
        for (int j = 0; j < n-1; j++){ //Hacer el swap, el intercambio con el siguiente
            if (array[j] > array[j+1]){  //Aca cambia de forma ASCENDENTE 
                temp = array[j];
                array[j] = array[j+1];
                array[j+1] = temp;
            }
        }
    }
}
