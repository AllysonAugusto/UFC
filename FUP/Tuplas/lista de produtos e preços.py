# Inicializando a tupla vazia
listagem = ()

while True:
    print("-" * 40)
    print("{:^40}".format("LISTAGEM DE PREÇOS"))
    print("-" * 40)

    # Exibindo os produtos e preços
    for produto, preco in listagem:
        print(f'{produto:.<30} R$ {preco:>7.2f}')

    print("-" * 40)

    # Perguntando ao usuário se deseja adicionar mais produtos
    continuar = input("Deseja adicionar mais produtos? (S/N): ").strip().upper()
    if continuar != 'S':
        break

    # Solicitando ao usuário que digite o nome e o preço do novo produto
    produto = input("Digite o nome do produto: ")
    preco = float(input("Digite o preço do produto: "))

    # Atualizando a tupla com o novo produto e preço
    listagem += ((produto, preco),)

# Mensagem de encerramento
print("Fim do programa. Obrigado por utilizar!")
