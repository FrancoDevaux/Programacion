#include <iostream>

using namespace std;

int main(){

    //VARIABLES
    int opcion, iluminacion;
    double temperatura;
    bool riego = false;
    int respuesta;

    do {
        cout << "\n1 - Controlar la temperatura\n";
        cout << "2 - Controlar la iluminacion\n";
        cout << "3 - Controlar el riego\n";
        cout << "4 - Salir del programa\n";
        cout << "Ingrese una opcion (1-2-3-4): ";
        cin >> opcion;

        switch (opcion){
            case 1:{
                do {
                    cout << "\nIngrese temperatura (entre 17.9 y 24.5): ";
                    cin >> temperatura;
                } while(temperatura < 17.9 || temperatura > 24.4);
                cout << "Temperatura indicada a ---> " << temperatura << " grados." << endl;
                break;
            }
            case 2:{
                do {
                    cout << "\nIngrese la intensidad de iluminacion (entre 0 y 100): ";
                    cin >> iluminacion;
                } while(iluminacion < 0 || iluminacion > 100);
                cout << "Iluminacion regulada a ---> " << iluminacion << "% de intensidad" << endl;
                break;
            }
            case 3:{
                if (riego){
                    cout << "\nRiego actualmente activado. Desea desactivarlo? 1-->para si, 0-->para no (1 / 0 ): ";
                    cin >> respuesta;

                    if (respuesta == 1){
                        riego = false;
                        cout << "\nRiego desactivado.\n";
                    }
                    else if (respuesta == 0){
                        riego = true;
                        cout << "\nRiego activado\n";
                    }
                    else {
                        cout << "\n[!]Caracter INVALIDO\n";
                    }
                }
                else{
                    cout << "\nRiego actualmente desactivado. Desea activarlo? Presiona 1-Cambiarlo, 0-Queda igual -> (1 / 0 ): ";
                    cin >> respuesta;

                    if (respuesta == 1){
                        riego = true;
                        cout << "\nRiego activado.\n";
                    }
                    else if (respuesta == 0)
                    {
                        riego = false;
                        cout << "\nRiego desactivado\n";
                    }
                    else{
                        cout << "\n[!]Carcater INVALIDO\n";
                    }
                    
                }
                break;
            }
            case 4:{
                cout << "[!]Saliendo del programa..." << endl;
                break;
            }
            default:{
                cout << "[!]Opcion invalida" << endl;
            }
        }
    }while (opcion != 4);
    return 0;
}