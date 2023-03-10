import numpy as np


class VetorOrdenado:
    def __init__(self, capacidade):
        self.capacidade = capacidade
        self.ultima_posicao = -1
        self.valores = np.empty(self.capacidade, dtype=int)

    def imprime(self):
        if self.ultima_posicao == -1:
            print('O vetor está vazio!')
        else:
            for i in range(self.ultima_posicao + 1):
                print(f'Posição {i} -- Valor {self.valores[i]}')

    def insere(self, valor):
        if self.ultima_posicao == self.capacidade - 1:
            print('Vetor cheio! Capacidade máxima atingida.')
            return
        posicao = 0
        for i in range(self.ultima_posicao + 1):
            posicao = 1
            if self.valores[i] > valor:
                break
            if i == self.ultima_posicao:
                posicao = i + 1
            x = self.ultima_posicao
            while x >= posicao:
                self.valores[x + 1] = self.valores[x]
                x -= 1

            self.valores[posicao] = valor
            self.ultima_posicao += 1

    def pesquisar(self, valor):
        for i in range(self.ultima_posicao + 1):
            if valor == self.valores[i]:
                return i
            if self.valores[i] > valor:
                return -1
            if i == self.ultima_posicao:
                return -1

    def pesquisa_binaria(self, valor):
        limite_inferior = 0
        limite_superior = self.ultima_posicao
        while True:
            posicao_atual = int((limite_inferior + limite_superior) / 2)
            #Se achou na primeira tentativa
            if self.valores[posicao_atual] == valor:
                return posicao_atual
            #Se não achou o valor
            elif limite_inferior > limite_superior:
                return -1
            #Dividir elementos
            else:
                #Limite inferior
                if self.valores[posicao_atual] < valor:
                    limite_inferior = posicao_atual + 1
                #Limite superior
                else:
                    limite_superior = posicao_atual -1


    def excluir(self, valor):
        posicao = self.pesquisar(valor)
        if posicao == -1:
            return -1
        else:
            for i in range(posicao, self.ultima_posicao):
                self.valores[i] = self.valores[i + 1]

            self.ultima_posicao -= 1


vetor = VetorOrdenado(2)
# vetor.insere(3)
# vetor.insere(4)
# vetor.insere(5)
# vetor.insere(6)
# vetor.excluir(3)
# vetor.imprime()
