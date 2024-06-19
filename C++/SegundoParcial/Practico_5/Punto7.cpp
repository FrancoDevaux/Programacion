/*Escribir un programa que le pida al usuario ingresar una palabra de no más de 10 letras, luego
debe llenar un arreglo con las letras de la palabra desde atrás hacia delante y en caso de que
queden huecos en el arreglo debe llenarse con *. Luego mostrar en consola el contenido de
dicho arreglo.*/
//Ejemplo: Si se ingresa la palabra trabajo, el arreglo debe quedar de la siguiente manera ojabart***

#include <iostream>

using namespace std;

int main(){

    //Variables
    string palabra;
    char arreglo[10];


    //Que el usuario ingrese una PALABRA
    cout << "\nIngrese una palabra de 10 o menos letras: ";
    cin >> palabra;


    //Si supera la 10 LETRAS que muestre esto
    if (palabra.length() > 10){
        cout << "\n\t\t[!]Ingresaste MAS de 10 letras";
        return 1;
    }
    

    //Cargar el arreglo con las letras en orden INVERSO
    for (int i = 0; i < palabra.length(); i++){
        arreglo[i] = palabra[palabra.length()-i-1];
    }


    //Rellenar el arreglo con *
    for (int i = palabra.length(); i < 10; i++){
        arreglo[i] = '*';
    }


    //Mostar el arreglo en CONSOLA
    for (int i = 0; i < 10; i++){
        cout << arreglo[i];
    }
    cout << endl;

    return 0;

}   