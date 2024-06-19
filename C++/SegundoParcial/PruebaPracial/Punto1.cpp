#include <iostream>

using namespace std;

int main(){

    //VARIABLES
    int opcion, iluminacion, salir, opcion3;
    double temperatura;
    bool riego = false;
    string respuesta;

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
                (riego) ? cout << "\nEl riego esta actualmente prendidio\n":cout << "El riego esta apagado\n";

                do{
                    cout << "Para cambiar el riego presiona 1, sino 0: ";
                    cin >> opcion3;
                }while (opcion3 !=1 && opcion3 !=0);
                    
                if (opcion3 == 1){
                    riego = !riego;
                    (riego) ? cout << "Ahora esta prendido\n":cout << "Apagado\n";
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