#include <iostream>
#include <cmath>
using namespace std;

int main(){
    const float pi = 3.14;
    double parametro, seno, coseno, tangente;

    cout << "Ingrese un numero ENTERO para sacarle el (cos,tan,sin): ";
    cin >> parametro;

    seno = sin(parametro * (pi/180));
    coseno = cos(parametro * (pi/180));
    tangente = tan(parametro * (pi/180));

    cout << "El seno de " << parametro << " es de: " << seno << endl;
    cout << "El coseno de " << parametro << " es de: " << coseno << endl;
    cout << "La tengente de " << parametro << " es de: " << tangente;

    return 0;

}