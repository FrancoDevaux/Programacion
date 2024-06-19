/*
Crea un juego de adivinanzas numéricas. El programa debe tener las siguientes funciones:
. GenerarNumeroAleatorio: Esta función genera y devuelve un número aleatorio dentro de un rango especificado 1 a 1000.
. ValidarEntrada: Esta función recibe un número ingresado por el usuario y verifica si es válido 
(por ejemplo, si es un número dentro del rango establecido).
. ComprobarAdivinanza: Esta función recibe el número ingresado por el usuario y el número objetivo a adivinar, 
y devuelve un mensaje indicando si el usuario adivinó el número o si es mayor o menor que el objetivo.

El programa principal debe utilizar estas funciones para permitir que el usuario intente adivinar
el número objetivo. El juego debe proporcionar pistas al usuario indicando si el número ingresado
es mayor o menor que el número objetivo, hasta que el usuario adivine el número correcto.
*/

#include <iostream>
#include <cstdlib>
#include <ctime>
using namespace std;

//PROTOTIPOS
int GenerarNumeroAleatorio();
bool ValidarEntrada(int numeroIngresado, bool& validar);
bool ComprobarAdivinanza(int numeroIngresado, int AdivinarNumero, bool& adivinado);

//MAIN
int main(){
    int AdivinarNumero = GenerarNumeroAleatorio(), NumeroPuesto;
    bool adivinado = false, validar = false;

    do{
        cout << "\nIngrese un numero: ";
        cin >> NumeroPuesto;

        ValidarEntrada(NumeroPuesto,validar);
        if (validar){
            ComprobarAdivinanza(NumeroPuesto,AdivinarNumero,adivinado);
            if (adivinado){
                cout << "\n[+]ADIVINASTE el numero!";
            }
            else if (AdivinarNumero > NumeroPuesto){
               cout << "\nEl numero a adivinar es MAYOR a " << NumeroPuesto;
            }else if (AdivinarNumero < NumeroPuesto){
                cout << "\nEl numero a adivinar es MENOR a " << NumeroPuesto;
            }
        }
        else{
            cout << "\n[!]Numero no valido, vuelve a poner otro gilipollas";
        }
        
    }while(adivinado == false);

    return 0;
}

//FUNCIONES
int GenerarNumeroAleatorio(){
    srand(time(NULL));
    int NumerosRandoms = rand() % 1000 + 1; //Numeros del 1 al 1000 
    return NumerosRandoms;
}

bool ValidarEntrada(int numeroIngresado, bool &validar){
    if ((numeroIngresado <= 1000) && (numeroIngresado >=1)){
        validar = true;
    }
    else{
        validar = false;
    }
    return validar;
}

bool ComprobarAdivinanza(int numeroIngresado, int AdivinarNumero, bool &adivinado){
    if (numeroIngresado == AdivinarNumero){
        adivinado = true;
    }
    return adivinado;
}