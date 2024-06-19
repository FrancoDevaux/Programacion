/*6)
Estructuras y manejo de arreglos.
a)Crea una estructura "Estudiante" con los campos "nombre", "edad" y "notas" (este campo debe almacenar la nota de los 3 
parciales). Crea un arreglo de estructuras de tamaño 3 y permite que el usuario ingrese los datos de los estudiantes.
b)Mostrar la nota más alta de cada estudiante de forma clara.
c)Calcular y mostrar el promedio de cada alumno y el promedio general del curso.
d)Modificar la nota del tercer parcial del segundo estudiante. Si tiene una nota menor que 60, se le debe sumar el 25%, 
si la nota está entre 60 y 80 se le debe sumar el 5% y si es mayor que 80 debe restar el 3%.*/

//------------------------------------------------------------------------------------------------------------------------

//Vamos a necestiar una estructura Estudiantes (nombre string, edad entero, notas arreglo=3)
//Usar una lista estudanite (arreglo[estudiante])
//funciones:(notaAlta float, promedio float, promedioGeneral float, modificarNota void, mostarLista void, llenarDatos void)

#include <iostream>
#include <string>
using namespace std;

//ESTRUCTURA llamada Estudiantes que contiene 3 datos
struct Estudiante {
    string nombre;
    int edad;
    float notas[3];
};


//PROTOTIPOS ---> antes del main
void llenarDatos(Estudiante arr[], int cant);
void mostrarLista(Estudiante arr[], int cant);
float notaAlta(float arr[], int cant);
float promedio(float arr[], int cant);
float promedioGeneral(Estudiante arr[], int cant);
void modificarNota(float &nota);


//MAIN
int main(){

    const int tam = 3;

    Estudiante lista[tam]; //Arreglo de la lista estudiante
    llenarDatos(lista,tam);  //Pusimo 2 paraemtrso por la funcion void que puismo q va hacer de 2
    mostrarLista(lista,tam);

    for (int i = 0; i < tam; i++){ //Para mostar la nota mas alta y entra a lista de 3
        cout << "\nLa nota mas alta del alumno " << i+1 << " es: " << notaAlta(lista[i].notas,3) << endl; 
    }                                                           //,3 es porque es la cant de estuidante parciales

    cout << "\nEl promedio general es: " << promedioGeneral(lista,tam) << endl;

    modificarNota(lista[1].notas[2]);
    mostrarLista(lista, tam);

    return 0;
}



//FUNCIONES ---> despues del main
void llenarDatos(Estudiante arr[], int cant){
    for (int i = 0; i < cant; i++){
        cout << "\nIngrese nombre " << i+1 << ": ";
        cin >> arr[i].nombre;
        cout << "Ingrese edad: " << i+1 << ": ";;
        cin >> arr[i].edad;

        for (int j = 0; j < 3; j++){  //Para las notas
            cout << "Ingrese nota de parcial " << j+1 << i+1 <<":";  //porque el primer lugar del arreglo es cero, y ahor ava a valer lo del parcial 1
            cin >> arr[i].notas[j];
        }
    }
}  //NO lleva return porque es void

void mostarLista(Estudiante arr[], int cant){
    for (int i = 0; i < cant; i++){

        cout << "------------------Alumno " << i+1 << "---------------" << endl;

        cout << "\nNombre: " << arr[i].nombre << endl;
        cout << "Edad: " << arr[i].edad << endl;

        for (int j = 0; j < cant; j++){  //OBSERVACION si poner < 3.....
            cout << "Nota parcial " << j+1 << ": " << arr[i].notas[j] << endl;
        }
    }
}

float notaAlta(float arr[], int cant){
    float mayor = 0;
    for (int i = 1; i < cant; i++){
        if (arr[i] > mayor){     //mayor seri al anota mas alta 
            mayor = arr[i];
        }
    }
    return mayor;
}

float promedio(float arr[], int cant){
    float suma = 0;
    for (int i = 0; i < cant; i++){
        suma += arr[i];
    }
    return (suma/cant);
}

float promedioGeneral(Estudiante arr[], int cant){
    float suma = 0;
    for (int i = 0; i < cant; i++){
    suma += promedio(arr[i].notas,3);
    }
    return (suma/cant);
}

void modificarNota(Estudiante arr[], int cant){
    
}


