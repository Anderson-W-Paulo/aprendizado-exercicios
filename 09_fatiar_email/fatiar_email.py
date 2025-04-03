'''
1)Programa recebe um endereço de e-mail e ira dividi-lo em partes
    Nome do Usuário -> antes do @
    Domínio -> depos do @
    Extensão de domínio -> parte final (ex.: .com, .org, .edu)

2)Adicionar as partes dividades em um CSV agrupado por listas em dicionários
'''


class AdicionarEmail:
    dict_usuario = {'Nome Usuário': [], 'Domínio': [], 'Extensão Domínio': []}

    def __init__(self, email):
        self.email = email
        #self.lista_nome_usuario = []
        #self.lista_dominio = []
        #self.lista_extensao_dominio = []
        self.formatar_email(self.email)

    def exibir(self):
        print(f'Email: {self.email}')
        #print(self.lista_nome_usuario)
        #print(self.lista_dominio)
        #print(self.lista_extensao_dominio)

    def formatar_email(self, email):
        #FORMATANDO EMAIL E ADICIONANDO AS LISTAS
        email_dividido = email.split('@') # ['nome usuário', 'dominio.ext_dominio']
        #self.lista_nome_usuario.append(email_dividido[0])

        #self.lista_dominio.append(email_dividido2[0])
        #self.lista_extensao_dominio.append(email_dividido2[1])
        #ADIOCINANDO LISTAS AS CHAVES CORRETAS NO DICIONÁRIO
        AdicionarEmail.dict_usuario['Nome Usuário'].append(email_dividido[0])
        email_dividido2 = email_dividido[1].split('.')  # ['dominio', ' ext_dominio']
        AdicionarEmail.dict_usuario['Domínio'].append(email_dividido2[0])
        AdicionarEmail.dict_usuario['Extensão Domínio'].append(email_dividido2[1])

    def adicionar_no_banco_de_dados(self):
        # ABRE O ARQUIVO PARA ADICIONAR OS DADOS
        with open('BancoDados.txt', 'a+') as arquivo:
            for chave, valor in (AdicionarEmail.dict_usuario.items()):
                arquivo.write(f'{chave} : {valor}\n')

    def ler_banco_de_dados(self):
        # LÊ O CONTEÚDO DO ARQUIVO E EXIBE
        with open('BancoDados.txt', 'r') as arquivo:
            conteudo = arquivo.read()
            print(conteudo)


r = 0
while True:
    email = input('EMAIL: ')

    contato = AdicionarEmail(email)
    contato.exibir()
    r = input('Deseja continuar [S/N]').lower()
    if r == 'n':
        contato.adicionar_no_banco_de_dados()
        break


















