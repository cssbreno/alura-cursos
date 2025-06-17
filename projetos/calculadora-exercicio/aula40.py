"""Calculadora com While"""

while True:
    print("Selecione a operação:")
    print("1 - Soma")
    print("2 - Subtração")
    print("3 - Multiplicação")
    print("4 - Divisão")
    print("5 - Sair")

    opcao = input("Digite a opção: ")

    if opcao not in ['1', '2', '3', '4', '5']:
        print("Digite uma opção válida")
        print("--------------------------------")
        continue

    if len(opcao) > 1:
        print("Digite apenas uma opção.")
        continue

    if opcao == "5":
        print("Você saiu da calculadora")
        break

    try:
        entrada_numero_1 = input("Digite o primeiro número: ")
        entrada_numero_2 = input("Digite o segundo número: ")
        numero_1 = float(entrada_numero_1)
        numero_2 = float(entrada_numero_2)
    except ValueError:
        print("Erro: Digite um número válido.")
        continue

    if opcao == "1":
        print(f"{numero_1} + {numero_2} = {numero_1 + numero_2}")
    elif opcao == "2":
        print(f"{numero_1} - {numero_2} = {numero_1 - numero_2}")
    elif opcao == "3":
        print(f"{numero_1} * {numero_2} = {numero_1 * numero_2}")
    elif opcao == "4":
        if numero_2 == 0:
            print("Erro: divisão por zero não é permitida.")
        else:
            print(f"{numero_1} / {numero_2} = {numero_1 / numero_2}")

    sair = input("Deseja sair? [s]im ou [n]ão:").lower().startswith("s")

    if sair is True:
        print("Você saiu da calculadora")
        break
    elif sair is False:
        print("--------------------------------")
        continue
