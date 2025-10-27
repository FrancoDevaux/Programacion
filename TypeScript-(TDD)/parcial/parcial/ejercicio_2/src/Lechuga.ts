import { IRendimiento } from "./iRendimiento";
import { Cultivo } from "./Cultivo";

export class Lechuga extends Cultivo {
  constructor(id: number, nombre: string, diasDesdeSiembra: number = 0) {
    super(id, nombre, diasDesdeSiembra);
  }

  getTipoCultivo(): string {
    return "Lechuga - Ciclo Corto";
  }

  calcularProduccionMensual(): number {
    return 2; // 2 kg por mes
  }

  calcularCostoOperativo(): number {
    return 50; // $50 por mes
  }
}
