import { IRendimiento } from "./iRendimiento";

export abstract class Cultivo implements IRendimiento {
  protected id: number;
  protected nombre: string;
  protected diasDesdeSiembra: number;
  protected nivelAgua: number;

  constructor(id: number, nombre: string, diasDesdeSiembra: number) {
    this.id = id;
    this.nombre = nombre;
    this.diasDesdeSiembra = diasDesdeSiembra;
    this.nivelAgua = 100;
  }
  calcularProduccionMensual(): number {
    throw new Error("Method not implemented.");
  }
  calcularCostoOperativo(): number {
    throw new Error("Method not implemented.");
  }

  abstract getTipoCultivo(): string;

  getId(): number { return this.id; }
  getNombre(): string { return this.nombre; }
  getDiasDesdeSiembra(): number { return this.diasDesdeSiembra; }
  

}