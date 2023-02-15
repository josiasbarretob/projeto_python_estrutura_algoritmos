alunos = {'Pedro': 8.0, 'Maria': 10.0, 'Amilton': 7.5, 'Josias': 10.0}
alunos['Thamirys'] = 6.0
alunos['Majuh'] = 7.0
with open('alunos.txt', 'w') as text3:
    for alunos, nota in alunos.items():
         text3.write(f'nome, nota ({alunos}, {nota})\n')


with open('/Users/josborges/PycharmProjects/pythonProject/teste_pycharm/alunos.txt') as texto:
    for linha in texto:
        print(linha)