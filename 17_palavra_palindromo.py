import re

print('AFINAL, PALÍNDROMO OU NÃO?')

palavra_invertida = []
dado = input('Informe a sua palavra/frase: ').lower()
dado_transformado = dado.replace(' ', '').replace(',', '').replace('.', '')

for i in dado_transformado[::-1]:
    palavra_invertida.append(i)

p2 = ''.join(palavra_invertida)

if p2 == dado_transformado:
    print('sim')
else:
    print('não')




