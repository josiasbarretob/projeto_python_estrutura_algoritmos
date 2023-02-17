import numpy as np


def bubble_sort(vetor):
    n = len(vetor)
    for i in range(n):
        for j in range(0, n - 1 - i):
            if vetor[j] > vetor[j + 1]:
                temp = vetor[j]
                vetor[j] = vetor[j + 1]
                vetor[j + 1] = temp
    return vetor

vetor = np.array([9, 7, 23, 6, 5, 10, 1, 4, 2, 3])
print(bubble_sort(vetor))

print('=========================================')
def bubble_sortI(lista):
    n = len(lista)
    for i in range(n):
        for j in range(0, n - 1 - i):
            if lista[j] > lista[j + 1]:
                temp = lista[j]
                lista[j] = lista[j + 1]
                lista[j + 1] = temp
    return lista

list  = (7, 2, 1, 8, 'Josias', 8.7)
lista = [8, 7, 3, 9, 1, 0, 10, 3, 9.6]

print(list)
print(bubble_sortI(lista))
