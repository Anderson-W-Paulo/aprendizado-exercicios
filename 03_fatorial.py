#FATORIAL RECURSIVO
"""
Esse fatorial executará recursivamente fatorial(n) até encontrar um resultado de referência que é o n == 0 = 1
Encontrando a referência fatorial(0) = 1, seguira com uma pilha de processos onde fará as multiplicações
factorial(5) = 5 * factorial(4)
factorial(4) = 4 * factorial(3)
factorial(3) = 3 * factorial(2)
factorial(2) = 2 * factorial(1)
factorial(1) = 1 * factorial(0)
factorial(0) = 1  (caso base)

factorial(1) = 1 * 1 = 1
factorial(2) = 2 * 1 = 2
factorial(3) = 3 * 2 = 6
factorial(4) = 4 * 6 = 24
factorial(5) = 5 * 24 = 120
"""
def fatorial(n):
    if n == 0: #se n for 0 retornará o valor 1
        return 1
    else:
        recursao = fatorial(n-1) #chama a função de novo com n-1
        resultado = n * recursao #multiplica n pelo resultado da função
        return resultado #retorna o valor calculado

#print(fatorial(5))


#FATORIAL RECURSIVO COM VERIFICAÇÃO DE TIPOS

def fatorial2(n):
    if not isinstance(n, int):
        print('Fatorial dever ser apenas número inteiro')
        return None
    elif n < 0:
        print('Fatorial não deve ser negativo')
    elif n == 0:
        return 1
    else:
        return n * fatorial(n-1)

#print(fatorial2('a'))


#EXEMPLO DE DEPURAÇÃO
def fatorial3(n):
    space = ' ' * (4*n) # controlar a endentação da saída
    print(space, 'fatorial', n)
    if n == 0:
        print(space, 'retorna 1')
        return 1
    else:
        recursao = fatorial3(n-1)
        resultado = n * recursao
        print(space, 'retorno', resultado)
        return resultado

print(fatorial3(4))
print('-------------------------------------------\n')

#exercícios
def b(z, depth=0):
    ident = ' ' * depth #cria espaço para indicar profundidade
    print(f'{ident}Entrando em b({z})')
    prod = a(z, z, depth + 1) # prod entrando na função a
    print(f'{ident}Saindo de b({z}) com resultado {prod}')
    return prod

def a(x, y, depth = 0):
    ident = ' ' * depth
    print(f'{ident}Entrando a({x}, {y})')
    x = x + 1
    resultado = x * y
    print(f'{ident}Saindo de a({x}, {y}) com resultado {resultado}')
    return resultado

def c(x, y, z, depth = 0):
    ident = ' ' * depth
    print(f'{ident}Entrando c({x},{y},{z})')
    total = x + y + z
    square = b(total, depth + 1) ** 2 # square entrando na função b
    print(f'{ident}Entrando c({x},{y},{z}) com resultado {square}')
    return square


x = 1
y = x + 1
print(c(x, y + 3, x + y))
#(1, 5, 3)