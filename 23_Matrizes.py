import numpy as np
matriz = np.array([[1,2,3],
                   [4,5,6],
                   [7,8,9]])
print(matriz) #Impressão da Matriz
print(matriz.shape) #Ordem da Matriz
print(matriz[0], matriz[1][2])

for i in range (matriz.shape[0]):
    print(matriz[i])