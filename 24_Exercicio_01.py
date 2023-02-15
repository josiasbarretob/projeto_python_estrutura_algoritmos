# Lista:
# Crie uma estrutura de repetição para fazer a leitura de 5 números inteiros
# e os armazene dentro de uma lista.
# Após a leitura, crie outra estrutura de repetição para somar todos os valores digitados
listaNumeros = []
for i in range(1, 6):
    numero = int(input(f'Favor digite o {i}º número: \n'))
    listaNumeros.append(numero)
print(listaNumeros)
soma = 0
for numero in listaNumeros:
    soma += numero
print(soma)