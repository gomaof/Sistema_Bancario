span = '=+'*12
menu = f"""
{span} MENU {span}
    Escolha uma das opções abaixo

[1] Depositar
[2] Sacar
[3] Extrato
[0] Sair

{span}{span}
"""

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    opcao = input(menu)

    if opcao == "1":
        valor = float(input("Digite o valor que deseja depositar: "))
        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"
        else:
            print("A operação falhou! O valor informado é inválido.")
    
    
    elif opcao == "2":
        valor = float(input("Digite o valor que deseja sacar: "))
        excedeu_saldo = valor > saldo
        excedeu_limite = valor > limite
        excedeu_saque = numero_saques >= LIMITE_SAQUES

        if excedeu_saldo:
            print("Sua solicitação de saque FALHOU! Você não tem saldo suficiente.")
        elif excedeu_limite:
            print("Sua solicitação de saque FALHOU! Você atingiu o limite de saque diário.")
        elif excedeu_saque:
            print("Sua solicitação de saque FALHOU! Quantidade máxima de saques atingidas.")
        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saques += 1
        else:
            print("A operação falhou! O valor informado é inválido.")

    elif opcao == "3":
        print(f"\n{span} Extrato {span}")
        print("Não houve movimentação realizadas na conta até o momento." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print(span, span)
    
    elif opcao == "0":
        print("\nOperação Finalizada, até a próxima\n")
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")
