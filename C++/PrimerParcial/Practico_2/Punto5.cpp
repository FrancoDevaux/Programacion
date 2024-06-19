#include <iostream>
#include <cmath>
using namespace std;

int main (){
    double Cateto1, Cateto2, ResultadosCatetos, hipotenusa;

    cout << "Ingrese el lado del primer cateto de un triangulo rectangulo: ";
    cin >> Cateto1;
    cout << "Ingrese el lado del segundo cateto de un triangulo rectangulo: ";
    cin >> Cateto2;

    ResultadosCatetos = (pow(Cateto1,2) + pow(Cateto2,2));
    hipotenusa = sqrt(ResultadosCatetos);

    cout << "La hipotenusa del trinagulo rectangulo es de ---> " << hipotenusa;
    
    return 0;
}