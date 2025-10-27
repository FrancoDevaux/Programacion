import { describe, it, expect, beforeEach } from 'vitest';
import { GranjaVerticalExtendida } from '../src/GranjaVerticalExtendida';
import { Tomate } from '../src/Tomate';
import { Lechuga } from '../src/Lechuga';

describe('GranjaVerticalExtendida', () => {
  let granja: GranjaVerticalExtendida;

  beforeEach(() => {
    granja = new GranjaVerticalExtendida();
  });

  it('debe crear una granja vertical extendida vacía', () => {
    expect(granja).toBeDefined();
    expect(granja).toBeInstanceOf(GranjaVerticalExtendida);
  });

  it('debe calcular producción total de 0 cuando no hay cultivos', () => {
    expect(granja.calcularProduccionTotal()).toBe(0);
  });

  it('debe calcular producción anual de un solo tomate', () => {
    const tomate = new Tomate(1, 'Tomate Cherry');
    granja.agregarCultivo(tomate);
    
    // Tomate produce 4 kg/mes * 12 meses = 48 kg/año
    expect(granja.calcularProduccionTotal()).toBe(48);
  });

  it('debe calcular producción anual de una sola lechuga', () => {
    const lechuga = new Lechuga(2, 'Lechuga Romana');
    granja.agregarCultivo(lechuga);
    
    // Lechuga produce 2 kg/mes * 12 meses = 24 kg/año
    expect(granja.calcularProduccionTotal()).toBe(24);
  });

  it('debe calcular producción total anual de múltiples cultivos', () => {
    const tomate1 = new Tomate(1, 'Tomate Cherry');
    const tomate2 = new Tomate(2, 'Tomate Perita');
    const lechuga1 = new Lechuga(3, 'Lechuga Romana');
    const lechuga2 = new Lechuga(4, 'Lechuga Crespa');
    
    granja.agregarCultivo(tomate1);
    granja.agregarCultivo(tomate2);
    granja.agregarCultivo(lechuga1);
    granja.agregarCultivo(lechuga2);
    
    // 2 tomates: 2 * 4 * 12 = 96 kg/año
    // 2 lechugas: 2 * 2 * 12 = 48 kg/año
    // Total: 144 kg/año
    expect(granja.calcularProduccionTotal()).toBe(144);
  });

  it('debe calcular producción total correcta con mezcla de cultivos', () => {
    const tomate = new Tomate(1, 'Tomate Cherry');
    const lechuga = new Lechuga(2, 'Lechuga Romana');
    
    granja.agregarCultivo(tomate);
    granja.agregarCultivo(lechuga);
    
    // Tomate: 4 * 12 = 48 kg/año
    // Lechuga: 2 * 12 = 24 kg/año
    // Total: 72 kg/año
    expect(granja.calcularProduccionTotal()).toBe(72);
  });

  it('debe heredar el método agregarCultivo de la clase base', () => {
    const tomate = new Tomate(1, 'Tomate Cherry');
    
    expect(() => granja.agregarCultivo(tomate)).not.toThrow();
    expect(granja.calcularProduccionTotal()).toBe(48);
  });

  it('debe calcular rentabilidad con tomate y lechuga ', () => {
    const tomate = new Tomate(1, 'Tomate Cherry');
    const lechuga = new Lechuga(2, 'Lechuga Romana');
    
    granja.agregarCultivo(tomate);
    granja.agregarCultivo(lechuga);
    
    const rentabilidad = granja.calcularRentabilidad();
    expect(rentabilidad).toBeCloseTo(0.03529, 4);
  });

});