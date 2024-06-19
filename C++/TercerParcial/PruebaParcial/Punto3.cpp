/*
Crea un programa que gestione una lista de Estudiante.
Cada estudiante debe tener siguintes atributos: [nombre,edad,la nota de los 3 parciales (en un arreglo) y si aprobo o no].
El programa debe permitirle al usuario ingresar la cantidad de Estudiante que desee a la lista sin necesidad de que se
llene por completo, luego debe mostar todos los Estudiante ingresados, tambien se debe ver en la terminal el procentaje
de aprobados del curso.
*/

#include <iostream>
#include <string>
using namespace std;


//ESTRUCTURA
struct Estudiante{
    string nombre;
    int edad;
    int notas[3]; //Porque son 3 notas que almacena
    bool aprobado;
};

//PROTOTIPOS
void llenarEstudiante(Estudiante &estudiante);
void cargarEstudiantes(Estudiante arr[], int &cantidadIngresados, int maximo);
void mostrarEstudiantes(Estudiante arr[], int cantidadIngresados);
void PorcentajeAprobados(Estudiante arr[], int cantidadIngresados);

//MAIN
int main(){
    const int maximo = 10;
    int cantidadIngresados = 0;
    Estudiante lista[maximo];

    cargarEstudiantes(lista, cantidadIngresados, maximo);
    mostrarEstudiantes(lista, cantidadIngresados);
    PorcentajeAprobados(lista, cantidadIngresados);

    return 0;
}

//FUNCIONES
void llenarEstudiante(Estudiante &estudiante){
    cout << "\nIngrese Nombre: ";
    cin >> estudiante.nombre;
    cout << "Ingrese Edad: ";
    cin >> estudiante.edad;
    
    //Para las notas que son 3 por eso el menor
    for (int i = 0; i < 3; i++){
        cout << "Ingrese Nota del Parcial " << i + 1 << ": ";
        cin >> estudiante.notas[i];
    }
    int sumatoria = 0;
    for (int i = 0; i < 3; i++){
        sumatoria += estudiante.notas[i];
    }
    float promedio = sumatoria / 3.0;
    estudiante.aprobado = promedio >= 6;

}

void cargarEstudiantes(Estudiante arr[], int &cantidadIngresados, int maximo){
    char opcion = 's'; //Que opcion ya valga s si es que elige la letra n.

    do{
        if (cantidadIngresados < maximo){
            llenarEstudiante(arr[cantidadIngresados]);
            cantidadIngresados++;
            if (cantidadIngresados < maximo){
                cout << "\nQuiere cargar mas estudiantes? [s][n]: ";
                cin >> opcion;
            }else{
                cout << "\n[!]Lista llena, no se puede ingresar otro estudiante." << endl;
                opcion = 'n';
            }
        }else{
            cout << "\n[!]Lista llena, no se puede ingresar otro estudiante." << endl;
            opcion = 'n';
        }
    }while (opcion == 's');
}


void mostrarEstudiantes(Estudiante arr[], int cantidadIngresados){
    for (int i = 0; i < cantidadIngresados; i++){
        cout << "\nNombre: " << arr[i].nombre << endl;
        cout << "Edad: " << arr[i].edad << endl;

        for (int j = 0; j < 3; j++){
            cout << "Nota Parcial " << j + 1 << ": " << arr[i].notas[j] << endl;
        }
        if (arr[i].aprobado){
            cout << "Estado del alumno: APROBADO" << endl;
        }else{
            cout << "Estado del alumno: DESAPROBADO" << endl;
        }
        cout << "--------------------LISTA ESTUDIANTE--------------------------------" << endl;
    }
}


void PorcentajeAprobados(Estudiante arr[], int cantidadIngresados){
    float cantidadPorcentaje;
    if (cantidadIngresados > 0){
        int aprobados = 0;
        for (int i = 0; i < cantidadIngresados; i++){
            if (arr[i].aprobado){
                aprobados++;
            }
        }
        cantidadPorcentaje = (aprobados / float(cantidadIngresados)) * 100;
    }else{
        cantidadPorcentaje = 0;
    }
    cout << "\nEl porcentaje de aprobados que hay es de ---> " << cantidadPorcentaje << "%" << endl;
}


