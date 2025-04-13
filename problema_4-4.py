import numpy as np
# Simulación de puntajes
generator = np.random.default_rng(1010)
notas = np.round(generator.uniform(low=0, high=100, size=20)) #vuelvo a generar notas "random" con el generador
print(f"notas iniciales {notas}")
indices = np.where(notas <60) [0] #obtengo los valores de los índices en las notas menores que 60
tres_primeros = indices[:3] #obtengo los  tres primeros índices
notas[tres_primeros] = 0 #sustituyo los 3 primeros índices menores que 60 de las notas por 0
print(f"notas finales {notas}")