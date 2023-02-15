soma = 0
for numero in range(51, 0, -1):
    soma = soma + numero
print(soma)

for numeroo in range(0, 100, 2):
    print(numeroo)

# Inicialização / Teste Lógico / Incremento ou Decremento
# numeroo       /
# https://www.devmedia.com.br/for-python-estrutura-de-repeticao-for/38513
cont = 0
nome = 'Maria Julia Peixoto Barreto'
for letra in nome:
    if letra == 'a':
        cont = cont + 1
print(cont)
# Código acima conta quantas vezes aparece a letra 'a'
for i in range(0, 10):
    print('Primeiro laço:', i)
    for j in range(0, 5):
        print('Segundo laço:', j)