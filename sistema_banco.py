# Constantes para limites
LIMITE_SAQUES = 3
LIMITE_VALOR_SAQUE = 500

# Variáveis de estado
saldo = 0
extrato = ''
numero_saques = 0

"""
Sistema Bancário Simples
Programa permite ao usuário realizar depósitos, saques e consultar o extrato.
"""
# Início do loop principal contendo o menu de opções
while True:
    print('\n----- Menu -----')
    print('1. Depósito')
    print('2. Saque')
    print('3. Extrato')
    print('4. Sair')
    
    opcao = input('Escolha uma opção: ')

    if opcao == '1':
        valor_deposito = float(input('Informe o valor do depósito: '))
        if valor_deposito > 0:
            saldo += valor_deposito
            extrato += f'Depósito: R$ {valor_deposito:.2f}\n'
            print(f'Depósito de R$ {valor_deposito:.2f} realizado com sucesso!')
        else:
            print('Valor inválido. Tente novamente.')

    elif opcao == '2':
        if saldo == 0:
            print('Saldo insuficiente!')
            continue 

        valor_saque = float(input('Informe o valor do saque: '))
        if valor_saque <= 0:
            print('Valor inválido. Tente novamente.')
        elif numero_saques >= LIMITE_SAQUES:
            print('Limite diário de saques atingido.')
        elif valor_saque > saldo:
            print('Saldo insuficiente para realizar o saque.')
        elif valor_saque >= LIMITE_VALOR_SAQUE:
            print(f'Não foi possível realizar o saque! Valor máximo de saque é R$ {LIMITE_VALOR_SAQUE:.2f}.')
        else:
            saldo -= valor_saque
            extrato += f'Saque: R$ {valor_saque:.2f}\n'
            numero_saques += 1
            print(f'Saque de R$ {valor_saque:.2f} realizado com sucesso!')    
                
    elif opcao == '3':
        print('\n----- Extrato -----')
        if not extrato:
            print('Não foram realizadas movimentações.')
        else:
            print(extrato)
        print(f'Saldo atual: R$ {saldo:.2f}')
        print('-------------------')

    elif opcao == '4':
        print('Obrigado por utilizar nosso sistema bancário!')
        break
    else:
        print('Opção inválida. Por favor, escolha uma opção válida.')