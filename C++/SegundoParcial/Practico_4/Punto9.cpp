#include <iostream>

using namespace std;

int main(){

    int lado;

    cout << "\nIngrese un lado: ";
    cin >> lado;

    for (int fila = 1; fila <= lado; fila++)
    {
        for (int columna = 1; columna <= lado; columna++)
        {
            cout << "* \t";
        }
        cout << endl;
    }

    return 0;

}