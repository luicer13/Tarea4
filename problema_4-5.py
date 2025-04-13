import numpy as np  

generator = np.random.default_rng(1010)  
pesos = generator.normal(size=10)        

ubicaciones = np.array([
    [0, 0, 0],
    [1, 1, 2],
    [0, 0, 0],
    [2, 1, 3],
    [5, 5, 4],
    [5, 0, 0],
    [5, 0, 0],
    [0, 0, 0],
    [2, 1, 3],
    [1, 3, 1]])

peces = np.zeros((10, 4))            # Creamos una matriz de ceros con 10 filas y 4 columnas
peces[:, 0:3] = ubicaciones          # Colocamos las coordenadas en las primeras 3 columnas
peces[:, 3] = pesos                  # Colocamos los pesos de los peces en la última columna

peces_por_ubicacion = {}  # Este diccionario agrupará los peces por ubicación

for i in range(len(peces)):  # Recorremos del 0 al 9
    x, y, z, peso = peces[i]  # Extraemos la información de cada pez
    if x < 5 and y < 5 and z < 5:  # Solo aceptamos peces dentro de la pecera (x,y,z < 5)
        ubicacion = (x, y, z)  # Se usan los valores x, y y z para determinar la ubicación de cada pez
        if ubicacion not in peces_por_ubicacion:
            peces_por_ubicacion[ubicacion] = []  # Si la ubicación no está, la creamos
          
        peces_por_ubicacion[ubicacion].append((i, peso))  # Guardamos el índice del pez y su peso para poder identificarlo después

sobrevivientes = []  #Guardamos los índices de los peces que sobreviven

for ubicacion in peces_por_ubicacion:
    lista_peces = peces_por_ubicacion[ubicacion]  # Lista de tuplas (indice, peso)

    # Buscamos el pez con mayor peso
    pez_mas_pesado = max(lista_peces, key=lambda valor: valor[1])  # valor[1] es el peso
    
    sobrevivientes.append(pez_mas_pesado[0]) # Guardamos el índice del pez más pesado en la lista de sobrevivientes

no_pez_sobreviviente = [elem + 1 for elem in sobrevivientes] #Se suma 1 para poner el numero de pez en lugar del índice
print(f"Lista de # pez(peces) sobreviviente(s): {no_pez_sobreviviente}.")