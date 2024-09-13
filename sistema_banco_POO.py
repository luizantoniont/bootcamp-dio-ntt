import datetime

"""
Sistema Bancário Simples
Programa permite ao usuário criar usuário, conta corrente, depósitos,
saques e consultar o extrato.
Adicionando POO.
"""
# Classe para centralizar as validações
class Utils:
    @staticmethod
    def validar_cpf(cpf):
        """Valida se o CPF está no formato correto e possui 11 dígitos."""
        cpf = cpf.replace('.', '').replace('-','')
        return len(cpf) == 11 and cpf.isdigit()

    @staticmethod
    def validar_data_nascimento(data_nascimento):
        """Valida se a data de nascimento está no formato válido."""
        try:
            datetime.datetime.strptime(data_nascimento, '%d/%m/%Y')
            return True
        except ValueError:
            return False
        
class Cliente:
    def __init__(self, nome, data_nascimento, cpf, endereco):
        if not Utils.validar_cpf(cpf):
            raise ValueError("CPF inválido!")
        if not Utils.validar_data_nascimento(data_nascimento):
            raise ValueError("Data de nascimento inválida!")

        self._nome = nome
        self._data_nascimento = data_nascimento
        self._cpf = cpf
        self._endereco = endereco

    @property
    def nome(self):
        return self._nome
    
    @property
    def cpf(self):
        return self._cpf
    
    def __str__(self):
        return f'{self._nome} ({self._cpf})'
    
      
class Conta:
    def __init__(self, cliente):
        self._numero_da_conta = str(len(Operacoes.contas) + 1).zfill(6)
        self._agencia = '0001'
        self._cliente = cliente
        self._saldo = 0
        self._extrato = []
        self._numero_saques = 0

    def depositar(self, valor):
        if valor > 0:
            self._saldo += valor
            self._extrato.append(f'Depósito: R$ {valor:.2f}\n')
            print(f'Depósito de R$ {valor:.2f} realizado com sucesso!')
        else:
            print('Valor inválido. Tente novamente!')

    def sacar(self, valor, limite_saques_diarios=3, valor_maximo_saque=500):
        if valor > 0 and valor <= self._saldo and valor <= valor_maximo_saque:
            if self._numero_saques < limite_saques_diarios:
                self._saldo -= valor
                self._extrato.append(f'Saque: R$ {valor:.2f}\n')
                self._numero_saques += 1
                print(f'Saque de R$ {valor:.2f} realizado com sucesso!')
            else:
                print('Limite diário de saques atingido.')
        else:
            print('Saldo insuficiente para realizar o saque.')     

    def imprimir_extrato(self):
        print('\n----- Extrato -----')
        if not self._extrato:
            print('Não foram realizadas movimentações.')
        else:
            for movimento in self.__extrato:
                print(movimento)
        print(f"Saldo atual: R$ {self.__saldo:.2f}")
        print('-------------------')

    @property
    def numero_da_conta(self):
        return self._numero_da_conta

    @property
    def cliente(self):
        return self._cliente
    
# Nova Classe ContaCorrente (subclasse de Conta)
class ContaCorrente(Conta):
    def __init__(self, cliente):
        super().__init__(cliente)

    def __str__(self):
        return f'Conta Corrente - Cliente: {self.cliente.nome}'
    
# Classe Operacoes que gerencia a interação com o usuário
class Operacoes:
    contas = []  # Lista de contas (centralizada)

    def __init__(self):
        self.usuarios = {}

    def criar_cliente(self):
        nome = input('Nome completo: ')
        data_nascimento = input('Data de nascimento (DD/MM/AAAA): ')
        cpf = input('CPF (somente números): ')
        endereco = input('Endereço (formato: logradouro - bairro - cidade/CEP estado): ')
        if cpf in self.usuarios:
            print('CPF já cadastrado.')
            return

        try:
            novo_cliente = Cliente(nome, data_nascimento, cpf, endereco)
            self.usuarios[cpf] = novo_cliente
            print('Cliente criado com sucesso!')
        except ValueError as e:
            print(e)

    def criar_conta_corrente(self):
        cpf_usuario = input('CPF do usuário para vincular à conta (somente números): ')
        usuario_encontrado = self.usuarios.get(cpf_usuario)

        if usuario_encontrado:
            nova_conta = ContaCorrente(usuario_encontrado)
            Operacoes.contas.append(nova_conta)
            print(f'Conta corrente {nova_conta.numero_da_conta} criada com sucesso!')
        else:
            print('Usuário não encontrado. Não foi possível criar a conta.')

    def realizar_deposito(self):
        numero_conta = input('Informe o número da conta: ')
        conta_encontrada = self.buscar_conta(numero_conta)

        if conta_encontrada:
            valor_deposito = float(input('Informe o valor do depósito: '))
            conta_encontrada.depositar(valor_deposito)
        else:
            print('Conta não encontrada.')

    def realizar_saque(self):
        numero_conta = input('Informe o número da conta: ')
        conta_encontrada = self.buscar_conta(numero_conta)

        if conta_encontrada:
            valor_saque = float(input('Informe o valor do saque: '))
            conta_encontrada.sacar(valor_saque)
        else:
            print('Conta não encontrada.')

    def imprimir_extrato(self):
        numero_conta = input('Informe o número da conta: ')
        conta_encontrada = self.buscar_conta(numero_conta)

        if conta_encontrada:
            conta_encontrada.imprimir_extrato()
        else:
            print('Conta não encontrada.')

    def listar_contas(self):
        if not Operacoes.contas:
            print('Nenhuma conta cadastrada.')
            return

        print('\n----- Lista de Contas -----')
        for conta in Operacoes.contas:
            print(f"Número da Conta: {conta.numero_da_conta}")
            print(f"Nome do Cliente: {conta.cliente.nome}")
            print('---------------------------')

    def buscar_conta(self, numero_conta):
        for conta in Operacoes.contas:
            if conta.numero_da_conta == numero_conta:
                return conta
        return None

    def encerrar_sistema(self):
        print('Obrigado por utilizar nosso sistema bancário!')   

# Executar o sistema
sistema = Operacoes()

# Loop principal com o menu
while True:
    print('\n----- Menu -----')
    print('1. Criar Cliente')
    print('2. Criar Conta Corrente')
    print('3. Depósito')
    print('4. Saque')
    print('5. Extrato')
    print('6. Listar Contas')
    print('7. Sair')

    opcao = input('Escolha uma opção: ')

    if opcao == '1':
        sistema.criar_cliente()
    elif opcao == '2':
        sistema.criar_conta_corrente()
    elif opcao == '3':
        sistema.realizar_deposito()
    elif opcao == '4':
        sistema.realizar_saque()
    elif opcao == '5':
        sistema.imprimir_extrato()
    elif opcao == '6':
        sistema.listar_contas()
    elif opcao == '7':
        sistema.encerrar_sistema()
        break
    else:
        print('Opção inválida. Por favor, escolha uma opção válida.')
