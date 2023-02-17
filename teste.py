# # Bubble Sort
import numpy


# Implementação utilizando Vetores!
def bubble_sort(vetor):
    tamanho = len(vetor)
    for i in range(tamanho):
        for j in range(tamanho - i - 1):
            if vetor[j] > vetor[j + 1]:  # Ex: vetor=[9, 4, 6, 3, 7, 1]
                temp = vetor[j]
                vetor[j] = vetor[j + 1]
                vetor[j + 1] = temp
    return vetor


vetor = numpy.array([9, 4, 6, 3, 7, 1])
print(bubble_sort(vetor))


# Implementação utilizando listas!
def bubble_sort_lista(lista):
    tamanho = len(lista)
    for i in range(tamanho):
        for j in range(tamanho - 1 - i):
            if lista[j] > lista[j + 1]:
                temp = lista[j]
                lista[j] = lista[j + 1]
                lista[j + 1] = temp
    return lista


lista = [9, 8, 7, 6, 5, 4, 3, 2, 1]
print(bubble_sort_lista(lista))


# Implementação do Selection
def selection_sort(vetor):  # vetor=[9, 8, 4, 5, 2]
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


vetor = numpy.array([9, 8, 4, 5, 2])
print(selection_sort(vetor))


# Implementação do Selection SORT utilizando Listas!
def selection_sort_lista(lista):
    n = len(lista)
    for i in range(n):
        index_menor = i
        for j in range(i + 1, n):  # Lista = [9, 8, 4, 5, 2]
            if lista[index_menor] > lista[j]:
                index_menor = j
        temp = lista[i]
        lista[i] = lista[index_menor]
        lista[index_menor] = temp
    return lista


lista = [9, 8, 7, 6, 5, 4, 0, 3, 2, 1]
print(selection_sort_lista(lista))
