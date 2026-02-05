import { describe, it, expect } from "vitest"
import { Taladro } from "./../src/taladro"
import { Amoladora } from "./../src/amoladora"
import { Hidrolavadora } from "./../src/hidrolavadora"

// ejemplo guiador
describe("costoAlquiler - Template Method", () => {
  it("calcula Taladro", () => {
    const t = new Taladro("Taladro Bosch")
    expect(t.costoAlquiler(1)).toBe(1300)
    expect(t.costoAlquiler(3)).toBe(1900)
  })

  // agregar los test faltantes aquí
  it("calcula Amoladora", () => {
    const a = new Amoladora("Amoladora Makita")
    expect(a.costoAlquiler(1)).toBe(1450)
    expect(a.costoAlquiler(3)).toBe(1950)
  })

  it("calcula Hidrolavadora", () => {
    const h = new Hidrolavadora("Hidrolavadora Karcher")
    expect(h.costoAlquiler(1)).toBe(3900)
    expect(h.costoAlquiler(3)).toBe(4700)
  })
  
  // descomenta esto debajo para cuando llegues al taladro
  it("lanza error si dias <= 0", () => {
    const t = new Taladro("Taladro")
    expect(() => t.costoAlquiler(0)).toThrow()
    expect(() => t.costoAlquiler(-1)).toThrow()
  })

})
