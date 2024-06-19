#include <iostream>
#include <cmath>
using namespace std;

int main(){
    int i, Numero, Resultado, x = 1; 
    double Raiz;

    cout << "Ingrese un numero entero POSTIVO: ";
    cin >> Numero;

    cout << "El valor Ingresado es ---> " << Numero << endl;

    Raiz = sqrt(Numero);
    cout << "La raiz cuadrada es de ---> " << Raiz << endl; 

    Raiz = trunc(Raiz);
    cout << "La parte entera de la raiz es de ---> " << Raiz << endl;

    while (Numero >= 10){
        Numero = Numero / 10;
        x++;
    }

    Resultado = pow(Raiz, x);

    cout << "El numero que elegiste tiene ---> " << x << " cifras " << endl;
    cout << "El resultado es de ---> " << Resultado;

    return 0;

}