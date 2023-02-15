# - Função para ler e retorna o valor da temperatura (não recebe parâmetro)
def ler_temperatura():
    temp = float(input('Favor informe a Temperatura em Celsius:\n'))
    return temp


def converter_temperatura(temp_celsius):
    temp_fahrenheit = (9 * temp_celsius + 160) / 5
    return temp_fahrenheit


def mostrar_temperatura(temp_fahrenheit):
    print(temp_fahrenheit)


temperatura_celsius = ler_temperatura()
converter_fahrenheit = converter_temperatura(30)
mostrar = mostrar_temperatura(converter_fahrenheit)
print(temperatura_celsius)
print(converter_fahrenheit)
print(mostrar)