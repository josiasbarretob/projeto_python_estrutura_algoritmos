import numpy as np


class Pilha:
    def __init__(self, tamanho):
        self.__tamanho = tamanho
        self.__topo = -1
        self.__valores = np.empty(self.__tamanho, dtype=int)

    def __pilha_cheia(self):
        if self.__topo == self.__tamanho - 1:
            return True
        else:
            return False

    def __pilha_vazia(self):
        if self.__topo == -1:
            return True
        else:
            return False

    def empilhar(self, valor):
        if self.__pilha_cheia():
            print('A pilha está cheia e náo é possível adicionar elementos!')
        else:
            self.__topo += 1
            self.__valores[self.__topo] = valor

    def desempilhar(self):
        if pilha.__pilha_vazia():
            print('A pilha está vazia!')
        else:
            self.__topo -= 1
            # self.__valores[self.topo] = valor

    def ver_topo(self):
        if self.__pilha_vazia():
            print('Pilha Vazia! Topo igual a:', self.__valores[self.__topo])
        else:
            print('Topo igual a:', self.__valores[self.__topo])


pilha = Pilha(5)
pilha.empilhar(2)
pilha.empilhar(3)
pilha.desempilhar(2)
pilha.ver_topo()
print(pilha.ver_topo())
