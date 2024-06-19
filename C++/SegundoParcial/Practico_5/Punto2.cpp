#include <iostream>

using namespace std;

int main(){

    int numeros[] = {24, 5, 58, 100, -8, 94, 96, -16, 105};

    int buscarNumero;
    cout << "\nIngrese un numero que desa buscar: ";
    cin >> buscarNumero;

    bool encontrado = false;
    int posicion;

    for (int i = 0; i < 10; i++){
        if (numeros[i] == buscarNumero){
            encontrado = true;
            posicion = i;
            break;
        }
    }

    if (encontrado)
    {
        cout << "El numero " << buscarNumero << " se encuentra en la posicion " << posicion + 1 << endl;
    }
    else
    {
        cout << "El numero " << buscarNumero << " no se encuntra en el arreglo." << endl;
    }

    return 0;

}