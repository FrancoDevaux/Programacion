#include <iostream>
#include <cmath>
using namespace std;

int main (){

    int numero1, numero2, multiplicacion;
    double division;

    cout << "\nIngrese un numero del (1-10): ";
    cin >> numero1;
    cout << "\nIngrese otro numero del (1-10): ";
    cin >> numero2;


    if ((numero1 <= 10 && numero2 <=10) && (numero1 % 2 == 0 && numero2 % 2 == 0))
    {
        cout << "\nAmbos numeros son PARES!" << endl;
        division = (numero1 / numero2);
        cout << "\nLa division entre los numeros: " << numero1 << " y " << numero2 << " es ---> " << division << endl;

    }
    else if ((numero1 <= 10 && numero2 <=10) && (numero1 % 2 != 0 || numero2 % 2 != 0))
    {
        //cout << "\nAmbos numeros son IMPARES!" << endl;
        
        //int mayor = max(numero1, numero2);
        //int menor = min(numero1, numero2); //esta es otra forma de sacar el numero min o mayor de 2 numeros

        if (numero1 > numero2){
        multiplicacion = pow(numero1, numero2);
        cout << "\nLa multiplicacion de elevar: " << numero1 << " a la " << numero2 << " es ---> " << multiplicacion << endl;
        }
        else
        {
            multiplicacion = pow(numero2, numero1);
            cout << "\nLa multiplicacion de elevar: " << numero2 << " a la " << numero1 << " es ---> " << multiplicacion << endl;
        }

    }
    else{
        cout << "\nIngresaste numeros fuera del RANGO (1-10)" << endl;
    }
    
    return 0;

    

}