/*Implementa una función que reciba una estructura "Persona" (con campos como nombre,
edad, etc.) por valor y la imprima en pantalla.*/


#include <iostream>
#include <string>
using namespace std;

struct Persona
{
    string nombre;
    int edad;
    int telefono;
};

//PROTOTIPOS
void imprimirDatos(Persona pers);
void cargarDatos(Persona  &pers); //porque todo lo que se haga dentro quiero que siga estando dentro de esta funcion

int main(){
    Persona persona; //Crea la variable persona
    cargarDatos(persona);
    imprimirDatos(persona);

    return 0;

}

void cargarDatos(Persona &pers){
    cout << "\nIngrese el nombre: ";
    cin >> pers.nombre;

    cout << "Ingrese edad: ";
    cin >> pers.edad;

    cout << "Ingrese telefono: ";
    cin >> pers.telefono;

}

void imprimirDatos(Persona pers){
    cout << "\nNombre: " << pers.nombre << endl;

    cout << "Edad: " << pers.edad << endl;

    cout << "Telefono: " << pers.telefono << endl;
}