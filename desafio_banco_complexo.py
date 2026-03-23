from datetime import datetime

historico_depositos = []
historico_saques = []
contador_de_saques = 0
contador_de_depositos = 0
numero_maximo_saques = 10
numero_maximo_depositos = 5
saldo = 0

clientes = {
    '463846792-21': {"nome": "Gustavo", "telefone": '122343232-3243', "ativo": True},
    '3456783210':   {"nome": "Marquezine", "telefone": '127433434-3263', "ativo": True},
    '44027883829':  {'nome': 'Seu Jorge', 'telefone': '137433634-3243', 'ativo': True}
}

agencia = {
    '0001': '463846792-21',
    '0002': '3456783210',
    '0003': '44027883829'
}


def sacar():
    global saldo, contador_de_saques
    valor_saque = float(input('Digite o valor que você deseja sacar: '))

    if valor_saque <= 0 or valor_saque > saldo:
        print('Valor requisitado não compatível com sua conta')
    elif contador_de_saques >= numero_maximo_saques:
        print('Você excedeu a quantidade de saques permitidos!')
    else:
        contador_de_saques += 1
        saldo -= valor_saque
        data_hora = datetime.now().strftime("%d/%m/%Y %H:%M")
        historico_saques.append((valor_saque, data_hora))
        print('Seu saque foi concluído')


def depositar():
    global saldo, contador_de_depositos
    valor_deposito = float(input('Digite o valor que deseja depositar: '))

    if valor_deposito <= 0:
        print('Valor inválido')
    elif contador_de_depositos >= numero_maximo_depositos:
        print('Você excedeu o limite de depósitos do dia')
    else:
        saldo += valor_deposito
        contador_de_depositos += 1
        data_hora = datetime.now().strftime("%d/%m/%Y %H:%M")
        historico_depositos.append((valor_deposito, data_hora))
        print('Seu depósito foi concluído com sucesso')


def extrato():
    print(f'\nSaldo atual: R${saldo:.2f}')
    print(f'Saques realizados: {contador_de_saques}')

    if historico_saques:
        print("\nHistórico de saques:")
        for i, (valor, data) in enumerate(historico_saques, 1):
            print(f"  Saque {i}: R${valor:.2f} em {data}")

    if historico_depositos:
        print("\nHistórico de depósitos:")
        for i, (valor, data) in enumerate(historico_depositos, 1):
            print(f"  Depósito {i}: R${valor:.2f} em {data}")


def criar_usuario():
    cpf   = input('Insira o CPF: ')
    nome  = input('Insira o nome: ')
    tel   = input('Insira o telefone: ')

    if cpf not in clientes:
        clientes[cpf] = {'nome': nome, 'telefone': tel, 'ativo': True}
        print('Novo cliente cadastrado com sucesso!')
    else:
        print('Este CPF já existe, revise seus dados')


def criar_conta_corrente():
    ultima_chave = sorted(agencia.keys())[-1]
    nova_chave = f"{int(ultima_chave) + 1:04d}"

    cpf = input('Escreva o CPF de um cliente existente: ')

    if cpf in clientes:
        agencia[nova_chave] = cpf
        print(f'Conta {nova_chave} criada com sucesso!')
    else:
        print('CPF não encontrado nos clientes cadastrados')


while True:
    try:
        opcao = int(input('\n[1]Extrato  [2]Sacar  [3]Depositar  [4]Criar cliente  [5]Criar conta\n> '))
    except ValueError:
        print('Digite apenas números!')
        continue

    if opcao == 1:
        extrato()
    elif opcao == 2:
        sacar()
    elif opcao == 3:
        depositar()
    elif opcao == 4:
        criar_usuario()
    elif opcao == 5:
        criar_conta_corrente()
    else:
        print('Digite uma opção válida...')