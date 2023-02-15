# https://blog.betrybe.com/tecnologia/tuplas-em-python/
tupla_computador = ('Teclado', 'Mouse', 'Impressora', 'Monitor', 'Headset')
print(tupla_computador)
print(tupla_computador.index('Monitor'))
for itens in tupla_computador:
    print(itens)

lista_Carros = ['Camaro', 'Gol', 'Cerato', 'Brasília', 'Fusca']
lista_Cores = ['Azul', 'Vermelho', 'Amarelo', 'Preto', 'Verde']
listaCompleta = lista_Cores + lista_Carros
print(listaCompleta)

lista = lista_Carros * 3
print(lista)
print(len(listaCompleta)) #Tamanho total da lista
print(listaCompleta[0])
lista_Carros.append('Honda Civic')
print(lista_Carros)
lista_Carros.remove('Camaro')
print(lista_Carros)

for elementos in lista_Carros:
    print(elementos)
