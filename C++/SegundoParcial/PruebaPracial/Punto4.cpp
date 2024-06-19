#include <iostream>
#include <cstdlib>
#include <ctime>

using namespace std;

int main(){

    srand(time(NULL));
    int arreglo[10], numeroRandom, cantidad = 0;
    bool encontrado = false;

    for (int i = 0; i < 10; i++){
        numeroRandom = rand() % 10;
        arreglo[i] = numeroRandom;
        cout << numeroRandom << ",";
    }
    cout << endl;

    for (int i = 0; i < 10; i++){
        if (arreglo[i] == 8){
            cout << "encontrado\n";
            encontrado = true;
        }
        if (encontrado){
            break;
        }
    }
    if (encontrado){
        for (int i = 0; i < 10; i++){
            if (arreglo[i] == 8){
                cantidad++;
            }
        }
        //cout << "La cantidad total de encontrados es de --> " << cantidad << " veces" << endl;
    }

    cout << "La cantidad total de num8 encontrados es de --> " << cantidad << " veces" << endl;

    return 0;

}
