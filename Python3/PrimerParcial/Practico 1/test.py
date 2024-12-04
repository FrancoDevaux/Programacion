
notas = [80, 40, 10, 70, 80, 95, 100]
notas_ajustadas = notas.copy()

for i in range(len(notas)):
    notas_ajustadas[i] += 5
    if(notas_ajustadas[i] > 95):
        notas_ajustadas[i] = 100
    
print(f"\nLa lista nueva: {notas_ajustadas}")
print(f"La lista vieja: {notas}")