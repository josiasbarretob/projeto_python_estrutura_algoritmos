import math
a = 5
b = 9
print('A soma é:', a + b)
print('A subtração é:', a - b)
print('A divisão é:', a / b)
print('A multiplicação é:', a * b)
print('O resto da divisão é:', a % b)
print(f'{a} elevado a {b} é:', a ** b)
print(f'A Raiz quadrada de {b} é:',math.sqrt(b))

#---------------------------------------------------------

casos_doencas = 134
numero_habitantes = 34432
casos_habitantes = casos_doencas / numero_habitantes
print(round(casos_habitantes,4)) #Arredondamento em 4 casas após a vírgula

###https://docs.python.org/pt-br/3/library/math.html