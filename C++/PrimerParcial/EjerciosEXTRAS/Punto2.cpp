#include <iostream>
#include <cmath>

using namespace std;

int main (){

    const double pi = 3.14159;
    int vueltas, cuadrante;
    double seno, coseno, tangente, radianes, grados;

    cout << "\nIngrese un valor de un angulo en (grados): ";
    cin >> grados;

    radianes = (grados * (pi/180));

    cout << "\nEl angulo ingresados en radianes es de ---> " << radianes << endl;

    if (grados > 360)
    {
        vueltas = (grados / 360);
        cuadrante = ((int)grados / 90) % 4;

        cout << "\nEl angulo dio " << vueltas << " vueltas." << endl;
        cout << "\nSe encuentra en el cuadrante " << cuadrante + 1 << ".\n" << endl;
    }
    else 
    {
        seno = sin(radianes);
        coseno = cos(radianes);
        tangente = tan(radianes);

        cout << "\nEl seno es de: " << seno << ", el coseno es de: " << coseno << " y la tangente es de: " << tangente << endl;

    }

    return 0;

    
}