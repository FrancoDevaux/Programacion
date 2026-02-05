import { Herramienta } from "./herramienta";

export function reporteAlquiler(herramientas: Herramienta[], dias: number): string {
  let total = 0;
  let resultado = "";

  for (const herramienta of herramientas) {
    const descripcion = herramienta.descripcion(dias);
    resultado += descripcion + "\n";
    total += herramienta.costoAlquiler(dias);
  }

  resultado += `TOTAL: $${total}`;
  return resultado;


  /**Otra forma de hacerlo:
   * export function reporteAlquiler(herramientas: Herramienta[], dias: number): string {
   *   let total = 0
  const lineas = herramientas.map(h => {const linea = h.descripcion(dias) total += h.costoAlquiler(dias)
    return linea
  })
  lineas.push(`TOTAL: $${total}`)
  return lineas.join("\n")
}
   */
}