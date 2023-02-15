numero = 1
soma = 0
while numero < 6:
    print(numero)
    soma += numero
    numero += 1
print(soma)

for i in range(0, 6):
    print(i)

num1 = -1
while num1 < 1 or num1 > 10:
    num1 = int(input('Digite um número de 0 a 10: \n'))