//antes ordenar el arreglo de forma ascendente para hacerse este algoritmo.

#include<iostream>

using namespace std;

int main()

{

    int n,mitad,primero,ultimo,x, arreglo[] = {0,1,2,3,4,5,6,7,8,9};  //arreglo ordenado

    primero = 0;

    ultimo = 9;

    x = 0;

    cout<< "\ningresa el numero a buscar:" ;

    cin>> n;

    
    while (primero <= ultimo && x == 0)
    {

        mitad = (primero + ultimo) / 2;

        //cout << mitad << "\t";

        if (n == arreglo[mitad])

            x = 1;

        else if (n < arreglo[mitad])

            ultimo = mitad -1;

        else if (n > arreglo[mitad])

            primero = mitad + 1;

    }

    if (x == 1)

        cout<<"\nEl numero " << n << " se encuentra en el vector";

    else

        cout<< "\nEl numero no se encuentra el vector";

    return 0;

}