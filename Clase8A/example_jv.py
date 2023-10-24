import numpy as np

# matriz numeros aleatorios
matriz = np.random.randint(0,2,[5,5])
print(matriz)

# Tomar una posición y voy a sumar todos los numeros que estan a su alrededor

def sumar_vecinos(x,y,matriz):
    # dim matriz
    sum = 0
    dim = matriz.shape
    for i in range(-1,2):
        for j in range(-1,2):
            if i == j == 0:
                continue
            else:
                if x+i >= 0 and x+i < dim[0] and y+j >= 0 and y+j < dim[1]:
                    sum += matriz[x+i,y+j]

    print(sum)

x = int(input("Ingrese x: "))
y = int(input("Ingrese y: "))
sumar_vecinos(x,y,matriz)


