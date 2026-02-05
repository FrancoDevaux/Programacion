export abstract class Herramienta {
  constructor(public nombre: string) {}

  costoAlquiler(dias: number): number {
    if (dias <= 0) {
      throw new Error("dias debe ser mayor que 0");
    }
    return this.costoBase() + this.recargoPorDia() * dias + this.depositoReembolsable();
  }


  protected abstract costoBase(): number;
  protected abstract recargoPorDia(): number;
  protected abstract depositoReembolsable(): number;

  
  descripcion(dias: number): string {
    const costo = this.costoAlquiler(dias);
    return `${this.nombre}: $${costo} por ${dias} día(s)`;
  }
}