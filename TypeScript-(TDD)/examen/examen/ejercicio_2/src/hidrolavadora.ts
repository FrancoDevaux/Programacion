import { Herramienta } from "./herramienta";

export class Hidrolavadora extends Herramienta {
  costoBase(): number {return 1500}

  recargoPorDia(): number {return 400}
  
  depositoReembolsable(): number {return 2000}
}