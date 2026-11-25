
# SISTEMA DE VENDAS - TECHCELL

produtos = {
    1: ["Fone Bluetooth", 89.90],
    2: ["Carregador Turbo", 59.90],
    3: ["Cabo USB-C", 29.90],
    4: ["Suporte para Celular", 39.90],
    5: ["rx7600", 1.559,90],
    6: ["rx580 8gb ", 645,85]
}

carrinho = []

while True:

    print("\n==============================")
    print("          TECHCELL")
    print("==============================")
    
    print("1 - Ver produtos")
    print("2 - Comprar")
    print("3 - Ver carrinho")
    print("4 - Finalizar compra")
    print("5 - Sair")

    opcao = input(" Escolha uma opção: ")

    # VER PRODUTOS
    if opcao == "1":

        print("\n--- PRODUTOS ---")

        for numero, produto in produtos.items():
            print(numero, "-", produto[0], "- R$", produto[1])

    # COMPRAR
    elif opcao == "2":

        print("\n--- PRODUTOS ---")

        for numero, produto in produtos.items():
            print(numero, "-", produto[0], "- R$", produto[1])

        escolha = int(input("\nDigite o número do produto: "))

        if escolha in produtos:

            carrinho.append(produtos[escolha])

            print("Produto adicionado ao carrinho!")

        else:
            print("Produto não encontrado.")

    # CARRINHO
    elif opcao == "3":

        print("\n--- CARRINHO ---")

        if len(carrinho) == 0:

            print("Carrinho vazio.")

        else:

            total = 0

            for produto in carrinho:
                print("-", produto[0], "- R$", produto[1])
                total = total + produto[1]

            print("----------------")
            print("Total: R$", total)

    # FINALIZAR
    elif opcao == "4":

        if len(carrinho) == 0:

            print("\nO carrinho está vazio.")

        else:

            total = 0

            for produto in carrinho:
                total = total + produto[1]

            print("\n--- FINALIZAR COMPRA ---")

            nome = input("Digite seu nome: ")

            print("\nCompra realizada com sucesso!")
            print("Cliente:", nome)
            print("Total: R$", total)
            print("Obrigado por comprar na TechCell!")

            carrinho.clear()

    # SAIR
    elif opcao == "5":

        print("\nObrigado por usar a TechCell!")
        break

    else:

        print("\nOpção inválida.")
