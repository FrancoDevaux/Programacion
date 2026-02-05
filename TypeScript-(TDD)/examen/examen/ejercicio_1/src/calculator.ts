export class Calculator {
  suma(a: number, b: number): void {
    const resultado = a + b;
    console.log(`Suma: ${a} + ${b} = ${resultado}`);
  }

  resta(a: number, b: number): void {
    const resultado = a - b;
    console.log(`Resta: ${a} - ${b} = ${resultado}`);
  }

  division(a: number, b: number): void {
    if (b === 0) {
      console.log(`No se puede dividir por cero!`);
    } else {
      const resultado = a / b;
      console.log(`Division: ${a} / ${b} = ${resultado}`);
    }
  }

  multiplicacion(a: number, b: number): void {
    const resultado = a * b;
    console.log(`Multiplicacion: ${a} * ${b} = ${resultado}`);
  }
}