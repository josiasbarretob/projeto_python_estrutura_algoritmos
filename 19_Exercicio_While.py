soma = 0
numero = 1
while numero <= 5:
    nota = float(input(f'Favor digite a {numero}ª nota: \n'))
    soma = soma + nota
    numero += 1
media = soma / 5
print('A média das 5 notas é: ', media)
# As variáveis declaradas dentro do bloco while ou for só podem ser acessadas dentro deste laço.
# Variável local...