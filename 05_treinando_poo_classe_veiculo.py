
class Veiculo:
    def __init__(self, marca, modelo, ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano

    def exibir_detalhes(self):
        print(f'MARCA: {self.marca} // MODELO: {self.modelo} // ANO: {self.ano} \n')


class Moto(Veiculo):
    def __init__(self, marca, modelo, ano, cilindrada): #precisa desse construtor
        super().__init__(marca, modelo, ano) #chamar o construtor da classe-pai para classe filha / garantir que a inicialização do construtor da classe pai seja iniciada corretamente
        self.cilindrada = cilindrada

    def get_cilindrada(self):
        print(f'Cilindrada da moto modelo {self.modelo} é: {self.cilindrada}')

    def set_cilindrada(self, valor_cilindrada):
        self.cilindrada = valor_cilindrada

    def empinar(self):
        print('EMPINANDO E DANDO GRAU...\n')


class Carro:
    def __init__(self, marca='Desconhecido', modelo='Genérico', anoo=0):
        self.marca = marca #nível de acesso Público
        self.modelo = modelo #Público
        self.aceleracao = 0 #Público
        self.velocidade = 0 #Público
        self.anoo = anoo

        self.__ano = 0  # Privado

    def get_ano_carro(self):
        return f'O ano do carro {self.modelo} é: {self.__ano}\n'

    def set_ano_carro(self, ano):
        if ano >= 0:
            self.__ano = ano
        else:
            print('Valor digitado inválido\n')


    def exibir_detalhes(self):
        print(f'A marcada do carro: {self.marca}')
        print(f'O modelo do carro: {self.modelo}')
        print(f'O ano do carro: {self.anoo}')
        print('')

    def acelerar(self, aceleracao, tempo):
        self.aceleracao = aceleracao
        self.velocidade += self.aceleracao * tempo
        velocidade_kmh = self.velocidade * 3.6
        print(f'Aceleração do carro {self.modelo} : {self.aceleracao} m/s²')
        print(f'O carro {self.modelo} está a {velocidade_kmh:.2f} km/h\n')



    #definir/alterar método especial para re retornar características do carro
    def __str__(self):
        return f'Carro: {self.marca} // {self.modelo} // ({self.__ano})\n'
#car1.__str__() - chamando o método de maneira errada, pois de forma correta retorna no print, o que será imprimido


car1 = Carro('HONDA', 'HBW', 2024)
car1.exibir_detalhes()
car2 = Carro('VoelgsWagen', 'GOL G4', 2018)
car2.exibir_detalhes()
#---------------------------------------------------------------------
print(car1)
print(car2)
#---------------------------------------------------------------------
car2.acelerar(5, 3)
#---------------------------------------------------------------------
#ENCAPSULAMENTO
car3 = Carro('Hyundai', 'HB20')
print(car3.get_ano_carro())
car3.set_ano_carro(2020)
print(car3.get_ano_carro())
#---------------------------------------------------------------------
moto1 = Moto('Yamaha', 'Fazer', 2021, 500)
moto1.exibir_detalhes()
moto1.get_cilindrada()
moto1.set_cilindrada(650)
moto1.get_cilindrada()
moto1.empinar()

