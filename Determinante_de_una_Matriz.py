import numpy as np

print ('Ingresa el orden de la Matriz a Calcular')
filasA, columnasA = int(input()), int(input())

matrizA = []
for i in range(filasA):
    matrizA.append([0] * columnasA)

print('Ingrese la Matriz A')
for fila in range(filasA):
        for columna in range(columnasA):
            matrizA[fila][columna] = float(
        input(f'Ingrese la posición número {fila}, {columna}:  '))

determinante = np.linalg.det(matrizA)
print(determinante)