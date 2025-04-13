import numpy as np
generator = np. random . default_rng (1010) #genero valores "random"
data = np. round ( generator . uniform (low= 0 ,  #genero 10 valores desde 0 a 100 
high = 100 ,
size = 10 ))
valores_absolutos = np.abs(data[:, np.newaxis]- data[np.newaxis,:]) #uso np.newaxis y broadcasting para restar los numeros entre sí y utilizo np.abs para que se vuelvan positivos
print(valores_absolutos)