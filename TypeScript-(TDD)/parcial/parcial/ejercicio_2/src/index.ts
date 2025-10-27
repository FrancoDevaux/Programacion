import { GranjaVerticalExtendida } from './GranjaVerticalExtendida';
import { Lechuga } from './Lechuga';
import { Tomate } from './Tomate';
 
const granja = new GranjaVerticalExtendida();

const lechuga1 = new Lechuga(1, "Lechuga A", 25);
const tomate1 = new Tomate(2, "Tomate Cherry", 45);

granja.agregarCultivo(lechuga1);
granja.agregarCultivo(tomate1);

console.log("=== PRUEBAS ===");
console.log("Producción total:", granja.calcularProduccionTotal(), "kg/mes");
console.log("Rentabilidad:", granja.calcularRentabilidad(), "$/mes");

