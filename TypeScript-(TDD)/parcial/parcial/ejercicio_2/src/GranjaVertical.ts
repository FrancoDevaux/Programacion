import { Cultivo } from "./Cultivo";

export class GranjaVertical {
  protected cultivos: Cultivo[] = [];

  agregarCultivo(cultivo: Cultivo): void {
    this.cultivos.push(cultivo);
  }

}