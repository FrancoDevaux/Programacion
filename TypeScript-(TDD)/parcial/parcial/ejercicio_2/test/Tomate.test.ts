import { describe, it, expect } from 'vitest';
import { Tomate } from '../src/Tomate';

describe('Tomate', () => {
  describe('Tomate', () => {
    it('debe crear un tomate con los datos correctos', () => {
      const tomate = new Tomate(1, 'Tomate Cherry', 10);
      
      expect(tomate.getId()).toBe(1);
      expect(tomate.getNombre()).toBe('Tomate Cherry');
      expect(tomate.getDiasDesdeSiembra()).toBe(10);
    });

    it('debe inicializar diasDesdeSiembra en 0 por defecto', () => {
      const tomate = new Tomate(1, 'Tomate Cherry');
      
      expect(tomate.getDiasDesdeSiembra()).toBe(0);
    });

    it('debe retornar el tipo de cultivo correcto', () => {
      const tomate = new Tomate(1, 'Tomate Cherry');
      
      expect(tomate.getTipoCultivo()).toBe('Tomate - Ciclo Medio');
    });

    it('debe calcular la producción mensual correctamente', () => {
      const tomate = new Tomate(1, 'Tomate Cherry');
      
      expect(tomate.calcularProduccionMensual()).toBe(4);
    });

    it('debe calcular el costo operativo correctamente', () => {
      const tomate = new Tomate(1, 'Tomate Cherry');
      
      expect(tomate.calcularCostoOperativo()).toBe(120);
    });
  });
});