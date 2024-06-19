/*Escribir un programa que calcule el área de un triángulo o de un rectángulo dependiendo
que quiera el usuario (el usuario decide cuál de los dos debe calcular). Luego debe pedir que
ingrese la altura y la base del mismo y devolver el resultado del área.*/

#include <iostream>
#include <cmath>

using namespace std;

int main(){

    int respuesta, area_trinagulo, area_rectangulo;
    int base, altura;

    cout << "\nTenes estas opciones " << "\n1 ---> Area de un tringulo" << "\n2 ---> Area de un rectangulo" << "\nOpcion: "<< endl;
    cin >> respuesta;
    
    switch (respuesta){

        case 1:
            cout << "Ingrese la altura del triangulo: ";
            cin >> altura;
            cout << "Ingrese la base del triangulo: ";
            cin >> base;

            area_trinagulo = ((base * altura) / 2);
            cout << "\nEl area del triangulo es ---> " << area_trinagulo << endl;
            break;

        case 2:
            cout << "Ingrese la altura del rectangulo: ";
            cin >> altura;
            cout << "Ingrese la base del rectangulo: ";
            cin >> base;

            area_rectangulo = (base * altura);
            cout << "\nEl area del rectangulo es ---> " << area_rectangulo << endl;
            break;

        default:
            cout << "Ingresaste una opcion INVALIDA!";
            break;

        return 0;
    }










    return 0;



}