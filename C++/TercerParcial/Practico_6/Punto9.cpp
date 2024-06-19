/*Implementa una función llamada "quitarVocales" que reciba una cadena de caracteres y
elimine todas las vocales de la palabra, manteniendo el resultado en la misma variable.*/


#include <iostream>
#include <string>
using namespace std;

//!esVocal ---> NEGARLO

// Prototipos de funciones (dos maneras diferentes de hacer lo mismo)
string quitarVocales(string pal);
//void quitarVocal(string &pal);  //Función que modifica la cadena original eliminando las vocales


int main(){
    string palabraIngresada;
    cout << "\nIngrese una palbara: ";
    cin >> palabraIngresada;

    palabraIngresada = quitarVocales(palabraIngresada);
    //quitarVocal(palabraIngresada); // Opción 2: llamar a la función que modifica la cadena original

    cout << "La palabra quitandole las vocales " << endl;
    cout << palabraIngresada << endl;

    return 0;
}

string quitarVocales(string pal){
    int longitud;
    longitud = pal.length(); //Obtiene la longitud de la cadena

    string temp = ""; //Declara una cadena temporal para almacenar el resultado

    for (int i = 0; i < longitud; i++){
        if (pal[i] != 'a' && pal[i] != 'e' && pal[i] != 'i' && pal[i] != 'o' && pal[i] != 'u'){
            temp = temp + pal[i];
        }
    }
    return temp; //Devuelve la cadena temporal sin vocales
}



// Esto se puede hacer un de esta forma o la de arriba, osea con void o con string
// Función que recibe una referencia a una cadena y elimina las vocales de la cadena original
/*void quitarVocal(string &pal){

    int longitud = pal.length(); // Obtiene la longitud de la cadena
    string temp = ""; // Declara una cadena temporal para almacenar el resultado

    for(int i = 0; i < longitud; i++){

        // Si el carácter actual no es una vocal, se agrega a la cadena temporal
        if (pal[i] != 'a' && pal[i] != 'e' && pal[i] != 'i' && pal[i] != 'o' && pal[i] != 'u' ){
            temp = temp + pal[i];
        }
    }
    pal = temp; // Modifica la cadena original para que sea igual a la cadena temporal sin vocales
}*/