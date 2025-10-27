import { describe, it, expect } from 'vitest';
import { IRendimiento } from '../src/iRendimiento';
import { Tomate } from '../src/Tomate';
import { Lechuga } from '../src/Lechuga';

describe('IRendimiento - Interface', () => {
  it('debe ser implementada por Tomate', () => {
    const tomate = new Tomate(1, 'Tomate Cherry');
    
    // Verificar que implementa los métodos de la interfaz
    expect(tomate.calcularProduccionMensual).toBeDefined();
    expect(tomate.calcularCostoOperativo).toBeDefined();
    expect(typeof tomate.calcularProduccionMensual).toBe('function');
    expect(typeof tomate.calcularCostoOperativo).toBe('function');
  });

  it('debe ser implementada por Lechuga', () => {
    const lechuga = new Lechuga(2, 'Lechuga Romana');
    
    // Verificar que implementa los métodos de la interfaz
    expect(lechuga.calcularProduccionMensual).toBeDefined();
    expect(lechuga.calcularCostoOperativo).toBeDefined();
    expect(typeof lechuga.calcularProduccionMensual).toBe('function');
    expect(typeof lechuga.calcularCostoOperativo).toBe('function');
  });

  it('los métodos de IRendimiento deben retornar números', () => {
    const tomate = new Tomate(1, 'Tomate Cherry');
    const lechuga = new Lechuga(2, 'Lechuga Romana');
    
    expect(typeof tomate.calcularProduccionMensual()).toBe('number');
    expect(typeof tomate.calcularCostoOperativo()).toBe('number');
    expect(typeof lechuga.calcularProduccionMensual()).toBe('number');
    expect(typeof lechuga.calcularCostoOperativo()).toBe('number');
  });

  it('debe permitir usar objetos que implementan IRendimiento polimórficamente', () => {
    const cultivos: IRendimiento[] = [
      new Tomate(1, 'Tomate Cherry'),
      new Lechuga(2, 'Lechuga Romana'),
      new Tomate(3, 'Tomate Perita')
    ];
    
    const produccionTotal = cultivos.reduce(
      (sum, cultivo) => sum + cultivo.calcularProduccionMensual(), 
      0
    );
    
    // 4 + 2 + 4 = 10
    expect(produccionTotal).toBe(10);
  });

  it('debe permitir calcular costo total usando la interfaz', () => {
    const cultivos: IRendimiento[] = [
      new Tomate(1, 'Tomate Cherry'),
      new Lechuga(2, 'Lechuga Romana')
    ];
    
    const costoTotal = cultivos.reduce(
      (sum, cultivo) => sum + cultivo.calcularCostoOperativo(), 
      0
    );
    
    // 120 + 50 = 170
    expect(costoTotal).toBe(170);
  });
});