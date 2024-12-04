"""Un almacén guarda los códigos, los nombres de los productos y sus precios,
respectivamente, separados por punto y coma ( ; ) en el archivo productos.txt. Hacer
un algoritmo y luego los procedimientos necesarios que permitan tomar los datos del
archivo y buscar el precio de un artículo ingresado por teclado. Para probar el
algoritmo crear un archivo “productos.txt” y cargarle datos al estilo:
100;arroz;10
102;fideos;5
135;lentejas;8
138;porotos;6
140;sal gruesa;5
201;aceite;20 ( etc… )
"""

def leer_txt(archivo, codigo):

    #Se crea un diccionario vacío llamado productos. Este diccionario almacenará los códigos de los productos como claves 
    # y sus precios correspondientes como valores.
    productos = {}
    with open (archivo, 'r') as f:
        for linea in f:

            #Se divide la línea en tres partes (código, nombre y precio) separadas por el carácter ';'. 
            # Los valores se asignan a las variables correspondientes.
            codigoActual, nombre, precio = linea.strip().split(';')
            #Este método divide la cadena (que ya ha sido limpiada con strip()) en una lista de subcadenas, 
            # utilizando el carácter ';' como separador. 



            #Se agrega una nueva entrada al diccionario productos. La clave es el codigo_actual 
            # y el valor es el precio convertido a un número de punto flotante.
            productos[codigoActual] = float(precio)

        
    #Se busca el código proporcionado en el diccionario productos y se devuelve el precio correspondiente. 
    # Si el código no se encuentra, se devuelve None
    return productos.get(codigo)
    
archivo = "C:/Users/FRANCO/Desktop/Python3/PrimerParcial/Practico 2/productos.txt"
buscarCodigo = input("\nIngrese el codigo del producto: ")

#Se llama a la función leer_txt para obtener el precio del producto con el código ingresado.
precio = leer_txt(archivo, buscarCodigo)


#Si se encontró el producto (es decir, precio no es None), se imprime el precio.
if precio is not None:
    print(f"\nEl precio del producto {buscarCodigo} es: ${precio}")
else:
    print("\n[-]Producto ni encontrado")