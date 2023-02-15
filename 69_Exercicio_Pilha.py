import numpy as np
class Pilha:
    def __init__(self, tamanho):
        self.tamanho = tamanho
        self.topo = -1
        self.valores = np.empty(self.tamanho, dtype=str)

    def pilha_cheia(self):
        if self.topo == self.tamanho - 1:
            return True
        else:
            return False

    def pilha_vazia(self):
        if self.topo == -1:
            return True
        else:
            return False

    def empilhar(self, valor):
        if self.pilha_cheia():
            print('A pilha está cheia e náo é possível adicionar elementos!')
        else:
            self.topo += 1
            self.valores[self.topo] = valor

    def desempilhar(self):
        if self.pilha_vazia():
            print('A pilha está vazia!')
        else:
            self.topo -= 1
            # self.__valores[self.topo] = valor

    def ver_topo(self):
        if self.pilha_vazia():
            print('Pilha Vazia! Topo igual a:', self.valores[self.topo])
        else:
            print('Topo igual a:', self.valores[self.topo])


print('---Validador de Expressão---')
expressao = input('Favor digite a expressão para a verificação:\n')
print('A expressão digitada foi:\n', expressao)
tamanho = len(expressao)
pilha_expressao = Pilha(tamanho)
for caracter in expressao: #{8+(9/[4/2])}
    if caracter == '{':
        pilha_expressao.empilhar('{')
    elif caracter == '(':
        pilha_expressao.empilhar('(')
    elif caracter == '[':
        pilha_expressao.empilhar('[')
    elif caracter == ']':
        pilha_expressao.desempilhar()
    elif caracter == ')':
        pilha_expressao.desempilhar()
    elif caracter == '}':
        pilha_expressao.desempilhar()


if pilha_expressao.pilha_vazia():
    print('Correto!')
else:
    print('Incorreto!')