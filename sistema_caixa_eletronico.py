import sys #O import do sys serviria para que, no final do programa, encerrasse completamente. Mas optei pelo break

saldo = 2000.00       
limite_saque = 500.00
saques_diarios = 0
maximo_saques = 3

while True: #Pesquisei um pouco e vi que while true se torna um loop infinito que só pode ser finalizado por alguma interação
    opcao = int(input(f"""          Seja bem vindo a central Bravesco!
          ----------------------------------------------
            Por favor, selecione uma das opcoes abaixo:
            [1] Saque     
            [2] Deposito
            [3] Extrato
            [4] Sair
          
          """))
    #achei muito interessante acessar as opções apenas mudando o tipo de variável. Bem simples
    if opcao == 1:  
        if saques_diarios < maximo_saques:
            saque = float (input("Informe o valor a ser sacado: "))

            if saque <= limite_saque and saque <= saldo:
                saldo -= saque
                saques_diarios += 1
                print(f"Retire o valor de R$ {saque:.2f} na boca do caixa...")
                print(f"Saldo atual R$ {saldo:.2f}")

            elif saque <= 0:
                print("Valor invalido. Tente um numero positivo e diferente de zero!")

            else:
                print("Saldo ou limite insuficiente para esta operação.")

        else:
            print("Limite de saques diarios atingidos!")

    elif opcao == 2:
        deposito = float (input("Informe o valor a ser depositado: "))
        if deposito > 0:
            saldo += deposito 
            print(f"Valor de R$ {deposito:.2f} depositado com sucesso!")
            print(f"Saldo atual: R$ {saldo:.2f}")
    
    elif opcao == 3: # Confesso que essa parte me bugou um pouco. Mas segui conforme o exemplo do Guilherme e deu tudo certo!
        print("\n ============EXTRATO============")
        print("Nao foram realizadas transações." if not extrato else extrato)
        print(f"\n Saldo: R$ {saldo:.2f}")
        print("====================================")

    else:
        print("          Obrigado por usar os nossos serviços!")
        print("          ======================================")
        print("          ☺")
        break
        




