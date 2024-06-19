#include <iostream>
#include <cstdlib>   
#include <ctime>
using namespace std;


//Declaramos una variable constante para el tamaño de la matriz
const int n = 3;

//Declaración de funciones void
void cargarMatrizAleatoria(int matriz[n][n]);
void cargarMatrizManual(int matriz[n][n]);
void mostrarMatriz(const int matriz[n][n]);
bool buscarValor(const int matriz[n][n], int valor);
int encontrarMaximo(const int matriz[n][n]);
int encontrarMinimo(const int matriz[n][n]);
void ordenarMatriz(int matriz[n][n], bool ascendente); /*Declare una bandera booleana que me indica el orden,
                                                        si va a hcer ascendente o descendente.*/

int main() {
    int matriz[n][n];
    bool matrizCargada = false; //Inicializamos la variable en falso porque no esta cargada al princpio hasta que el User lo haga.
    int opcion;

    do {

        //Que muestre el menú interactivo con estas opciones y elija una el User.
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
                matrizCargada = true;  //La ponemos en true para validar que la matriz ya fue cargada.
                break;
            case 2:
                cargarMatrizManual(matriz);
                matrizCargada = true; //La ponemos en true para validar que la matriz ya fue cargada.
                break;
            case 3:
                if (matrizCargada) { //Si la matriz fue cargada osea esta en true, que me muestre la matriz sino que imprima lo de abajo
                    mostrarMatriz(matriz);
                } else {
                    cout << "\n[!]Primero debe cargar la matriz.\n";
                }
                break;
            case 4:
                if (matrizCargada) { //Si Matriz cargada es true, que ingrese un valor que quiera buscar
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
                if (matrizCargada) { //Si Matriz cargada es true, y que immprima el valor maximo llamando a la funcion (encontarMaximo) de la matriz 3x3
                    cout << "El valor maximo de la matriz es: " << encontrarMaximo(matriz) << endl;
                } else {
                    cout << "\n[!]Primero debe cargar la matriz.\n";
                }
                break;
            case 6:
                if (matrizCargada) { //Matriz cargada en true, y que immprima el valor minimo llamando a la funcion (encontarMinimo) de la matriz 3x3
                    cout << "El valor minimo de la matriz es: " << encontrarMinimo(matriz) << endl;
                } else {
                    cout << "\n[!]Primero debe cargar la matriz.\n";
                }
                break;
            case 7:
                if (matrizCargada) {
                    ordenarMatriz(matriz, true); //En true para que se ordene de forma ascendente (de mayor a menor)
                    cout << "\n[+]Matriz ordenada de forma ascendente.\n";
                } else {
                    cout << "\n[!]Primero debe cargar la matriz.\n";
                }
                break;
            case 8:
                if (matrizCargada) {
                    ordenarMatriz(matriz, false); //Sino en false para que se ordene en forma descendente (de menor a mayor)
                    cout << "\n[+]Matriz ordenada de forma descendente.\n";
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
    } while(opcion != 9); //Mostar el MENU mientras opcion sea distinto de 9

    return 0;
}

//Cargar la matriz con números aleatorios
void cargarMatrizAleatoria(int matriz[n][n]) {
    srand(time(0));
    for(int i = 0; i < n; ++i) {
        for(int j = 0; j < n; ++j) {
            matriz[i][j] = rand() % 100 + 1; //Del 1 al 100
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

//Buscar un valor específico en la matriz y en el Main le preguntamos que valor quiere elegir
bool buscarValor(const int matriz[n][n], int valor) {
    for(int i = 0; i < n; ++i) {
        for(int j = 0; j < n; ++j) {
            if(matriz[i][j] == valor) {
                return true;  //Lo retornamos en true porque habria coincidencia sino retorna falso.
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

// Función para ordenar la matriz --> Use el OrdenamientoInserccionIntercambio
void ordenarMatriz(int matriz[n][n], bool ascendente){
    int array[n*n]; //Declare un array en donde almacena los elementos de la matriz
    for (int i = 0; i < n; i++){
        for(int j=0; j < n; j++){
            array[i*3 +j]= matriz[i][j]; //De matriz al array, poner i*n+j es lo mismo
        }
    }
    cout << "Este arreglo esta sin ordenar: ";
    for (int i = 0 ;i < 9; i++){
        cout << array[i] << " ";      //Aca mostramos el array sin ordenar
    }
    cout << endl;
    
    if (ascendente) {
        int tmp, pos;

        for (int i = 1; i < 9; i++){ // <9 porque sabemso que la matriz es de 3x3
            pos = i;
            while ((pos > 0) && (array[pos - 1] < array[pos])){ //Forma ascendnete <
                tmp = array[pos];
                array[pos] = array[pos - 1];
                array[pos - 1] = tmp;
                pos--; //Se decrementa para pasar al siguiente elementos
            }
        }
    } else {
        int tmp, pos;

        for (int i = 1; i < 9; i++){
            pos = i;
            while ((pos > 0) && (array[pos - 1] > array[pos])){ //Forma descendente >
                tmp = array[pos];
                array[pos] = array[pos - 1];
                array[pos - 1] = tmp;
                pos--;
            }
        }
    }

    cout << "Ahora se muetra el arreglo ordenado: ";
    for(int i = 0; i < 9; i++){
        cout << array[i] << " "; //Mostramos por consola el arreglo ordenado con un espacio entre numeros
    }
    cout << endl;

    for(int i = 0; i < 3; ++i) {
        for(int j = 0; j < 3; ++j) {
            matriz[i][j] = array[i*3+j];
        }
    }
}    
  


    