lista = []
tupla = ()
for i in range(5):
    lista += [i]
    tupla += (i,)
print('Lista', lista)
lista.append('Josias')
print('Lista', lista)
lista.insert(0, 10)
print('Lista', lista)
print(tupla)
tupla=('Josias', 10)
print(tupla)

def list(n):
    return range(n)
print(lista)
lista2 = list()
for i in lista2:
    print(i)