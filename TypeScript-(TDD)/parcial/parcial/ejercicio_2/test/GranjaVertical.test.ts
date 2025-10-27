import { describe, it, expect, beforeEach } from 'vitest';
import { GranjaVertical } from '../src/GranjaVertical';
import { Tomate } from '../src/Tomate';
import { Lechuga } from '../src/Lechuga';

describe('GranjaVertical', () => {
  let granja: GranjaVertical;

  beforeEach(() => {
    granja = new GranjaVertical();
  });

  it('debe crear una granja vertical vacía', () => {
    expect(granja).toBeDefined();
    expect(granja).toBeInstanceOf(GranjaVertical);
  });

  it('debe poder agregar un cultivo de tomate', () => {
    const tomate = new Tomate(1, 'Tomate Cherry');
    
    expect(() => granja.agregarCultivo(tomate)).not.toThrow();
  });

  it('debe poder agregar un cultivo de lechuga', () => {
    const lechuga = new Lechuga(2, 'Lechuga Romana');
    
    expect(() => granja.agregarCultivo(lechuga)).not.toThrow();
  });

  it('debe poder agregar múltiples cultivos', () => {
    const tomate = new Tomate(1, 'Tomate Cherry');
    const lechuga = new Lechuga(2, 'Lechuga Romana');
    const tomate2 = new Tomate(3, 'Tomate Perita');
    
    expect(() => {
      granja.agregarCultivo(tomate);
      granja.agregarCultivo(lechuga);
      granja.agregarCultivo(tomate2);
    }).not.toThrow();
  });
});