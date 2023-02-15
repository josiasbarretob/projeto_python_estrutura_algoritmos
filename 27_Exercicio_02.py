# Função para ler os valores (não recebe parâmetro e retorna os dois valores)
def leitura():
    # usuário deve fornecer o tempo gasto na viagem e a velocidade média durante ela.
    tempo = float(input('Caro usuário, favor informe o tempo gasto na viagem: \n'))
    velocidade = float(input('Caro usuário, favor informe a velocidade média do carro: \n'))
    return tempo, velocidade


# Função para calcular a distância (recebe como parâmetro o tempo e a velocidade e retorna a distância)
def distancia(tempo, velocidade):
    return tempo * velocidade


# Função para calcular a quantidade de litros (recebe como parâmetro a distância e retorna os litros)
def calcular_litros(distancia):
    return distancia / 12


# Função para apresentar o resultado (recebe como parâmetro os valores e somente imprime o resultado)
def imprimir(velocidade, tempo, distancia, calcular_litros):
    return print(f'Velocidade Km/h:', velocidade, '\nTempo gasto na Viagem (h):', tempo, '\n Distancia: ', distancia, 'Km',
          '\nCombustível em Litros: ', round(calcular_litros,1))


tempo_viagem, velocidade_carro = leitura()
deslocamento = distancia(tempo_viagem, velocidade_carro)
litros = calcular_litros(deslocamento)
imprimir(velocidade_carro, tempo_viagem, deslocamento, litros)

