import { describe, it, expect } from 'vitest';
import { Lechuga } from '../src/Lechuga';

describe('Lechuga', () => {
    it('debe crear una lechuga con los datos correctos', () => {
        const lechuga = new Lechuga(2, 'Lechuga Romana', 5);
        
        expect(lechuga.getId()).toBe(2);
        expect(lechuga.getNombre()).toBe('Lechuga Romana');
        expect(lechuga.getDiasDesdeSiembra()).toBe(5);
    });

    it('debe inicializar diasDesdeSiembra en 0 por defecto', () => {
        const lechuga = new Lechuga(2, 'Lechuga Romana');
        
        expect(lechuga.getDiasDesdeSiembra()).toBe(0);
    });

    it('debe retornar el tipo de cultivo correcto', () => {
        const lechuga = new Lechuga(2, 'Lechuga Romana');
        
        expect(lechuga.getTipoCultivo()).toBe('Lechuga - Ciclo Corto');
    });

    it('debe calcular la producción mensual correctamente', () => {
        const lechuga = new Lechuga(2, 'Lechuga Romana');
        
        expect(lechuga.calcularProduccionMensual()).toBe(2);
    });

    it('debe calcular el costo operativo correctamente', () => {
        const lechuga = new Lechuga(2, 'Lechuga Romana');
        
        expect(lechuga.calcularCostoOperativo()).toBe(50);
    });
});
