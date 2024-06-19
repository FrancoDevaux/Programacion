#include <iostream>
using namespace std;


// OTRA FORMA DE HACER EL PUNTO 8 


int main(){

    int Enero, Febrero, Marzo, Abril, Mayo, Junio, Julio, Agosto, Septiembre, Octubre, Noviembre, Diciembre;
    int dia, mes;

    cout << "Ingrese un dia del anio: ";
    cin >> dia;
    cout << "Ingrese un mes del anio: ";
    cin >> mes;

    Enero = 31;
    Febrero = 28;
    Marzo = 31;
    Abril = 30;
    Mayo = 31;
    Junio = 30;
    Julio = 31;
    Agosto = 31;
    Septiembre = 30;
    Octubre = 31;
    Noviembre = 30;
    Diciembre = 31;


    switch (mes)
        case 1:
            cout << "Estamos en el dia " << dia;
            break;

        case 2:
            cout << "Estamos en el dia " << dia+Enero;
            break;

        case 3:
            cout << "Estamos en el dia " << dia+Enero+Febrero;
            break;

        case 4:

}