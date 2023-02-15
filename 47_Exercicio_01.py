class Aluno:
    def __init__(self, nome, nota1, nota2):
        self.nome = nome
        self.nota1 = nota1
        self.nota2 = nota2
        self.media = 0.0


    def calcular_media(self):
        self.media = (self.nota1 + self.nota2) / 2
        return self.media

    def imprimir(self):
        print(f'Nome: {self.nome}, nota 1: {self.nota1}, nota 2: {self.nota2}, média: {self.media}')


    def mostrar_resultado(self):
        if self.media >= 6:
            print('O aluno está aprovado!')
        else:
            print('O aluno está Reprovado!')

aluno1 = Aluno('JOSIAS', 8.0, 9.8)
media = aluno1.calcular_media()
print(aluno1.imprimir(), aluno1.calcular_media(), aluno1.mostrar_resultado())
