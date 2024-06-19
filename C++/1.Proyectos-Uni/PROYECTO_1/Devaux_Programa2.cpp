#include <iostream>


using namespace std;

int main(){

    // Variables
    int dia, mes;

    //Ingresa el dia y mes que quiera
    cout << "\nIngrese el DIA de nacimiento: ";
    cin >> dia;
    cout << "Ingrese el MES de nacimiento (1-12): ";
    cin >> mes;


    // Uso de la herramienta SWITCH CASE para saber el signo zodiacal
    switch (mes){
        case 1:
            if (dia >= 21){
                cout << "\nTu signo zodiacal es ---> Acuario\n" << endl;
            }
            else {
                cout << "\nTu signo zodiacal es ---> Capricornio\n" << endl;
            }
            break;

        case 2:
            if (dia <= 19)
            {
                cout << "\nTu signo zodiacal es ---> Acuario\n" << endl;
            }
            else
            {
                cout << "\nTu signo zodiacal es ---> Piscis\n" << endl;
            }
            break;                     
        
        case 3:
            if (dia <= 20)
            {
                cout << "\nTu signo zodiacal es ---> Piscis\n" << endl;
            }
            else
            {
                cout << "\nTu signo zodiacal es ---> Aries\n" << endl;
            }
            break;

        case 4:
            if (dia <= 19)
            {
                cout << "\nTu signo zodiacal es ---> Aries\n" << endl;
            }
            else
            {
                cout << "\nTu signo zodiacal es ---> Tauro\n" << endl;
            }
            break;

        case 5:
            if (dia <= 20)
            {
                cout << "\nTu signo zodiacal es ---> Tauro\n" << endl;
            }
            else
            {
                cout << "\nTu signo zodiacal es ---> Geminis\n" << endl;
            }                
            break;

        case 6:
            if (dia <= 21)
            {
                cout << "\nTu signo zodiacal es ---> Geminis\n" << endl;
            }
            else
            {
                cout << "\nTu signo zodiacal es ---> Cancer\n" << endl;
            }
            break;

        case 7:
            if (dia <= 22)
            {
                cout << "\nTu signo zodiacal es ---> Cancer\n" << endl;
            }
            else
            {
                cout << "\nTu signo zodiacal es ---> Leo\n" << endl;
            }
            break;

        case 8:
            if (dia <= 23)
            {
                cout << "\nTu signo zodiacal es ---> Leo\n" << endl;
            }
            else
            {
                cout << "\nTu signo zodiacal es ---> Virgo\n" << endl;
            }
            break;

        case 9:
            if (dia <= 22)
            {
                cout << "\nTu signo zodiacal es ---> Virgo\n" << endl;
            }
            else
            {
                cout << "\nTu signo zodiacal es ---> Libra\n" << endl;
            }
            break;

        case 10:
            if (dia <= 22)
            {
                cout << "\nTu signo zodiacal es ---> Libra\n" << endl;
            }
            else
            {
                cout << "\nTu signo zodiacal es ---> Escorpio\n" << endl;
            }
            break;

        case 11:
            if (dia <= 22)
            {
                cout << "\nTu signo zodiacal es ---> Escorpio\n" << endl;
            }
            else
            {
                cout << "\nTu signo zodiacal es ---> Sagitario\n" << endl;
            }
            break;

        case 12:
            if (dia <= 21)
            {
                cout << "\nTu signo zodiacal es ---> Sagitario\n" << endl;
            }
            else
            {
                cout << "\nTu signo zodiacal es ---> Capricornio\n" << endl;
            }
            break;

        default:
            cout << "\n\tIngresaste un numero INVALIDO!\n" << endl;


    }

}