import { Herramienta } from "./herramienta";

export class Amoladora extends Herramienta {
  costoBase(): number {return 1200}

  recargoPorDia(): number {return 250}

  depositoReembolsable(): number {return 0}
}