#include <iostream>
#include <cmath>
using namespace std;

int main(){
    const float pi = 3.14;
    double radio, perimetro, area;

    cout << "Ingrese el radio de un circulo para calcular el PERiMETRO y AREA: ";
    cin >> radio;

    perimetro = ((2 * pi) * radio);
    area = (pi * pow(radio,2));   //Asi es para poner radio al cuadrado

    cout << "El perimetro del radio que ingresaste: " << radio << " es de ---> " << perimetro << endl;
    cout << "Y el area del radio que ingresaste: " << radio << " es de ---> " << area;

    return 0;
}