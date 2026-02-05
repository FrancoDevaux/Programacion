import { Herramienta } from "./herramienta";

export class Taladro extends Herramienta {
  costoBase(): number {return 1000}

  recargoPorDia(): number {return 300}

  depositoReembolsable(): number {return 0}
}