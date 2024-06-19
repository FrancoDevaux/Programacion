#include <iostream>

using namespace std;

int main (){

    double precio, descuento;
    string membresia;

    cout << "Ingrese el precio de tu helado: $";
    cin >> precio;
    cout << "Ahora ingrese tu tipo de membresia (A/B/C): ";
    cin >> membresia;

    if (membresia == "A" || membresia == "a"){
        descuento = (precio * 0.1);
        descuento = (precio - descuento);
        cout << "Al ser cliente con la membresia de tipo A, tu compra final es de ---> $" << descuento;
    }
    else if (membresia == "B" || membresia == "b"){
        descuento = (precio * 0.15);
        descuento = (precio - descuento);
        cout << "Al ser cliente con la membresia de tipo B, tu compra final es de ---> $" << descuento;
    }
    else if (membresia == "C" || membresia == "c"){
        descuento = (precio * 0.2);
        descuento = (precio - descuento);
        cout << "Al ser cliente con la membresia de tipo C, tu compra final es de ---> $" << descuento;
    }
    else{
        cout << "Ingresesate una membresia INVALIDA";
    }

    return 0;

}