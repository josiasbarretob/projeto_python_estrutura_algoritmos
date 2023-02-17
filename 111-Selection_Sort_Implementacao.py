import numpy as np


def selection_sort(vetor):
    n = len(vetor)
    for i in range(n):
        index_menor = i
        for j in range(i + 1, n):
            if vetor[index_menor] > vetor[j]:
                index_menor = j
        temp = vetor[i]
        vetor[i] = vetor[index_menor]
        vetor[index_menor] = temp
    return vetor


vetor = np.array([7, 8, 9, 2, 0, 1])
print(selection_sort(vetor))
