from datetime import datetime 

import time

saques = 0

saldo = 0.0
saques_realizados = []
depositos_realizados = []
limite_saques = 10

print("Bem-vindo ao Banco com TADA!")
while True:
    print("\nEscolha uma opção:")
    print("[1] Sacar")
    print("[2] Extrato")
    print("[3] Depositar")
    print("[0] Sair")

    opcao = input("Digite a opção desejada: ")

    if opcao == "1":
        if saques >= limite_saques:
            print("Limite de saques diários atingido.")
            continue

        valor_saque = float(input("Digite o valor que deseja sacar: R$"))
        if valor_saque > saldo:
            print("Saldo insuficiente para saque.")
        elif valor_saque <= 0:
            print("Valor inválido para saque.")
        else:
            saldo -= valor_saque
            saques += 1
            data_hora = datetime.now().strftime("%d/%m/%Y %H:%M")
            saques_realizados.append((valor_saque, data_hora))
            print(f"Saque de R${valor_saque:.2f} realizado com sucesso no dia {data_hora}.")

    elif opcao == "2":
        print(f"Saldo atual: R${saldo:.2f}")
        print(f"Saques realizados hoje: {saques}")
        if saques_realizados:
            print("Histórico de saques:")
            for valor, data_hora in saques_realizados:
                print(f"  - R${valor:.2f} em {data_hora}")

    elif opcao == "3":
        valor_deposito = float(input("Digite o valor que deseja depositar: R$"))
        if valor_deposito <= 0:
            print("Valor inválido para depósito.")
        else:
            saldo += valor_deposito
            data_hora = datetime.now().strftime("%d/%m/%Y %H:%M")
            depositos_realizados.append((valor_deposito, data_hora))
            print(f"Depósito de R${valor_deposito:.2f} realizado com sucesso no dia {data_hora}.")

    elif opcao == "0":
        print("Obrigado por usar o Banco com TADA! Até logo!")
        break

    else:
        print("Opção inválida. Por favor, escolha uma opção válida.")