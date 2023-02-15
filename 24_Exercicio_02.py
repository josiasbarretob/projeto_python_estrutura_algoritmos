# Dicionário:
# Crie um dicionário para armazenar o nome e a nota de 3 alunos,
# fazendo a leitura dos valores por meio de uma estrutura de repetição.
# Depois, crie uma nova estrutura de repetição para somar todas as notas e retornar a média
dicionarioAlunos = {}
for elementoDicionario in range(0, 3):
    nome = input('Favor insira o seu nome: \n')
    nota = float(input('Informe a sua nota: \n'))
    dicionarioAlunos[nome] = nota
print(dicionarioAlunos)
soma = 0
for valor in dicionarioAlunos.values():
    soma += valor
media = soma / 3
print('A média das notas digitadas é:', round(media,2))