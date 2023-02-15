### Dicionario
pessoas = {'Idade' : 28, 'Ano de Nascimento' : 1994, 'Sexo': 'M', 'CPF' : '106.697.307-50'}
# print(pessoas)
# print(pessoas['Idade'])
# pessoas['CEP'] = '28.175-000'
# print(pessoas.values())
for chave, valor in pessoas.items():
    print(chave, valor)
pessoas['Altura'] = 1.78
print(pessoas.keys(), pessoas.values(), pessoas.get('CPF'))
# https://kenzie.com.br/blog/dicionario-python/#:~:text=Para%20criar%20um%20dicion%C3%A1rio%20em,armazenados%20de%20forma%20n%C3%A3o%20ordenada.
### Conjuntos
nomes = ('Josias', 'Maria Julia', 'Thamirys', 'Ivanete', 'Aline', 'Ivania', 'Thamirys')
print(nomes)
print(set(nomes))

c1 = {1, 4, 6, 7, 9, 3}
c2 = {2, 4, 6, 7, 9, 0}
c3 = c1.intersection(c2)
c4 = c1.difference(c2)
print(c3)
print(c4)