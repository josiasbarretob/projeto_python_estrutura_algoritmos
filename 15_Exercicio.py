idade = int(input('Favor insira a sua idade: '))
if idade >= 0 and idade <= 12:
    print('Criança')
elif idade > 12 and idade <= 18:
    print('Adolescente')
elif idade > 18:
    print('Adulto')
else:
    print('Idade digitade inválida!')
