#include <iostream>
#include <cmath>
using namespace std;

int main(){
    int cant_zapatos, precio_inicial, total_compra;
    const int precio = 8000;
    float descuento;


    cout << "\nIngrese cuantos pares de calzado va a comprar: ";
    cin >> cant_zapatos;
    
    precio_inicial = (cant_zapatos * precio);
    cout << "El precio inicial de la compra es de: $" << precio_inicial << endl;

    if (cant_zapatos >= 10 && cant_zapatos < 20)
    {
        descuento = (precio_inicial * 0.1);
        cout <<  "El decuento es de ---> " << descuento << endl;

        total_compra = (precio_inicial - descuento);
        cout << "El precio Final es de: $" << total_compra;
    }

    else if (cant_zapatos >= 20 && cant_zapatos <= 30)
    {
        descuento = (precio_inicial * 0.2);
        cout <<  "El decuento es de ---> " << descuento << endl;

        total_compra = (precio_inicial - descuento);
        cout << "El precio Final es de: $" << total_compra;
    }

    else
    {
        descuento = (precio_inicial * 0.4);
        cout <<  "El decuento es de ---> " << descuento << endl;

        total_compra = (precio_inicial - descuento);
        cout << "El precio Final es de: $" << total_compra;
    }

    return 0;
}