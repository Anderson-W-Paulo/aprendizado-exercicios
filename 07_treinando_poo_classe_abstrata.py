from abc import ABC, abstractmethod

class Funcionarios(ABC):
    def __init__(self, nome, idade, cargo):
        self.nome = nome
        self.idade = idade
        self.cargo = cargo
        self.lista_cargo = {'estagiário':1500, 'assistente':1870, 'vendedor': 2000,'junior':3000, 'pleno': 5000, 'senior':8000, 'gerente':7500, 'presidente':12000}

    @abstractmethod
    def buscar_salario(self, cargo):
        pass

class Gerente(Funcionarios):
    def buscar_salario(self, cargo):
        for k, v in self.lista_cargo.items():
            if cargo == k:
                print(f'O salário do funcionário {self.nome} : R${v}')


class Vendedor(Funcionarios):
    def buscar_salario(self, cargo):
        for k, v in self.lista_cargo.items():
            if cargo == k:
                print(f'O salário do funcionário {self.nome} : R${v}')

    def calcular_salario(self, q_vendas):
        salario = 2000 + (20 * q_vendas)
        print(f'Salário do vendedor esse ano: {salario}')

#instanciando funcionários
f1 = Gerente('George', 63, 'gerente')
f2 = Vendedor('Paulo', 29, 'estagiário')

#
f1.buscar_salario('gerente')
f2.buscar_salario('vendedor')
f2.calcular_salario(8)

