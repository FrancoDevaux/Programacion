## Ejercicio 2 - Turno 1: Granja vertical
### Explicación breve del código

Este sistema modela el funcionamiento de una granja vertical. El sistema permite **agregar cultivos** y **obtener métricas** de la granja (producción total, costos, etc.) de forma **tipada, pura y testeable**. La granja se compone de **cultivos**. Cada cultivo expone comportamientos de **producción mensual** y **costo operativo mensual**.

* **Clases/archivos (rol):**

  * `GranjaVertical`: administra la colección de cultivos y ofrece operaciones agregadas (p. ej., sumar producciones).
  * `GranjaVerticalExtendida`: extiende a `GranjaVertical` añadiendo cálculos adicionales.
  * `Cultivo` (contrato) y concretos como `Lechuga`, `Tomate`: encapsulan lógica de cada cultivo (p. ej., `calcularProduccionMensual()` y `calcularCostoOperativo()`).
.


### a) Implementar la nueva funcionalidad

Implementar en `GranjaVerticalExtendida` el método:

```ts
calcularRentabilidad(): number
```

**Ayuda: usar lo que ya existe y `reduce`...**

* `produccionAnual = suma(12 * cultivo.calcularProduccionMensual())`
* `costoAnual      = suma(12 * cultivo.calcularCostoOperativo())`
* `rentabilidad    = produccionAnual / costoAnual`

### b) **TDD** mínimo obligatorio

Escribir antes un test que pueda:

   * Crear 2 cultivos reales (p. ej. `Tomate`, `Lechuga`), agregados a `GranjaVerticalExtendida`.
   * Esperar un valor numérico correcto. Usar `toBeCloseTo`:

  > `toBeCloseTo`
  > Type: (value: number, numDigits?: number) => Awaitable<void>
  >
  > Usar toBeCloseTo para comparar números de punto flotante. El argumento opcional `numDigits` limita el número de dígitos que se verifican después del punto decimal.
  

