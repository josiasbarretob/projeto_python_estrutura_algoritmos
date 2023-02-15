soma = 0
for numero in range(0, 5):
    nota = float(input(f'Favor digite a {numero+1}ª nota: \n'))
    soma += nota
media = soma / 5
print('A média das 5 notas é:', media)

