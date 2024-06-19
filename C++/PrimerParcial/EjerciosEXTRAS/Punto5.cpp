#include <iostream>
#include <string>
#include <cmath>
using namespace std;

int main(){

    string nombre;
    int dia, mes, anio, caracteres, suma_digitos;
    int mes_viaje, dia_viaje;

    cout << "\nIngrese tu nombre: ";
    (getline(cin,nombre));

    cout << "\nIngrese fecha de nacimiento (dia): ";
    cin >> dia;
    cout << "\nIngrese fecha de nacimiento (mes): ";
    cin >> mes;
    cout << "\nIngrese fecha de nacimiento (anio): ";
    cin >> anio;

    caracteres = nombre.length();
    cout << "\nEl nombre " << nombre << " tiene " << caracteres << " letras." << endl;

    if (caracteres > 12)
    {
        suma_digitos = 0;
        while (caracteres != 0) 
        {
            suma_digitos += caracteres % 10;
            caracteres /= 10;
        }

        mes_viaje = suma_digitos;
        cout << "\nLa suma es de --> " << mes_viaje << endl;
        


        dia_viaje = trunc((dia * mes) / anio);
        cout << "\nEl resultado de dia_viaje es: " << dia_viaje << endl;

        if (dia_viaje > 31) 
        {
            dia_viaje = 3;
        }

        cout << "\nTe vas de viaje el dia " << dia_viaje << endl;

    }
    else
    {
        cout << "\n!PERO NO ingreasate letras." << endl;
    }
    
    return 0;

}