#include <iostream>
#include <cstdlib>   
#include <ctime>
#include <algorithm>

using namespace std;

//Declaramos una constante para el tamaño de la matriz
const int n = 3;

//Declaración de funciones void
void cargarMatrizAleatoria(int matriz[n][n]);
void cargarMatrizManual(int matriz[n][n]);
void mostrarMatriz(const int matriz[n][n]);
bool buscarValor(const int matriz[n][n], int valor);
int encontrarMaximo(const int matriz[n][n]);
int encontrarMinimo(const int matriz[n][n]);
void ordenarMatriz(int matriz[n][n], bool ascendente); //declare una bandera booleana que me indica el orden


int main() {
    int matriz[n][n];
    bool matrizCargada = false; //Inicializamos la variable en falso porque no esta cargada al princpio hasta que el User lo haga
    int opcion;

    do {

        //Que muestre el menú interactivo con estas opciones y elija una el User
        cout << "\nMenu:\n";
        cout << "1. Cargar la matriz con numeros aleatorios\n";
        cout << "2. Cargar la matriz de forma manual\n";
        cout << "3. Mostrar los valores de la matriz\n";
        cout << "4. Buscar un valor especifico en la matriz\n";
        cout << "5. Devolver el valor maximo de la matriz\n";
        cout << "6. Devolver el valor minimo de la matriz\n";
        cout << "7. Ordenar los valores de la matriz de forma ascendente\n";
        cout << "8. Ordenar los valores de la matriz de forma descendente\n";
        cout << "9. Salir del programa\n";
        cout << "\nIngrese su opcion: ";
        cin >> opcion;

        switch(opcion) {
            case 1:
                cargarMatrizAleatoria(matriz);
                matrizCargada = true;  //La ponemos en true para validar que la matriz esta cargada
                break;
            case 2:
                cargarMatrizManual(matriz);
                matrizCargada = true; //La ponemos en true para validar que la matriz esta cargada
                break;
            case 3:
                if (matrizCargada) { //Si la matriz fue cargada osea esta en true, que me muestre la matriz sino que imprima lo de abajo
                    mostrarMatriz(matriz);
                } else {
                    cout << "\n[!]Primero debe cargar la matriz.\n";
                }
                break;
            case 4:
                if (matrizCargada) { //Matriz cargada en true, que ingrese un valor que quiera buscar
                    int valor;
                    cout << "Ingrese el valor a buscar: ";
                    cin >> valor;
                    if (buscarValor(matriz, valor)) { //Si el valor ingresado esta en la matriz hace lo de abajo sino ejecuta el else
                        cout << "\nEl valor ---> " << valor << " se encuentra en la matriz.\n";
                    } else {
                        cout << "\nEl valor ---> " << valor << " no se encuentra en la matriz.\n";
                    }
                } else {
                    cout << "\n[!]Primero debe cargar la matriz.\n";
                }
                break;
            case 5:
                if (matrizCargada) { //matriz cargada en true, y que immprima el valor maximo llamando a la funcion (encontarMaximo) de la matriz 3x3
                    cout << "El valor máximo de la matriz es: " << encontrarMaximo(matriz) << endl;
                } else {
                    cout << "\n[!]Primero debe cargar la matriz.\n";
                }
                break;
            case 6:
                if (matrizCargada) { //Matriz cargada en true, y que immprima el valor minimo llamando a la funcion (encontarMinimo) de la matriz 3x3
                    cout << "El valor mínimo de la matriz es: " << encontrarMinimo(matriz) << endl;
                } else {
                    cout << "\n[!]Primero debe cargar la matriz.\n";
                }
                break;
            case 7:
                if (matrizCargada) {
                    ordenarMatriz(matriz, true); //En true para que se ordene de forma ascendente (de mayor a menor)
                    cout << "[+]Matriz ordenada de forma ascendente.\n";
                } else {
                    cout << "\n[!]Primero debe cargar la matriz.\n";
                }
                break;
            case 8:
                if (matrizCargada) {
                    ordenarMatriz(matriz, false); //Sino en false para que se ordene en forma descendente (de menor a mayor)
                    cout << "[+]Matriz ordenada de forma descendente.\n";
                } else {
                    cout << "\n[!]Primero debe cargar la matriz.\n";
                }
                break;
            case 9:
                cout << "\nSaliendo del programa...\n";
                break;
            default:
                cout << "\n[[!]]Opcion no valida, ingrese nuevamente una opcion correcta.\n";
        }
    } while(opcion != 9);

    return 0;
}

//Cargar la matriz con números aleatorios
void cargarMatrizAleatoria(int matriz[n][n]) {
    srand(time(0));
    for(int i = 0; i < n; ++i) {
        for(int j = 0; j < n; ++j) {
            matriz[i][j] = rand() % 100 + 1;
        }
    }
    cout << "\n[+]Matriz cargada con numeros aleatorios.\n";
}

//Cargar la matriz de forma manual ingresada por el User
void cargarMatrizManual(int matriz[n][n]) {
    for(int i = 0; i < n; ++i) {
        for(int j = 0; j < n; ++j) {
            cout << "Ingrese el valor para la posicion [" << i << "][" << j << "]: ";
            cin >> matriz[i][j];
        }
    }
    cout << "\n[+]Matriz cargada de forma manual.\n";
}

//Mostrar los valores de la matriz 
void mostrarMatriz(const int matriz[n][n]) {
    for(int i = 0; i < n; ++i) {
        for(int j = 0; j < n; ++j) {
            cout << matriz[i][j] << "\t";
        }
        cout << endl;
    }
}

//Buscar un valor específico en la matriz y en el main le preguntamos que valor quiere elegir
bool buscarValor(const int matriz[n][n], int valor) {
    for(int i = 0; i < n; ++i) {
        for(int j = 0; j < n; ++j) {
            if(matriz[i][j] == valor) {
                return true;  //Lo retornamos en true porque habria coincidencia sino en false
            }
        }
    }
    return false;
}

//Encontrar el valor máximo de la matriz
int encontrarMaximo(const int matriz[n][n]) {
    int maximo = matriz[0][0];
    for(int i = 0; i < n; ++i) {
        for(int j = 0; j < n; ++j) {
            if(matriz[i][j] > maximo) {
                maximo = matriz[i][j];
            }
        }
    }
    return maximo;
}

//Encontrar el valor mínimo de la matriz
int encontrarMinimo(const int matriz[n][n]) {
    int minimo = matriz[0][0];
    for(int i = 0; i < n; ++i) {
        for(int j = 0; j < n; ++j) {
            if(matriz[i][j] < minimo) {
                minimo = matriz[i][j];
            }
        }
    }
    return minimo;
}

// Función para ordenar la matriz
void ordenarMatriz(int matriz[n][n], bool ascendente) {
    int temp[n * n]; //Declare un array temporal para almacenar todos los elementos de la matriz
    int index = 0; //Esta varaible lleva un registro de la posición actual en el array (temp) donde se debe colocar el siguiente elemento
    for(int i = 0; i < n; ++i) {
        for(int j = 0; j < n; ++j) {
            temp[index++] = matriz[i][j];
        }
    }
    if (ascendente) {
        sort(temp, temp + n * n); //Utilizo sort para ordenar los elementos en el array temp. Los dos primeros argumentos especifican las posiciones inicial y final del array a ordenar
    } else {
        sort(temp, temp + n * n, greater<int>()); //utilizo la función greater<int>() como una función de comparación que ordenaria en orden descendente 
    }
    index = 0;
    for(int i = 0; i < n; ++i) {
        for(int j = 0; j < n; ++j) {
            matriz[i][j] = temp[index++];
        }
    }
}