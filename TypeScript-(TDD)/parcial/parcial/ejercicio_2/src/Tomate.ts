import { IRendimiento } from "./iRendimiento";
import { Cultivo } from "./Cultivo";

export class Tomate extends Cultivo {
  constructor(id: number, nombre: string, diasDesdeSiembra: number = 0) {
    super(id, nombre, diasDesdeSiembra);
  }

  getTipoCultivo(): string {
    return "Tomate - Ciclo Medio";
  }
  
  calcularProduccionMensual(): number {
    return 4; // Los tomates producen 4 kg por mes
  }
  
  calcularCostoOperativo(): number {
    return 120; // El costo operativo de los tomates es $120 por mes
  }
}