#include <iostream>
#include <cmath>
using namespace std;
int main(){
    const float pi = 3.14;
    double Grados_a_Radianes, grados;

    cout << "ingrese un numero para pasarlo a radianes: ";
    cin >> grados;

    Grados_a_Radianes = (grados * (pi/180));

    cout << "El numero ingresado en grados que es: " << grados << " a radianes quedaria en ---> " << Grados_a_Radianes;
    return 0;
}