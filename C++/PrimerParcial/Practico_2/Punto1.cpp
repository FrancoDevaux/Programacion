#include <iostream>
#include <cmath>
using namespace std;

int main()
{
    float numero;
    double raiz;

    cout << "Ingrese un numero para sacar la raiz de: ";
    cin >> numero;

    if (numero < 0)
    {
        cout << "Por favor ingrese un numero POSITIVO: ";
        cin >> numero;
        raiz = sqrt(numero);
        cout << "La raiz es de: " << raiz;
    }
    
    else
    {
        raiz = sqrt(numero);
        cout << "La raiz del numero es de: " << raiz;
    }
    
  
    return 0;
}
