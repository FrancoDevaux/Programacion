#include <iostream>

using namespace std;

int main(){

    int horas, sueldo;
    const int Precio_Hora = 1000;
    const int Precio_Hora_Extra = 2000;

    cout << "Cuantas horas trabajaste para saber tu sueldo semanal: ";
    cin >> horas;

    if (horas <= 40)
        {
            sueldo = (horas * Precio_Hora);
            cout << "Tu sueldo semanal es de ---> $" << sueldo;
        }
        else
        {
            sueldo = (horas * Precio_Hora_Extra);
            cout << "Tu sueldo semanal es de ---> $" << sueldo;
        }

    return 0;


}



