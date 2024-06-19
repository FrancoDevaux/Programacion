#include <iostream>
#include <cstdlib>  //Generar Numeros aleatorios
#include <ctime>  // La semilla de los numeros aleatorio


using namespace std;

int main(){

    int numeroAdivinar, numeroIngresado, intentos = 0;

    srand(time(NULL)); // Inicializar la semilla para generar numeros aleatorios


    //Ahora vamos a generar numeros aleatorios del 1 al 100
    numeroAdivinar = rand() % 100 + 1;

    do
    {
        cout << "\nIngrese un numero: ";
        cin >> numeroIngresado;

        intentos++;

        if (numeroIngresado > numeroAdivinar)
        {
            cout << "El numero ingresado es MAYOR" << endl;
        }
        else if (numeroIngresado < numeroAdivinar)
        {
            cout << "El numero ingresado es MENOR" << endl;
        }
        else
        {
            cout << "ADIVINASTE" << endl;
        }

    } while (numeroAdivinar != numeroIngresado);

    cout << "\nLa cantidad de intentos fue de ---> " << intentos << " intentos." << endl;

    return 0;

}