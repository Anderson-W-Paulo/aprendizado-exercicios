'''
Given an input of size: n, output a right angled triangle with n number of rows
Dada uma entrada de tamanho: n, a saída é um triângulo retângulo com n números de linhas

vídeo: https://www.youtube.com/watch?v=xbwYRW7FY0E
'''

n = int(input('Informe quantas linhas para seu triângulo de *: '))
if n <= 0:
    while n <= 0:
        n = int(input('ERRO! - informe um número inteiro positivo: '))

print('=-' * 30)

#método 1 - eu fiz
for i in range(n):
    for j in range(1):
        print('*' * (i+1))

print()
row = n

#método 2 - youtube
for row in range(1, row+1):
    print('*' * row)
