#include <iostream>
#include <cmath>

using namespace std;

int main(){

    double numero;

    cout << "\bIngrese un numero (entero o con decimal): ";
    cin >> numero;

    if (trunc(numero) == numero)
    {
        cout << "\nEl numero " << numero << " es ENTERO." << endl;
    }
    else
    {
        cout << "\nEl numero " << numero << " NO es entero." << endl;
    }

    return 0;

}