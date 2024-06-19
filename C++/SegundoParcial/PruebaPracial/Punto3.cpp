#include <iostream>

using namespace std;

int main(){
    
    //PUNTO A)
    int numero;
    while(true){
        cout << "\nIntroduce un numero entre (0/100): ";
        cin >> numero;

        if (numero > 0 && numero <= 100){
            cout << "Elegiste el numero ---> " <<  numero << endl;
            break;
        }
    }
    
    //PUNTO B)1
    for (int i =0; i <= 100; i+=10){
        cout << i << ",";
    }
    cout << endl << endl;
    
    cout << "Incrementar el Inidice del bucle\n";
    //PUNTO B)2
    int suma = 0; 
    int arreglo[11];
    int contador = 0;
    for (int i = 0; i <=100; i+=10){
        suma += i;
        arreglo[contador] = suma;
        contador++;
    }
    for (int i = 0; i <= 10; i++){
        cout << arreglo[i] << ",";
    }
    cout << endl << endl;

    //PUNTO C
    cout << "Esta es la suma: " << suma << endl;
    cout << "El numero total del contador saltando en diez posiciones hasta 100 es: " << contador << endl;

    return 0;

}