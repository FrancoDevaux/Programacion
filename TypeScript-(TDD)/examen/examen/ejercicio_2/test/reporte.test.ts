import { describe, it, expect } from "vitest"
import { Taladro } from "./../src/taladro"
import { Amoladora } from "./../src/amoladora"
import { Hidrolavadora } from "./../src/hidrolavadora"
import { reporteAlquiler } from "./../src/reporte"

// Descomenta esto cuando llegues al reporte
describe("reporteAlquiler", () => {
  it("genera líneas y total", () => {
    const herramientas = [
      new Taladro("Taladro Bosch"),
      new Amoladora("Amoladora Makita"),
      new Hidrolavadora("Hidrolavadora Karcher"),
    ]
    const texto = reporteAlquiler(herramientas, 2)
    expect(texto).toMatch(/Taladro Bosch/)
    expect(texto).toMatch(/Amoladora Makita/)
    expect(texto).toMatch(/Hidrolavadora Karcher/)
    expect(texto).toMatch(/TOTAL:/)
    
    expect(texto).toMatch(/TOTAL: \$7600/)
  })
})