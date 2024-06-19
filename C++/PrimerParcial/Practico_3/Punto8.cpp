#include <iostream>

using namespace std;

int main(){

    int dia, mes, numero;

    /*cout << "Ingrese dia y mes: "
    cin >>dia>>mes;*/

    cout << "Ingrese un DIA del anio: ";
    cin >> dia;
    cout << "Ingrese un MES del anio: ";
    cin >> mes;

    switch (mes){

        case 1:
            cout << "Estamos en el dia ---> " << dia;
            break;
        
        case 2:
            cout << "Estamos en el dia ---> " << dia+31;
            break;

        case 3:
            cout << "Estamos en el dia ---> " << dia+59;
            break;

        case 4:
            cout << "Estamos en el dia ---> " << dia+90;
            break;

        case 5:
            cout << "Estamos en el dia ---> " << dia+120;
            break;

        case 6:
            cout << "Estamos en el dia ---> " << dia+151;
            break;

        case 7:
            cout << "Estamos en el dia ---> " << dia+181;
            break;

        case 8:
            cout << "Estamos en el dia ---> " << dia+212;
            break;

        case 9:
            cout << "Estamos en el dia ---> " << dia+243;
            break;

        case 10:
            cout << "Estamos en el dia ---> " << dia+273;
            break;

        case 11:
            cout << "Estamos en el dia ---> " << dia+304;
            break;

        case 12:
            cout << "Estamos en el dia ---> " << dia+334;
            break;

        default:
            cout << "Ingresaste una fecha INVALIDA! ";
            break;

            
        return 0;



    }
}