/*Crea un programa que gestione una lista de libros. Cada libro debe tener los siguientes
atributos: título, autor y año de publicación. El programa debe tener las siguientes funciones:
• agregarLibro: Esta función recibe por parámetro los datos de un libro (título, autor y
año de publicación) y agrega un nuevo libro a la lista de libros.
• buscarLibroPorAutor: Esta función recibe por parámetro el nombre de un autor y busca
todos los libros de la lista que coincidan con ese autor. Devuelve una lista de libros que
cumplen con la condición.
• mostrarLibros: Esta función muestra en pantalla todos los libros de la lista, uno por
línea.
Utiliza una estructura llamada Libro para representar los datos de cada libro*/

/*ESTRATEGIA: 
agregarLibro, mostrarLibro, BuscarLibroPorAutor*/

#include <iostream>
#include <string>

using namespace std;

//Estructura de libro
struct Libro{
    string titulo;
    string autor;
    int lanzamiento;
};

//PROTOTIPOS
void agregarLibro(Libro arr[], int maximo, int &tope); //&tope porque le mando cuantos tengo ingresados en el arreglo, osea si se pasaria de 10 que defini
void cargar(Libro &libro);
void buscarLibroPorAutor(Libro arr[], int cant, string nombre);
void mostrarLibro(Libro arr[], int cant);


int main(){
    Libro lista[10];  //Arreglo que contiene cada lugar una estructura de libro
    int cant_lleno = 0;  //Cuantos libros yo llene en el arreglo
    string nombreBuscado;

    agregarLibro(lista, 10, cant_lleno);
    mostrarLibro(lista, cant_lleno);

    cout << "\nIngrese un autor para buscar en la biblioteca: ";
    cin >> nombreBuscado;
    buscarLibroPorAutor(lista, cant_lleno, nombreBuscado);

    return 0;
}


//FUNCIONES
void agregarLibro(Libro arr[], int maximo, int &tope){
    bool salir = false;
    char opcion = ' ';
    do{
        //Saber si tengo lugar para ingrere un libro
        if (maximo > tope){
            Libro nuevo;
            cargar(nuevo);
            arr[tope] = nuevo;
            tope++; //porque ingresate un libro
        }
        else{
            cout << "\nLista llena";
            salir = true;
        }
        do{
            cout << "\nQuiere ingresar otro libro [s][n]: ";
            cin >> opcion;
        }while(opcion != 's' && opcion != 'n');

        if (opcion == 'n'){
            salir = true;
        }

    }while(!salir);
}

void cargar(Libro &libro){  //los puntos son para acceder a las ESTRUCTURAS del principio
    cout << "\nIngrese titulo del libro: ";
    cin >> libro.titulo;
    cout << "Ingrese autor: "; 
    cin >> libro.autor;
    cout << "Ingrese anio de lanzamiento: ";
    cin >> libro.lanzamiento;
}

void buscarLibroPorAutor(Libro arr[], int cant, string nombre){
    for (int i = 0; i < cant; i++){
        if (nombre == arr[i].autor){
            cout << arr[i].titulo;
        }
    }
}

void mostrarLibro(Libro arr[], int cant){
    for (int i = 0; i < cant; i++){
        cout << "\nTitulo: " << arr[i].titulo << endl;
        cout << "Autor: " << arr[i].autor << endl;
        cout << "Anio Lanzamineto: " << arr[i].lanzamiento << endl;
    }
    cout << endl;
}

