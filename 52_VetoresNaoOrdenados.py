import numpy as np


class VetorNaoOrdenado:
    def __init__(self, tamanho):
        self.tamanho = tamanho
        self.ultima_posicao = -1
        self.valores = np.empty(self.tamanho, dtype=int)

    # O(n)
    def imprimir(self):
        if self.ultima_posicao == -1:
            print('O vetor está vazio!')
        else:
            for i in range(self.ultima_posicao + 1):
                print(i, ' - ', self.valores[i])

    def inserir(self, valor):
        if self.ultima_posicao == self.tamanho - 1:
            print('Capacidade máxima atingida!')
        else:
            self.ultima_posicao += 1
            self.valores[self.ultima_posicao] = valor

    def pesquisar(self, valor):
        for i in range(self.ultima_posicao + 1):
            if valor == self.valores[i]:
                return i
        return -1

    def excluir(self, valor):
        posicao = self.pesquisar(valor)
        if posicao == -1:
            print('Valor não encontrado!')
        else:
            for i in range(posicao, self.ultima_posicao):
                self.valores[i] = self.valores[i + 1]

            self.ultima_posicao -= 1

vetor = VetorNaoOrdenado(10)
vetor.inserir(7)
vetor.inserir(6)
vetor.inserir(5)
vetor.inserir(4)
vetor.inserir(3)
vetor.pesquisar(10)
vetor.excluir(6)
vetor.imprimir()
