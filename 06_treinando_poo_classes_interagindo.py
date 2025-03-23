class Veiculos:
    def __init__(self, marca='Desconhecido', modelo='Desconhecido', ano=0):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano

    def exibir_detalhes(self):
        print(f'''MARCA: {self.marca}\nMODELO: {self.modelo}\nANO: {self.ano}\n''')

    def __str__(self):
        return f'{self.marca}-{self.modelo}'

class Carro(Veiculos):
    pass


class Moto(Veiculos):
    pass


class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        self.veiculos = []

    def comprar_veiculo(self, veiculo):
        self.veiculos.append(veiculo) # adiciona um veículo a lista de veículos da pessoa
        print(f'{self.nome} COMPROU veículo {veiculo}')

    def estacionar_veiculo(self, veiculo, garagem):
        """Estaciona um veículo na garagem se a pessoa for dona dele."""
        if veiculo in self.veiculos:
            garagem.estacionar(veiculo)
        else:
            print(f"{self.nome} não possui este veículo para estacionar.")


class Garagem: #armazena carros
    def __init__(self):
        self.lista_veiculos = [] #lista de veículos adicionados na garagem

    def estacionar(self, veiculo): #adiciona veículo na garagem
        self.lista_veiculos.append(veiculo)
        print(f'Veículo {veiculo} ESTACIONADO na garagem')

    def veiculos_estacionados(self):
        print(f'Veículos presentes na garagem: ')
        for v in self.lista_veiculos:
            print(f'{v}')


#Criando objetos
pessoa1 = Pessoa('Anderson', 24)
garagem_coberta = Garagem()

#Instanciando veículos
carro1 = Carro('Honda', 'Civic', 2015)
carro2 = Carro('Chevrolet', 'Celta', 2008)
carro3 = Carro('Fiat', 'UNO', 2000)
moto1 = Moto('Yamaha', 'Fazer', 2023)
moto2 = Moto('Honda', 'FAN 160', 2014)
moto3 = Moto('Royal Enfild', 'Hunter 350', 2024)

#Comprando Veículos
pessoa1.comprar_veiculo(carro1)
pessoa1.comprar_veiculo(moto3)


#estacionando na garagem
pessoa1.estacionar_veiculo(carro1, garagem_coberta)
pessoa1.estacionar_veiculo(moto3, garagem_coberta)

#listar veículos estacionados na garagem
garagem_coberta.veiculos_estacionados()
