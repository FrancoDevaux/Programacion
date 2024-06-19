//Implementa una función que reciba un arreglo de enteros y calcule la suma de todos sus elementos.

#include <iostream>
using namespace std;

int sumarArreglos (int arreglo[], int n){  //Decalaramos la funcion de sumar arreglos
    int suma = 0;  // Suma obvio que vale cero porque empieza sin nada
    for (int i = 0; i < n; i++){  //Recorremos el array hasta n que definimos abajo que vale 6 con esos numeros
        suma += arreglo[i];
    }
    return suma;  //que nos devuleva suma
}

int main(){

    int n = 6, array[n] = {6,5,4,3,2,1};
    cout << "\nLa suma de los elemntos del array es: " << sumarArreglos(array,n); //Poner en orden primero el array y luego el tamaño sino no funciona
    return 0;
}
