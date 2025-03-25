import random
palavras = ["Futebol", 'python', 'mato grosso do sul', 'bolo de cenoura', 'ornitorrinco' "Cachorro", "Gato", "Javali",
            "Neymar", "Samba", "Coringa", "Feijoada", "Caipirinha", "Copa", "Carnaval", "Capoeira", "Caipira", "Arara",
            "Jequiti", "Pao de queijo", "Itaipava", "Cristo Redentor", "Copacabana"]


#Escolhe palavra
palavra_escolhida = random.choice(palavras).lower()
tentativas = 5
risquinhos_na_tela = ['_'] * len(palavra_escolhida)


print(palavra_escolhida)
print(risquinhos_na_tela)
while tentativas != 0 and '_' in risquinhos_na_tela:
    resposta = input().lower()
    if resposta not in palavra_escolhida:
        print(f'Você errou, faltam {tentativas-1} tentativas')
        tentativas -= 1
    else:
        if resposta in palavra_escolhida:
            for i in range(len(palavra_escolhida)):
                if palavra_escolhida[i] == resposta: # se a letra corresponder a resposta
                    risquinhos_na_tela[i] = resposta # substitui o risquinho pelo caracter correto
            print(''.join(risquinhos_na_tela))

if '_' not in risquinhos_na_tela:
    print(f'\n\033[32mPARABÉNS, ACERTOU A PALAVRA:\033[34m {' '.join(risquinhos_na_tela)}')

else:
    print('\n\033[31mFALHOU, PERDEU O JOGO')
