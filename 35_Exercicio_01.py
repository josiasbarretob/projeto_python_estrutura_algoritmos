try:
    lista_real = []
    lista_real.append(float(input('Favor digite o primeiro número: \n')))
    lista_real.append(float(input('Favor digite o segundo número: \n')))
    divisao = lista_real[0] / lista_real[1]
except ValueError:
    print('Erro, Dígito inválido!')
except ZeroDivisionError:
    print('Error, divisão por zero!')
except IndexError:
    print('Error, Posição da Lista Inexistente!')
except KeyboardInterrupt:
    print('Usuário interrompeu a execução!')
else:
    print('A divisão de', lista_real[0], '/', lista_real[1], 'é =', divisao)

