import numpy as np

def es_primo(n):  #Función para definir que es un número primo

    if n <= 1: 
        return False
    elif n ==  2:
        return True
    for i in range(2,n):
        if n % i == 0:
            return False
    return True

arr = np.zeros((10,10,10)) #Crear un arrelo de ceros

ind_impar = [i for i in range(10) if i % 2 == 1] #list comprehension para valores impares del 0 al 9 
ind_par = [j for j in range(10) if j % 2 == 0]#list comprehension para valores pares del 0 al 9 
ind_primo = [k for k in range(10) if es_primo(k)] #list comprehension para valores primos del 0 al 9

arr[np.ix_(ind_impar,ind_par,ind_primo)] = 1 #np.ix_ crea un grid multidimensional de los indices que puede ser brodcasteable donde se combinan los valores impares, pares y primos  y a estos se les da el valor de 1
print(arr) #imprimo el arreglo con los valores de 1 modificados
print(np.argwhere(arr==1)) #np.argwhere muestra los indices del arreglo 10x10x10 donde se añadio el valor de 1, que son donde hay impar, par y primo