import datetime

"""
Sistema Bancário Simples
Programa permite ao usuário criar usuário, conta corrente, depósitos,
saques e consultar o extrato.
Adicionando funções.
"""

def validar_cpf(cpf):
    """Valida se o CPF está no formato correto e possui 11 digitos."""
    cpf = cpf.replace('.', '').replace('-','')
    return len(cpf) == 11 and cpf.isdigit()

def validar_data_nascimento(data_nascimento):
    """Valida se a data de nascimento está no formato válido."""
    try:
        datetime.datetime.strptime(data_nascimento, '%d/%m/%Y')
        return True
    except ValueError:
        return False
    
def criar_usuario(usuarios, nome, data_nascimento, cpf, endereco):
    """Cria um novo usuário no sistema."""
    if not validar_data_nascimento(data_nascimento):
        print('Data de nascimento inválida')
        return False
    
    if not validar_cpf(cpf):
        print('CPF inválido')
        return False
    if cpf in usuarios:
        print('CPF já cadastrado.')
        return False
      
    novo_usuario = {
        'nome': nome,
        'data_nascimento': data_nascimento,
        'cpf': cpf,
        'endereco': endereco
    }
    usuarios[cpf] = novo_usuario
    print('Usuário criado com sucesso!')
    return True

def criar_conta_corrente(contas, usuario):
    """Cria uma nova conta e adiciona à lista de contas"""   
    numero_conta = str(len(contas) + 1).zfill(6)
    nova_conta = {
        'numero_da_conta': numero_conta,
        'agencia': '0001',
        'usuario': usuario,
        'saldo': 0,
        'extrato': [],
        'numero_saques': 0
    }
    contas.append(nova_conta)
    print(f'Conta corrente {numero_conta} criada com sucesso!')
    return nova_conta 

def depositar(valor, /, conta):
    """Realiza um depósito na conta."""
    try:
        valor = float(valor)
        if valor > 0:
            conta['saldo'] += valor
            conta['extrato'].append(f'Depósito: R$ {valor:.2f}\n')
            print(f'Depósito de R$ {valor:.2f} realizado com sucesso!')
        else:
            print('Valor inválido. Tente novamente!')
    except ValueError:
        print("Valor inválido. Por favor, digite um número.")

def sacar(*, conta, valor, limite_saques_diarios=3, valor_maximo_saque=500):
    """Realiza um saque na conta, considerando os limites."""
    try:
        valor = float(valor)
        if valor > 0 and valor <= conta['saldo'] and valor <= valor_maximo_saque:
            if conta['numero_saques'] < limite_saques_diarios:
                conta['saldo'] -= valor
                conta['extrato'].append(f'Saque: R$ {valor:.2f}\n')
                conta['numero_saques'] += 1
                print(f'Saque de R$ {valor:.2f} realizado com sucesso!')
            else:
                print('Limite diário de saques atingido.')
        else:
            print('Saldo insuficiente para realizar o saque.')
    except ValueError:
        print("Valor inválido. Por favor, digite um número.")  

def imprimir_extrato(conta, /, *, saldo_atual):
    print('\n----- Extrato -----')
    if not conta['extrato']:
        print('Não foram realizadas movimentações.')
    else:
        for movimento in conta['extrato']:
            print(movimento)
    print(f"Saldo atual: R$ {saldo_atual:.2f}")
    print('-------------------')

def listar_contas(contas):
    """Lista todas as contas cadastradas no sistema."""
    if not contas:
        print('Nenhuma conta cadastrada.')
        return

    print('\n----- Lista de Contas -----')
    for conta in contas:
        print(f"Número da Conta: {conta['numero_da_conta']}")
        print(f"Agência: {conta['agencia']}")
        print(f"Nome do Usuário: {conta['usuario']['nome']}")
        print(f"Saldo: R$ {conta['saldo']:.2f}")
        print('---------------------------')

def encerrar_sistema():
    print('Obrigado por utilizar nosso sistema bancário!')

usuarios = {}
contas = []
agencia_atual = 0

# Início do loop principal contendo o menu de opções
while True:
    print('\n----- Menu -----')
    print('1. Criar Usuário')
    print('2. Criar Conta Corrente')
    print('3. Depósito')
    print('4. Saque')
    print('5. Extrato')
    print('6. Listar Contas')
    print('7. Sair')
    
    opcao = input('Escolha uma opção: ')

    if opcao == '1':
        nome = input('Nome completo: ')
        data_nascimento = input('Data de nascimento (DD/MM/AAAA): ')
        cpf = input('CPF (somente números): ')
        endereco = input('Endereço (formato: logradouro - bairro - cidade/CEP estado): ')
        criar_usuario(usuarios, nome, data_nascimento, cpf, endereco)
    
    elif opcao == '2':
        cpf_usuario = input('CPF do usuário para vincular à conta (somente números): ')
        cpf_usuario = cpf_usuario.replace('.', '').replace('-', '')  # Remover formatação
        usuario_encontrado = usuarios.get(cpf_usuario)
        
        if usuario_encontrado:
            criar_conta_corrente(contas, numero_conta=None, usuario=usuario_encontrado)
        else:
            print('Usuário não encontrado. Não foi possível criar a conta.')
    
    elif opcao == '3':
        numero_conta = input('Informe o número da conta: ')
        conta_encontrada = None
        
        for conta in contas:
            if conta['numero_da_conta'] == numero_conta:
                conta_encontrada = conta
                break
        
        if conta_encontrada:
            valor_deposito = input('Informe o valor do depósito: ')
            depositar(valor_deposito, conta_encontrada)
        else:
            print('Conta não encontrada.')
    
    elif opcao == '4':
        numero_conta = input('Informe o número da conta: ')
        conta_encontrada = None
        
        for conta in contas:
            if conta['numero_da_conta'] == numero_conta:
                conta_encontrada = conta
                break
        
        if conta_encontrada:
            valor_saque = input('Informe o valor do saque: ')
            sacar(conta=conta_encontrada, valor=valor_saque)
        else:
            print('Conta não encontrada.')
    
    elif opcao == '5':
        numero_conta = input('Informe o número da conta: ')
        conta_encontrada = None
        
        for conta in contas:
            if conta['numero_da_conta'] == numero_conta:
                conta_encontrada = conta
                break
        
        if conta_encontrada:
            imprimir_extrato(conta_encontrada)
        else:
            print('Conta não encontrada.')
    
    elif opcao == '6':
        listar_contas(contas)

    elif opcao == '7':
        encerrar_sistema()
        break
    
    else:
        print('Opção inválida. Por favor, escolha uma opção válida.')
