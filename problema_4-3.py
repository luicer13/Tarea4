import numpy as np

# Simulamos puntajes con random
generator = np.random.default_rng(1010)
scores = np.round(generator.uniform(low=0, high=100, size=10))

# Creamos la matriz de diferencias absolutas
dif_matrix = np.abs(scores[:, np.newaxis] - scores[np.newaxis, :])

print("Puntajes:", scores)
print("Matriz de diferencias:\n", dif_matrix)