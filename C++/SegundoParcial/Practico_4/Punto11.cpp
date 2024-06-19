#include <iostream>

using namespace std;

int main(){
    
    int lado;

    cout << "\nIngrese lado de la matriz: ";
    cin >> lado;

    if (lado <= 0) {
        cout << "[!]Error: El numero debe ser positivo." << endl;
        return 1;
    }

    for (int i= 1;i<=lado;i++){
        for (int j= 1;j<=lado;j++){
            if (i==j){
                cout << j << " ";
            } else cout << 0 << " ";
    }  
    cout << endl;   
    } 
    return 0;


}