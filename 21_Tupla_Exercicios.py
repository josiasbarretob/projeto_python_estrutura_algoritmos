lanche = ('Hamburguer', 'Pizza', 'Salgado', 'Suco')
lanches = ['Hamburguer', 'Pizza', 'Salgado', 'Suco']

numeros = (10, 13, 10, 5)
print(lanche[3])
print(numeros[1])

for i in range(len(lanche)):
    print(f'Lanche {i} = {lanche[i]}')

print('===============================')

for comida in lanche:
    print(f'O lanche é: {comida}')

print('===============================')

for i, comida in enumerate(lanche):
    print(f'Lanche {i} = {lanche[i]}')

#As tuplas são imutáveis.

#numeros[0] = 3
print('===============================')
for i in range(len(numeros)):
    print(numeros[i])

# lanches.insert(0, 'Café')
lanches[0] = 'Café'
lanches.append('Bolo')
print(lanches)
print(sorted(lanches))