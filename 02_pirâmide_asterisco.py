'''
Pirâmido com *
O padrão a cada linha, é adicionado 2 estrelas depois da tericeira linha que tem 5 estrelas, por padrão dos espaços usados por cada estrela
  ex: *
     ***
    *****
   *******
  *********
'''
n = 8
for c in range(n):
    print(' ', end='')
    for a in range(c, c+2, 2):
        print('*' * c)

print()
