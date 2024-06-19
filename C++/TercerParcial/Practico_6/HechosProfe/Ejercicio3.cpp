#include <iostream>
using namespace std;

//---------------Prototipos de funciones--------------------------------------
void mostrar(int arr[], int cant); // Función para mostrar los elementos de un arreglo
void ordenarInsercion(int arr[], int cant); // Función para ordenar los elementos de un arreglo utilizando el método de inserción
void ordenarInsercionIntercambio(int arr[], int cant); // Función para ordenar los elementos de un arreglo utilizando el método de inserción con intercambios
void ordenarSeleccionDirecta(int arr[], int cant); // Función para ordenar los elementos de un arreglo utilizando el método de selección directa
void ordenarBurbujeo(int arr[], int cant); // Función para ordenar los elementos de un arreglo utilizando el método de burbujeo

//---------------Función principal-------------------------------------------
int main(){
    const int tam = 5; // Tamaño del arreglo
    int arreglo[tam] = {5, 2, 1, 3, 4}; // Inicialización del arreglo con elementos desordenados
   
    mostrar(arreglo, tam); // Mostrar el arreglo antes de ordenar
    //ordenarInsercion(arreglo, tam); // Ordenar el arreglo usando el método de inserción
    //ordenarInsercionIntercambio(arreglo, tam); // Ordenar el arreglo usando el método de inserción con intercambios
    //ordenarSeleccionDirecta(arreglo, tam); // Ordenar el arreglo usando el método de selección directa
    ordenarBurbujeo(arreglo, tam); // Ordenar el arreglo usando el método de burbujeo
    mostrar(arreglo, tam); // Mostrar el arreglo después de ordenar

    return 0; // Fin del programa
}

//-------------Función para mostrar los elementos de un arreglo---------------------
void mostrar(int arr[], int cant){
    cout << "Mostrando...\n"; // Mensaje para indicar que se va a mostrar el arreglo
    for(int i = 0; i < cant; i++){
        cout << arr[i] << "\t"; // Mostrar cada elemento del arreglo
    }
    cout << endl; // Salto de línea al final de la impresión
}

//---Función para ordenar los elementos de un arreglo utilizando el método de inserción-----
void ordenarInsercion(int arr[], int cant){
    cout << "Ordenación por inserción...\n"; // Mensaje para indicar que se va a ordenar el arreglo
    int pos, aux;
    for(int i = 0; i < cant; i++){
        pos = i; // Guardar la posición actual
        aux = arr[i]; // Guardar el valor actual
        // Mover los elementos mayores a la derecha para hacer espacio para el elemento actual
        while((pos > 0) && (arr[pos - 1] > aux)){ 
            arr[pos] = arr[pos - 1]; // Mover el elemento a la derecha
            pos--; // Mover la posición hacia la izquierda
        }
        arr[pos] = aux; // Insertar el elemento en su posición correcta
    }
}

//---Función para ordenar los elementos de un arreglo utilizando el método de inserción con intercambios-----
void ordenarInsercionIntercambio(int arr[], int cant){
    cout << "Ordenando por inserción con intercambios...\n"; // Mensaje para indicar que se va a ordenar el arreglo
    int pos, temp;
    for (int i = 0; i < cant; i++){ // Recorrer todos los elementos del arreglo
        pos = i; // Guardar la posición actual
        // Mover los elementos mayores a la derecha mediante intercambios para hacer espacio para el elemento actual
        while((pos > 0) && (arr[pos - 1] > arr[pos])){ 
            temp = arr[pos]; // Guardar el valor del elemento actual
            arr[pos] = arr[pos - 1]; // Mover el elemento a la derecha
            arr[pos - 1] = temp; // Colocar el elemento guardado en la posición correcta
            pos--; // Mover la posición hacia la izquierda
        }
    } 
}

//---Función para ordenar los elementos de un arreglo utilizando el método de selección directa-----
void ordenarSeleccionDirecta(int arr[], int cant){
    cout << "Ordenando por selección directa...\n"; // Mensaje para indicar que se va a ordenar el arreglo
    for (int i = 0; i < cant - 1; i++){ // Bucle externo: recorre todos los elementos del arreglo excepto el último
        int mayor = i; // Inicializar la posición del mayor elemento con la posición actual
        for(int j = i + 1; j < cant; j++){ // Bucle interno: recorre los elementos restantes del arreglo
            if(arr[j] > arr[mayor]){ // Encontrar la posición del mayor elemento en el resto del arreglo
                mayor = j;
            }
        }
        // Intercambiar el elemento actual con el mayor elemento encontrado
        if(mayor != i){//En la teoría dice >1 y también está bien, solo queremos saber si mayor no es igual a i 
            int temp; // Variable temporal para realizar el intercambio
            temp = arr[i]; // Guardar el valor del elemento actual
            arr[i] = arr[mayor]; // Colocar el mayor elemento en la posición actual
            arr[mayor] = temp; // Colocar el elemento actual en la posición del mayor elemento
        }
    } 
}

//---Función para ordenar los elementos de un arreglo utilizando el método de burbujeo-----
void ordenarBurbujeo(int arr[], int cant){
    cout << "Ordenando por burbujeo...\n"; // Mensaje para indicar que se va a ordenar el arreglo
    bool intercambio = true; // Variable para controlar si se realizó algún intercambio en la pasada actual
    int i = 0; // Inicialización del contador de pasadas
    while((i < cant - 1) && intercambio){ // Bucle principal: continúa mientras haya intercambios y no se haya llegado al final del arreglo
        intercambio = false; // Se asume que no habrá intercambios en esta pasada
        for(int j = cant - 1; j > i; j--){ // Bucle interno: recorre el arreglo desde el final hasta la posición `i`
            if(arr[j] > arr[j - 1]){ // Comparación de elementos adyacentes
                int temp = arr[j]; // Variable temporal para realizar el intercambio
                arr[j] = arr[j - 1]; // Intercambio del elemento actual con el anterior
                arr[j - 1] = temp; // Finaliza el intercambio
                intercambio = true; // Se realizó un intercambio
            }
        }
        if(intercambio){ // Si se realizó algún intercambio
            i++; // Incrementa el contador de pasadas
        }
    }
}
