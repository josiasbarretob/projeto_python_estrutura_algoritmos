
import numpy as np

matriz = np.array([[3, 4, 1],
                   [3, 1, 5]])
soma = 0
print(matriz)
for linha in range(matriz.shape[0]):
    for coluna in range(matriz.shape[1]):
        soma+=matriz[linha][coluna]
print('Soma: ',soma)