import re
texto = 'Minha casa fica na Avenida 28 de março, 196. O CEP é 28170-000 e o meu linkedin é https://www.linkedin.com/in/josiasbarreto/'
print(re.findall('\d',texto))
print(re.findall('\d{5}-\d{3}',texto))
print(re.findall('https?://[A-Za-z0-9./]+',texto))