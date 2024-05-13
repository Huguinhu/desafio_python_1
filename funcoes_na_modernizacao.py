import random
import sys

usuarios = {}
limite_saque = 500.00
saldo = 2000.00
saques_diarios = 0  # Somente para contagem
maximo_saques = 3
transacoes = []

def cadastrar_conta(usuario, cpf):
    agencia = "0001"
    print("Gerando a sua conta corrente...")

    numeros = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    limite_digitos = 11

    conta_corrente = ''.join([str(random.choice(numeros)) for _ in range(limite_digitos)])
    print(f"""{usuario}, sua conta foi criada com sucesso!
    Abaixo seguem algumas informações sobre o seu cadastro:

    Nome: {usuario},
    Conta Corrente: {conta_corrente},
    Agencia: {agencia},

    """)

    usuarios[cpf] = {'agencia': agencia, 'conta_corrente': conta_corrente}

# Menu dos usuários:

def menu():
    while True:
        opcao = int(input(f"""Seja bem vindo!

        Por favor selecione uma opção válida:

        [1] Sacar
        [2] Depositar
        [3] Extrato
        [4] Sair
        [5] Criar conta

        """))

        if opcao == 1:
            sacar()

        elif opcao == 2:
            depositar()

        elif opcao == 3:
            historico_movimentacoes()

        elif opcao == 4:
            saida()

        elif opcao == 5:
            nova_conta()

        else:
            print("Por favor, selecione uma opção válida!")

# Validação de CPF:

def valida_cpf(cpf):
    cpf = ''.join(filter(str.isdigit, str(cpf)))

    if len(cpf) != 11 or cpf == cpf [0] * 11:
        return False

    cpf = list(map(int, cpf))
    calc_digit = lambda t: int(sum(t[i] * (len(t) + 1 - i) for i in range(len(t))) * 10 % 11) % 10
    if calc_digit(cpf[:9]) != cpf[9] or calc_digit(cpf[:10]) != cpf[10]:
        return False

    return True

# Cadastro dos usuários:

def cadastrar_usuario():
    global usuario, cpf

    usuario = str(input("Insira o seu nome e sobrenome: "))
    cpf = int(input("Insira o seu cpf (somente numero): "))

    if valida_cpf(cpf):
        if cpf in usuarios:
            print(f'Usuário {usuario} encontrado. Redirecionando para as opções.')

        else:
            print(f"""Não encontramos nenhum usuário com o CPF: {cpf} 🤔.

            ===================================================

            Deseja realizar o cadastro conosco {usuario}?

            [1] Sim
            [2] Não

            """)

            escolha = int(input())
            if escolha == 1:
                print("Maravilhoso! Iniciando cadastro...")

                nome_completo = input("Por favor, insira seu nome completo: ")
                email = input("Por favor, insira um email: ")
                celular = input("Insira seu numero de telefone: ")
                data_nascimento = input("Insira sua data de nascimento: ")
                rua = input(f"Possui o endereço de cor {usuario}? Vamos começar então!\nPor favor, insira sua rua: ")
                numero = input("Numero da residencia: ")
                bairro = input("Bairro: ")
                cidade = input("Cidade: ")

                usuarios[cpf] = {'nome': nome_completo, 'email': email, 'celular': celular, 'data_nascimento': data_nascimento, 'rua': rua, 'numero': numero, 'bairro': bairro, 'cidade': cidade}
                print(f'Usuário {nome_completo} cadastrado com sucesso!')

                cadastrar_conta(usuario, cpf)

            elif escolha == 2:
                print("Que pena! Espero ter você aqui um dia...")
                sys.exit()

            else:
                ("Favor escolher uma opção válida!")

    else:
        print(f'O CPF {cpf} não é válido.')

cadastrar_usuario()

# Função de saque:

def sacar():
    global saldo, saques_diarios, transacoes

    saque = float(input("Informe o valor a ser sacado: "))
    if saque >= saldo or saque > limite_saque:
        print("Saldo ou limite indisponível para saque.")
    elif saques_diarios == maximo_saques:
        print("Limite de saques diários excedido! Tente novamente amanhã.")
    else:
        print(f"Retire o valor de {saque} na boca do caixa...")
        transacoes.append(f"Saque no valor de {saque}")
        saques_diarios += 1
        saldo -= saque
        print(f"Valor atual disponível de: {saldo}")
        

# Função de depósito:

def depositar():
    global saldo, transacoes

    deposito = float(input("""Insira o valor a ser depositado:
    """))
    saldo += deposito
    transacoes.append(f"Deposito de R$ {deposito}")
    print(f"""Valor atual disponível de: {saldo}""")

# Função de extrato:

def historico_movimentacoes():
    print("""Exibindo o histórico de movimentacoes da sua conta: """)
    print("Não foi realizada nenhuma transacao ate o momento..." if not transacoes else transacoes)
    return transacoes

def saida():
    sys.exit()

def nova_conta():
    cadastrar_conta(usuario, cpf)

menu()
