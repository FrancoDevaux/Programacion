#include <iostream>
#include <cmath>
using namespace std;

int main(){
    int x1, x2, y1, y2;
    double distancia;

    cout << "Ingrese un numero para x1: ";
    cin >> x1;
    cout << "Ingrese un numero para y1: ";
    cin >> y1;
    cout << "Ingrese un numero para x2: ";
    cin >> x2;
    cout << "Ingrese un numero para y2: ";
    cin >> y2;
    
    distancia = sqrt(pow((x2 - x1), 2) + pow((y2 - y1), 2));
    
    cout << "La distancia entre los numeros en un plano cartesiano es de ---> " << distancia;
    return 0;

}