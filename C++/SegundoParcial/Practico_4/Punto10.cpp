#include <iostream>

using namespace std;

int main(){

    int lado;

    cout << "\nIngrese el lado de la matriz: ";
    cin >> lado;

    for (int filas = 1; filas <= lado; filas++)
    {
        for (int columnas = 1; columnas <= lado; columnas++)
        {
           if (filas==1 || columnas==1 || filas==lado || columnas==lado ) 
           {
                cout <<" * ";
           } 
           else
           {
                cout <<"   "; 
           } 
             
    
        }
    }   cout << endl << endl;
        
    return 0;

    
}