import random

face_dados = {
    1: (
        "┌─────┐",
        "│     │",
        "│  •  │",
        "│     │",
        "└─────┘",
    ),
    2: (
        "┌─────┐",
        "│•    │",
        "│     │",
        "│    •│",
        "└─────┘",
    ),
    3: (
        "┌─────┐",
        "│•    │",
        "│  •  │",
        "│    •│",
        "└─────┘",
    ),
    4: (
        "┌─────┐",
        "│•   •│",
        "│     │",
        "│•   •│",
        "└─────┘",
    ),
    5: (
        "┌─────┐",
        "│•   •│",
        "│  •  │",
        "│•   •│",
        "└─────┘",
    ),
    6: (
        "┌─────┐",
        "│•   •│",
        "│•   •│",
        "│•   •│",
        "└─────┘",
    ),
}


quantas_vezes = int(input('Quantas vezes deseja sortear? '))
lista = []
if quantas_vezes > 0 and quantas_vezes <= 6:
    for i in range(quantas_vezes):
        lista.append(random.randint(1, 6))
    print(lista)
else:
    print('erro, valor inválido')

#exibir dados lado a lado
linhas_dados = [""] * 5
for valor in lista:
    dados_sorteados = face_dados[valor]
    print(face_dados[valor])
    for i in range(5): # segredo, de fazer contagem até 5, quantidade de "linhas" que tem em cada dado
        linhas_dados[i] += dados_sorteados[i] + " " # espaço entre dados

for linha in linhas_dados:
    print(linha)
