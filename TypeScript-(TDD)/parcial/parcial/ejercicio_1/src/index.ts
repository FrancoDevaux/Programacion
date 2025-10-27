// Generado a partir del enunciado en Markdown.
// Regla general: para cada ejercicio que produzca un resultado, imprimir:
// console.log('ejercicioN:', resultado)  // reemplazar N por el número de ejercicio

/***********************
 *  Datos base comunes *
 ***********************/
type ID = string;

const personas = [
  { id: 'p1', nombre: 'Ana',   edad: 28 },
  { id: 'p2', nombre: 'Luis',  edad: 41 },
  { id: 'p3', nombre: 'Sofía', edad: 33 },
] as const;

const productos = [
  { sku: 'A1', nombre: 'Cuaderno',  precio: 1200,  categoria: 'libreria', stock: 10 },
  { sku: 'B2', nombre: 'Lápiz',     precio: 200,   categoria: 'libreria', stock: 0  },
  { sku: 'C3', nombre: 'Botella',   precio: 3500,  categoria: 'hogar',    stock: 5  },
  { sku: 'D4', nombre: 'Taza',      precio: 2200,  categoria: 'hogar',    stock: 12 },
] as const;

const movimientos = [
  { cuenta: 'caja',   tipo: 'ingreso',  monto: 1500 },
  { cuenta: 'banco',  tipo: 'egreso',   monto:  700 },
  { cuenta: 'caja',   tipo: 'ingreso',  monto:  900 },
  { cuenta: 'banco',  tipo: 'ingreso',  monto: 3200 },
  { cuenta: 'caja',   tipo: 'egreso',   monto:  300 },
] as const;

const pedidos = [
  { id: 'o1', items: [{ sku: 'A1', qty: 2 }, { sku: 'B2', qty: 5 }] },
  { id: 'o2', items: [{ sku: 'D4', qty: 1 }] },
  { id: 'o3', items: [{ sku: 'C3', qty: 3 }, { sku: 'A1', qty: 1 }] },
] as const;

const clientes = [
  { id: 'c1', nombre: 'Club Norte' },
  { id: 'c2', nombre: 'Asoc. Sur'  },
] as const;

const ventas = [
  { id: 'v1', clienteId: 'c1', items: [{ sku: 'A1', qty: 3 }, { sku: 'D4', qty: 2 }] },
  { id: 'v2', clienteId: 'c2', items: [{ sku: 'C3', qty: 1 }] },
  { id: 'v3', clienteId: 'c1', items: [{ sku: 'A1', qty: 1 }, { sku: 'B2', qty: 10 }] },
] as const;

/********************************
 *  Ejercicio 1
 *  Unir los siguientes arrays en uno solo y devolverlo ordenado ascendente SIN duplicados
 *******************************/
const a1 = [5, 2, 9, 5, 1];
const a2 = [3, 9, 4, 1, 8];
const a3 = [6, 2, 7, 3];

// TODO: Crear una función/expresión que una a1, a2 y a3, quite duplicados y ordene ascendente.
/*
  Sugerencia (opcional):
  - Usar el operador spread ... para concatenar
  - Usar Set para eliminar duplicados
  - Usar sort((a,b) => a - b) para ordenar números asc
*/

const resultado1 = [...new Set([...a1, ...a2, ...a3])].sort((a, b) => a - b);
console.log('ejercicio1:', resultado1);

/********************************
 *  Ejercicio 2
 *  Diccionario por id (sin duplicados)
 *  A partir de `personas`, generar un diccionario { [id]: persona }.
 *  Si se encuentra un id duplicado, lanzar un Error. No mutar `personas`.
 *******************************/

type Persona = typeof personas[number];

// TODO: Implementar la función. Si hay ids repetidos, lanzar Error.
function personasPorId(lista: readonly Persona[]): Record<ID, Persona> {
  const diccionario: Record<ID, Persona> = {};
  
  for (const persona of lista) {
    if (diccionario[persona.id]) {
      throw new Error(`el ID es duplicado ${persona.id}`);
    }
    diccionario[persona.id] = persona;
  }
  
  return diccionario;
}

const resultado2 = personasPorId(personas);
console.log('ejercicio2:', resultado2);

/********************************
 *  Ejercicio 3
 *  Join interno productos×pedidos (por sku)
 *  Generar un array de objetos { sku, nombreProducto, totalPedidos }
 *  con el total de unidades pedidas por sku en todos los pedidos.
 *  Incluir solo los sku que existan en `productos`.
 *******************************/

type Producto = typeof productos[number];
type Pedido   = typeof pedidos[number];
type ResumenPedido = { sku: string; nombreProducto: string; totalPedidos: number };

// TODO: Implementar la función de join/agrupación por sku.
function resumenPedidos(productos: readonly Producto[], pedidos: readonly Pedido[]): ResumenPedido[] {
  const totalesPorSku: Record<string, number> = {};

  for (const pedido of pedidos) {
    for (const item of pedido.items) {
      if (totalesPorSku[item.sku]) {
        totalesPorSku[item.sku] += item.qty;
      } else {
        totalesPorSku[item.sku] = item.qty;
      }
    }
  }

  const resultado = productos
    .filter(producto => totalesPorSku[producto.sku] !== undefined)
    .map(producto => ({
      sku: producto.sku,
      nombreProducto: producto.nombre,
      totalPedidos: totalesPorSku[producto.sku]
    }));

  return resultado;
}

const resultado3 = resumenPedidos(productos, pedidos);
console.log('ejercicio3:', resultado3);

export {
  personas, productos, movimientos, pedidos, clientes, ventas,
  a1, a2, a3,
  personasPorId, resumenPedidos
};