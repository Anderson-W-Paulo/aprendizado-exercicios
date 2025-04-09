import time
'''

class CountdownTimer:
    def __init__(self):
        self.hora = 0
        self.minuto = 0
        self.segundo = 0

    #@staticmethod # método independe de self, não precisa instânciar objeto para chamar o método
    def apresentacao(self):
        print('='*50, 'BEM VINDO AO TEMPORIZADOR', '='*50)

        def validar_entrada(valor):
            if not valor.isdigit():
                while not valor.isdigit():
                    print('Valor inválido, apenas número')
                    valor = input('Digite novamente: ')
            valor = int(valor)
            if valor < 0 or valor > 60:
                while valor < 0 or valor > 60:
                    print('Valor inválido, insira valor entre 0 e 59')
                    valor = int(input('Digite novamente: '))
            return valor

        hora = input('INFORME [HORA]: ')
        self.hora = validar_entrada(hora)
        minuto = input('INFORME [MINUTO]: ')
        self.minuto = validar_entrada(minuto)
        segundo = input('INFORME [SEGUNDO]: ')
        self.segundo = validar_entrada(segundo)

    def regressor(self):
        "Executa a contagem regressiva baseada nos atributos hora, minuto, segundo"
        total_segundos = (3600 * self.hora) + (60 * self.minuto) + self.segundo

        while total_segundos > 0:
            h, m, s = total_segundos // 3600, total_segundos // 60, self.segundo

            time.sleep(1)
            total_segundos -= 1 #( ts = ts - 1 => ts -= 1
            print(f'Faltam {total_segundos} segundos')
        print("\n⏳ Tempo esgotado!")


temporizador = CountdownTimer()
temporizador.apresentacao()
temporizador.regressor()'''


meu_tempo = int(input('Entre com o tempo em segundos: '))

for x in range(meu_tempo, 0, -1):
    segundos = x % 60
    minutos = int(x / 60) % 60
    horas = int(x / 3600)
    print(f'{horas:02}:{minutos:02}:{segundos:02}')
    time.sleep(1)

print("\n⏳ Tempo esgotado!")












