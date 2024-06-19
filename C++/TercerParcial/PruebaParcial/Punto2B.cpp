//Punto 2.b)

/*
Mencionar en que consiste el metodo de ordenacion por Inserccion.
¿Cual es la diferencia con el metodo de ordenacion por Seleccion Directa?
*/

/*
RTA:

---------------------------------------INSERCCION-----------------------------------------------
. Declaramos una variable pos que almacena la posición actual y la variable aux que almacena el valor actual.
- Lo que hace el de INSERCCION es: Nos paramaos en el 2 elemento (posición 1) y lo comparamos con el de la izquierda 
(dependiendo cm lo queramos ordenar) y compara si el elemento 2 (en la posición 1) es  menor que el de la izquierda,
si la respuesta es verdeara, el numero en la posición 0 se desplaza hacia la derecha, 
a la posición se le resta 1 y al salir del while como no tiene otro a la izquierda reemplaza el valor en la posición 0 
por el auxiliar y así sucesivamente, entrando al while si pos es mayor que cero y arreglo en pos-1 es mayor a aux. 
Si el de la izquierda es mayor que el de la derecha hacemos el intercambio (EXPLICACION  DE FORMA ASCENDNETE)

-------------------------------------SELECCION DIRECTA--------------------------------------------
Selecciona el primer valor como si fuera el menor, luego recorre el array donde compara si es menor que el otro 
y si no es el menor verdadero lo va a reemplazar.
.Cuenta con 2 for, el primero llega hasta n-1 porque se supone que el ultimo numero queda ordenado, 
usa variables para guardar el menor, etc.

- Lo que haces es buscar el numero mas chico del arreglo y lo pone en la primera posición (si lo queremos de forma ASCENDNETE)
, sino busca por el numero mas grande, y al arreglo lo recorre con 2 bucles for, 
el primer for va desde el primer lugar hasta el anteúltimo y el segundo for va desde el lugar que esta en el primer for +1
hasta el final.
- Este tamb crea una variable temporal dentro de un if, si menor es mayor a i.

*/

