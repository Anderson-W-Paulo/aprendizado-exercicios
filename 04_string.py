#BUSCANDO LETRA NA PALAVRA
''''Semenhante ao método find()'''
def buscar(palavra, letra):
    index = 0
    while index < len(palavra):
        if palavra[index] == letra:
            return print(index)
        index = index + 1
    return -1

word = 'pneumatologista'
letter = 'a'
buscar(word, letter)
print(word.find(letter))

#MOSTRAR QUANTAS VEZES A LETRA APARECE NA PALAVRA
'''TEMO O MÉTODO count()'''
def contar(palavra, letra):
    c = 0
    for letra in palavra:
        if letra == letter:
            c += 1
    print(f'A letra {letra} aparece {c} vezes')

contar(word, letter)
print(word.count(letter))




