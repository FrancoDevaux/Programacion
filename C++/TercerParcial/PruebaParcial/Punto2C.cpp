// Punto 2.c)

/*
Mencione que algoritmo de busqueda podria implementar y como funcionan
¿Cuales son sus diferencias?, ¿Cual busca mas rapido?, ¿Por que?.
*/

/*
RTA:

Seria la binaria porque si esta ordenado el arreglo, vos vas a la mitad, de una descartas la mitad de los valores 
siendo mayor o menor va para el lado correspondiente, ahi volves a descartar la mitad y siempre vas descartando la mitad 
haciendo muchos menos pasos que la búsqueda secuencial que pasa por todos los valores.

Si el arreglo esta desordenado no es tan eficiente el búsqueda binaria porque puede pasar que tengas que recorrer 
todos lo números que haya en el array.

En si el concepto de la búsqueda binaria es ir partiendo las mitades del arreglo y compara con el numero que ingresa el 
usuario y va comprando con los if y la variable mitad siempre va a ser igual 
a ((primero = 0; + ultimo = dependiendo el array (que seria el anteúltimo porque se empieza del cero contando) 
todo dividido 2)) y si da con coma la parte decimal se va ya que mitad es de tipo entero.

Dependiendo en que if entra y si el arreglo esta ordenado de forma ascendente o descendente, 
está de la mitad para la izquierda o para la derecha, descartando que mitad ya no vas a buscar haciéndolo mas eficiente 
y hasta que no encuentre el valor que el usuario quiera buscar vuelve a entrar en el bucle while actualizando el INDICE.
Va actualizando los indices y va a encontrar el elemento cuando este en el primer if en caso de que el numero ingresado 
sea == al array[mitad] sino no.

*/