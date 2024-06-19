//Escribe una función que reciba dos números enteros y devuelva su suma

#include <iostream>
using namespace std;

int sumar(int numero1, int numero2);  //Funcion sumar y que parametros va a tener

int main(){
    
    int numero1, numero2;  //Las 2 variable que vamos a usar

    cout << "\nIngresa el primer numero: ";
    cin >> numero1;
    cout << "Ingresa el segundo numero: ";
    cin >> numero2;
    cout << "\nLa suma de " << numero1 << "+" << numero2 << " es: " << sumar(numero1,numero2);  //Llamamos a la funcion sumar que definimos abajo
    return 0;
}

int sumar(int numero1, int numero2){
    int suma = numero1 + numero2;
    return suma;
}
