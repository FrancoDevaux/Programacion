import { Cultivo } from "./Cultivo";
import { IRendimiento } from "./iRendimiento";
import { GranjaVertical } from "./GranjaVertical";
import { Tomate } from "./Tomate";

export class GranjaVerticalExtendida extends GranjaVertical {
    calcularProduccionTotal(): number {
        return this.cultivos.reduce(
            (accum, c) => accum + 12 * c.calcularProduccionMensual(), 0);
    }

    calcularRentabilidad(): number {
        const produccionAnual = this.cultivos.reduce(
            (accum, c) => accum + 12 * c.calcularProduccionMensual(), 0);
        const costoAnual = this.cultivos.reduce(
            (accum, c) => accum + 12 * c.calcularCostoOperativo(), 0);
        return produccionAnual / costoAnual;
    }

}