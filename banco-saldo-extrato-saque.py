print("Seja bem Vindo ao Banco Python!")

saldo = 0
contadorSaques = 0
limiteDeSaques = 3

historicoSaques = []

historicoDespositos = []

while True:
    opcao = int(input("Escolha uma opção:\n[1]Sacar | [2]Extrato |\n[3]Depositar | [0]Sair\n"))

    if opcao == 1:
        print("Você escolheu a opção Sacar.")
        valor_saque = float(input("Digite o valor que deseja sacar: R$"))

        if valor_saque > saldo:
            print("Saldo insuficiente para saque.\n\n")


        elif valor_saque <= 0:
            print("Valor inválido para saque.\n\n")

        elif contadorSaques > limiteDeSaques:
            print("Limite de saques diários excedido.\n\n")


        elif valor_saque > 500:
            print("Valor máximo de saque é R$500,00.\n\n")


        else:
            saldo -= valor_saque
            contadorSaques += 1
            historicoSaques.append(valor_saque)
            print(f"Saque de R${valor_saque:.2f} realizado com sucesso.\n\n")
        
        



    elif opcao == 2:
        print("Você escolheu a opção Extrato.")
        print("Você já realizou {} saques hoje.".format(contadorSaques))
        print(f"Seu saldo atual é: R${saldo:.2f}\n\n")
        if historicoSaques:
            print("Histórico de saques:")
            for i, saque in enumerate(historicoSaques, 1):
                print(f"Saque {i}: R${saque:.2f}")
            print("\n")
        if historicoDespositos:
            print("Histórico de depósitos:")
            for i, deposito in enumerate(historicoDespositos, 1):
                print(f"Depósito {i}: R${deposito:.2f}")
            print("\n")
    

    elif opcao == 3:
        print("Você escolheu a opção Depositar.")
        valor_deposito = float(input("Digite o valor que deseja depositar: R$"))

        if valor_deposito <= 0:
            print("Valor inválido para depósito.\n\n")


        else:
            saldo += valor_deposito
            historicoDespositos.append(valor_deposito)
            print(f"Depósito de R${valor_deposito:.2f} realizado com sucesso.\n\n")
         


    elif opcao == 0:
        print("Obrigado por usar o Banco Python. Até logo!")
        break    
    else:
        print("Opção inválida. Tente novamente.\n\n")
