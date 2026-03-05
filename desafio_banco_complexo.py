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
# banco função sacar


def sacar(){
    valor_saque = float(input('Digite o valor que você deseja sacar: '))
    
    if valor_saque > saldo and valor_saque <= 0:
        print('Valor requisitado não compatível com sua conta')
    
    elif contador_de_saques > numero_maximo_saques:
        print('Você excedeu a quantidade de saques permitidos !!!')

    else:
        contador_de_saques += 1
        saldo -= valor_saque
    
        print('Seu saque foi concluído')
        
}

def depositar(){
    valor_deposito = float(input('Digite o valor que deseja depositar'))
    if valor_deposito > numero_maximo_depositos:
        print('Você ultrapassou o limite de depositos do dia')
    elif contador_de_depositos > numero_maximo_depositos:
        print('Voxê excedeu o limite de depositos do dia')

    else: 
        saldo += valor_deposito
        contador_de_depositos += 1
        print('Seu deposito foi concluido com seucesso')

}

