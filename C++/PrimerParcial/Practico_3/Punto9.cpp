#include <iostream>

using namespace std;

int main(){

    double salario, aumento;

    cout << "Indique tu salario mensual: $";
    cin >> salario;

    if (salario < 60000){
        aumento = (salario * 0.2);
        aumento = (salario + aumento);
        cout << "Ahora tu salario sera de ---> $" << aumento;
    }
    else if (salario >= 60000 && salario < 100000){
        aumento = (salario * 0.1);
        aumento = (salario + aumento);
        cout << "Ahora tu salario sera de ---> $" << aumento;
    }
    else if (salario >= 100000 && salario < 150000){
        aumento = (salario * 0.05);
        aumento = (salario + aumento);
        cout << "Ahora tu salario sera de ---> $" << aumento;
    }
    else{
        aumento = (salario * 0.03);
        aumento = (salario + aumento);
        cout << "Ahora tu salario sera de ---> $" << aumento;
    }

    return 0;
}