#include <iostream>
#include <string>

using namespace std;

// Prototipos de funciones (dos maneras diferentes de hacer lo mismo)
string quitarVocales(string pal); // Función que devuelve una nueva cadena sin vocales
void quitarVocal(string &pal); // Función que modifica la cadena original eliminando las vocales

int main(){
    string pal_ing; // Declaración de la variable para almacenar la palabra ingresada
    cout << "Ingrese una palabra" << endl; // Solicita al usuario que ingrese una palabra
    cin >> pal_ing; // Lee la palabra ingresada por el usuario

    //Distintas formas de llamar a la función dependiendo de cómo la hayamos declarado 
    
    //pal_ing = quitarVocales(pal_ing); // Opción 1: llamar a la función que devuelve una nueva cadena sin vocales
    //quitarVocal(pal_ing); // Opción 2: llamar a la función que modifica la cadena original
    
    // En este caso, se llama a la función que devuelve una nueva cadena sin vocales y se imprime el resultado
    cout << quitarVocales(pal_ing) << endl; 

    return 0; // Fin del programa
}

// Función que recibe una cadena y devuelve una nueva cadena sin vocales
string quitarVocales(string pal){
    int longitud = pal.length(); // Obtiene la longitud de la cadena
    string temp = ""; // Declara una cadena temporal para almacenar el resultado
    for(int i = 0; i < longitud; i++){
        // Si el carácter actual no es una vocal, se agrega a la cadena temporal
        if (pal[i] != 'a' && pal[i] != 'e' && pal[i] != 'i' && pal[i] != 'o' && pal[i] != 'u' ){
            temp = temp + pal[i];
        }
    }
    return temp; // Devuelve la cadena temporal sin vocales
}

// Función que recibe una referencia a una cadena y elimina las vocales de la cadena original
void quitarVocal(string &pal){
    int longitud = pal.length(); // Obtiene la longitud de la cadena
    string temp = ""; // Declara una cadena temporal para almacenar el resultado
    for(int i = 0; i < longitud; i++){
        // Si el carácter actual no es una vocal, se agrega a la cadena temporal
        if (pal[i] != 'a' && pal[i] != 'e' && pal[i] != 'i' && pal[i] != 'o' && pal[i] != 'u' ){
            temp = temp + pal[i];
        }
    }
    pal = temp; // Modifica la cadena original para que sea igual a la cadena temporal sin vocales
}
