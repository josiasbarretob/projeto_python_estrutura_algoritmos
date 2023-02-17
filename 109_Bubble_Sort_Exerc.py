import numpy as np


def bubble_sort(vetor):
    n = len(vetor)
    for i in range(n):
        for j in range(n - i - 1): #[9, 4, 2, 1]
            if vetor[j] > vetor[j + 1]:
                temp = vetor[j]
                vetor[j] = vetor[j + 1]
                vetor[j + 1] = temp
    return vetor


vetor = np.array([9, 4, 2, 1, 57, 34, 24])
print(bubble_sort(vetor))