m1 = float(input('Favor insira a nota da M1: \n'))
m2 = float(input('Favor insira a nota da M2: \n'))
m3 = float(input('Favor insira a nota da M3: \n'))
mediaAritmetica = (m1 + m2 + m3) / 3
if 0 <= mediaAritmetica <= 4.0:
    print('O aluno está reprovado!')
elif 4 < mediaAritmetica < 6.0:
    print('O aluno pegou exame')
    mExame = float(input('Favor digite a nota do exame: \n'))
    if mExame >= 6.0:
        print('Aluno está aprovado!')
    else:
        print('Aluno está reprovado!')
elif mediaAritmetica >= 6:
    print('O aluno está aprovado!')
else:
    print('Nota digitada inválida!')