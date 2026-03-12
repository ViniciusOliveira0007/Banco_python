# base é fazer um banco com contas, clientes, etc.
# precisa conseguir criar conta com função e as ações que eu tinha feito precisam se tornar funções

#importação do tempo 
from datetime import datetime 
import time

historico_depositos = []
historico_saques = []
contador_de_saques = 0
contador_de_depositos = 0
numero_maximo_saques = 10
numero_maximo_depositos = 5
saldo = 0

#dicionário de clientes

clientes = {
    '463846792-21':{
        'nome': "Gustavo",
        'telefone': '122343232-3243',
        'ativo': True
    },
    '3456783210':{
        'nome': "Marquezine",
        'telefone': '127433434-3263',
        'ativo': True
    },
    '44027883829':{
        'nome': 'Seu Jorge',
        'telefone': '137433634-3243',
        'ativo': True
    }
}

# banco função sacar


def sacar():
    valor_saque = float(input('Digite o valor que você deseja sacar: '))
    
    if valor_saque > saldo and valor_saque <= 0:
        print('Valor requisitado não compatível com sua conta')
    
    elif contador_de_saques > numero_maximo_saques:
        print('Você excedeu a quantidade de saques permitidos !!!')

    else:
        contador_de_saques += 1
        saldo -= valor_saque
    
        print('Seu saque foi concluído')

# banco função depositar

def depositar():
    valor_deposito = float(input('Digite o valor que deseja depositar'))
    if valor_deposito > numero_maximo_depositos:
        print('Você ultrapassou o limite de depositos do dia')
    elif contador_de_depositos > numero_maximo_depositos:
        print('Voxê excedeu o limite de depositos do dia')

    else: 
        saldo += valor_deposito
        contador_de_depositos += 1
        print('Seu deposito foi concluido com seucesso')

# banco função Extrato

def Extrato():
    print('Você escolheu a função Extrato')
    print(f'Você já efetuou {contador_de_saques} até o momento')
    print(f'Seu saldo atual é {saldo:.2f}\n\n')

    if historicoSaques:
        print("Histórico de saques:")
        for i, saque in enumerate(historico_Saques, 1):
            print(f"Saque {i}: R${saque:.2f}")
        print("\n")
    if historicoDespositos:
        print("Histórico de depósitos:")
        for i, deposito in enumerate(historico_Despositos, 1):
            print(f"Depósito {i}: R${deposito:.2f}")
        print("\n")

# banco função Criar usuário

def Criar_usuario():
    print('Criar usuário ')
    usuario_cpf =input('Insira o cpf: ')
    usuario_nome =input('Insira o nome: ')
    usuario_tel =input('Insira o telefone: ')

    usuarios = []

    usuarios.append(usuario_cpf)
    usuarios.append(usuario_nome)
    usuarios.append(usuario_tel)


    print('Qual conta deseja vincular ao usuário')