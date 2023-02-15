nome = 'Josias Barreto'
print(nome)
nomeMaiusculo = nome.upper()
print(nomeMaiusculo)
nomeMinusculo = nome.lower()
print(nomeMinusculo)
nomeLetra = nome.capitalize()
print(nomeLetra)
metadeNome = nome[0:4]
print(metadeNome)
ultimasLetrasNome = nome[2:]
print(ultimasLetrasNome)

radical = nome.replace('Barreto','Peixoto')
print(radical)
radical2 = nome.replace('eto','os')
print(radical2)
radical3 = nome.find('s') #Encontrar determinado caracter na string
print(radical3)
print(len(nome)) #Tamanho da String
print(nome.strip())
num1 = 14
num2 = 16
print(f'A soma de {num1} + {num2} = {num1 + num2}') #f de formatação
