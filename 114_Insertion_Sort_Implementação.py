import numpy as np


def insertion_sort(vetor):
    n = len(vetor)
    for i in range(1, n):
        marcado = vetor[i]

        j = i - 1
        while j >= 0 and marcado < vetor[j]:
            vetor[j + 1] = vetor[j]
            j -= 1
        vetor[j + 1] = marcado
    return vetor


vetor = np.array([9, 4, 7, 5, 0, 1])
insertion_sort(vetor)
