lista = []
for i in range(5):
    lista.append(int(input(f'Favor digite o {i}º número: \n')))

n = len(lista)

print(lista)
lista.append('Casa')
print(lista)