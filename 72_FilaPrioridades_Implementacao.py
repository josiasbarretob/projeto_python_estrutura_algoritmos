import numpy as np
class FilaPrioridade:
    def __init__(self, tamanho):
        self.tamanho = tamanho
        self.numero_elementos = 0
        self.valores = np.empty(self.tamanho, dtype=int)

    def __fila_vazia(self):
        return self.numero_elementos == 0

    def __fila_cheia(self):
        return self.numero_elementos == self.tamanho

    def enfileirar(self, valor):
        if self.__fila_cheia():
            print('A fila está cheia!')
            return

        if self.numero_elementos == 0:
            self.valores[self.numero_elementos] = valor
            self.numero_elementos += 1
        else:
            x = self.numero_elementos - 1
            while x >= 0:
                if valor > self.valores[x]:
                    self.valores[x+1] = self.valores[x]
                else:
                    break
                x -= 1
            self.valores[x + 1] = valor
            self.numero_elementos += 1

    def desenfileirar(self):
        if self.__fila_vazia():
            print('A fila está vazia!')
            return

        valor = self.valores[self.numero_elementos - 1]
        self.numero_elementos -= 1
        return valor

    def primeiro(self):
        if self.__fila_vazia():
            return -1
        return self.valores[self.numero_elementos - 1]

fila = FilaPrioridade(5)
#Tradicional - 30, 50, 10, 5
#Prioridades - 5, 10, 30, 50
fila.enfileirar(30)
fila.enfileirar(50)
fila.enfileirar(10)
fila.enfileirar(5)
print(fila.valores)
fila.enfileirar(40)
print(fila.valores)
print(fila.primeiro())
fila.desenfileirar()
fila.desenfileirar()
print(fila.primeiro())