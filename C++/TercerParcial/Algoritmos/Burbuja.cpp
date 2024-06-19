//Ordenacion de vectores
//Metodo de la burbuja
#include<iostream>
using namespace std;

void burbuja();


int main()
{
    burbuja();
    return 0;
}

void burbuja()
{
 int n = 7;
    int i,j,temp,a[n] = {2,3,1,4,7,8,3};
    for (i = 0; i < n-1; ++i){  //Recorre el arreglo
        for (j = 0; j < n-1; ++j){  //Agarra y entra en cada possicion del arreglo
            if (a[j] > a[j+1]){ //La siguiente por eso j+1 de forma ascendente por el mayor, si pondra < seria descendte
                temp = a[j]; 
                a[j] = a[j+1];
                a[j+1] = temp;
            }
        }
    }
    for (i = 0; i < n; ++i){
        cout<< a[i] <<endl;
    }

   } 