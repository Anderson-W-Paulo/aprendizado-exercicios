menu = {'Pipoca': 15, 'Refrigerante': 8, 'Água': 4, 'Chocolate': 5, 'Cachorro-quente': 5, 'Milkshake': 20}

print('='*25, 'Bem-Vindo', '='*25)

#Apresentar Cardápio
for chave, valor in menu.items():
    print(f'    |{chave:.<20}R$ {valor:.2f}|')
print('='*50)

#Inicializa total
v_total = 0

#Loop pera gerar pedidos
while True:
    escolha = input('Faça seu pedido: ').title()

    if escolha.lower() == 'encerrar':
        print('Pedido Encerrado')
        break
    elif escolha in menu.keys():
        v_total += menu[escolha]
        print(f'Você adicionou {escolha} (R${menu[escolha]}) ao seu pedido')
    else:
        print('Item não econtrado, tente novamente')


#Final
print(f'Total a pagar:  R${v_total}')
print('Obrigado pelo seu pedido')
