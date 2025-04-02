menu = """
    
[1] Depositar 
[2] Sacar 
[3] Extrato
[4] Sair

=>  """

saldo = 0 
limite = 500
extrato = ""
numero_saques = 0 
LIMITE_SAQUES = 3

while True: 

    opcao = input(menu)

    if opcao == "1":

        valor = float(input("Informe o valor do depósito: "))

        if valor < 0:
            print("Depósito inválido! O valor precisa ser positivo.")
        else:
            saldo += valor
            extrato += f"Depósito: +R$ {valor:.2f}\n"
            print(f"Depósito de R$ {valor:.2f} realizado com sucesso!")

    elif opcao == "2":
        valor = float(input("Informe o valor do Saque: "))

        if saldo <= 0:
            print("Saldo insuficiente para saque")
        elif numero_saques > LIMITE_SAQUES:
            print("Numero de Saques excedidos")
        elif valor > limite:
            print("Valor do saque acima do limite")
        elif valor > saldo : 
            print("Saldo insuficiente para essa transação")
        else:
            saldo -= valor
            numero_saques += 1
            extrato += f"Saque: -R$ {valor:.2f}\n"  # Adiciona ao extrato
            print(f"Saque de R$ {valor:.2f} realizado com sucesso!")
        


    elif opcao == "3":
        print("\nEXTRATO".center(30, "-"))
        print(extrato if extrato else "Nenhuma Transação realizada")
        print("-" * 30)
        print(f"Saldo atual: R$ {saldo:.2f}")
    
    elif opcao == "4":
        print("Saindo... Obrigado por utilizar nosso banco!")
        break

    else:
        print("Opção inválida! Escolha uma opção entre 1 e 4.")