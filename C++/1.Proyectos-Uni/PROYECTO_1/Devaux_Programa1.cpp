#include <iostream>
#include <cmath>
#include <string>
using namespace std;

int main(){

    // Declaramos unas variables
    int dia, mes, total_invitados;
    float invitados;
    string FestejoCumple;


    // User ingresa dia y mes de nacimiento
    cout << "\nIngrese el DIA de nacimiento: ";
    cin >> dia;
    cout << "Ingrese el numero del MES de nacimiento: ";
    cin >> mes;
    

    // Especificar a que signo zodiaco pertences segun el dia y mes ingresado
    if ((mes == 1 && dia >= 20) || (mes == 2 && dia <= 19)) 
    {
        cout << "Su signo del zodico es ---> Acuario" << endl;
    }
    
    else if ((mes == 2 && dia >= 20) || (mes == 3 && dia <= 20)) 
    {
        cout << "Su signo del zodiaco es ---> Piscis" << endl;
    }

    else if ((mes == 3 && dia >= 21) || (mes == 4 && dia <= 19)) 
    {
        cout << "Su signo del zodiaco es ---> Aries" << endl;
    }
    
    else if ((mes == 4 && dia >= 20) || (mes == 5 && dia <= 20))
    {
        cout << "Su signo del zodiaco es ---> Tauro" << endl;
    }

    else if ((mes == 5 && dia >= 21) || (mes == 6 && dia <= 21))
    {
        cout << "Su signo del zodiaco es ---> Geminis" << endl;
    }

    else if ((mes == 6 && dia >= 22) || (mes == 7 && dia <= 22))
    {
        cout << "Su signo del zodiaco es ---> Cancer" << endl;
    }

    else if ((mes == 7 && dia >= 23) || (mes == 8 && dia <= 23))
    {
        cout << "Su signo del zodiaco es ---> Leo" << endl;
    }

    else if ((mes == 8 && dia >= 24) || (mes == 9 && dia <= 22))
    {
        cout << "Su signo del zodiaco es ---> Virgo" << endl;
    }

    else if ((mes == 9 && dia >= 23) || (mes == 10 && dia <= 22))
    {
        cout << "Su signo del zodiaco es ---> Libra" << endl;
    }

    else if ((mes == 10 && dia >= 23) || (mes == 11 && dia <=22))
    {
        cout << "Su signo del zodiaco es ---> Escorpio" << endl;
    }

    else if ((mes == 11 && dia >= 23) || (mes == 12 && dia <= 21))
    {
        cout << "Su signo del zodiaco es ---> Sagitario" << endl;
    }

    else if ((mes == 12 && dia >= 22) || (mes == 1 && dia <= 20))
    {
        cout << "Su signo del zodiaco es ---> Capricornio" << endl;
    }

    else 
    {
        cout << "Error: Ingresaste dia o mes invalido" << endl;
        return 0;
    }


    // Preguntamos al usuario si es que le gusta festejar su cumpleaños
    cout << "\nLe gusta festejar su cumple? (Si / No): ";
    cin >> FestejoCumple;

    if (FestejoCumple == "Si" || FestejoCumple == "si" || FestejoCumple == "SI")
    {
        cout << "Que Bueno!" << endl;
    }

    else if (FestejoCumple == "No" || FestejoCumple == "no" || FestejoCumple == "NO")
    {
        cout << "Que Lastima" << endl;
    }

    else
    {
        cout << "Vuelva a intenatr ingresando valores correctos (Si-No)" << endl; 
    }


    // Preguntar al usuario cuantos invitados va a invitar
    cout << "\nCuantos invitados van a asistir a tu cumple?: ";
    cin >> invitados;

    total_invitados = round(sqrt(pow(invitados,4)));
    cout << "El total de invitados a tu cumple va hacer de: " << total_invitados;
    

    return 0;
}