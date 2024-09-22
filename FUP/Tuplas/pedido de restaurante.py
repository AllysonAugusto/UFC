def adicionar_pedido(pedidos):
    # Solicita ao usuário o número da mesa
    numero_mesa = input("Digite o número da mesa: ")
    
    # Solicita ao usuário os itens do pedido e os divide em uma lista
    itens = input("Digite os itens do pedido separados por vírgula: ").split(',')
    
    # Solicita ao usuário as quantidades de cada item e as divide em uma lista
    quantidades = input("Digite a quantidade de cada item separada por vírgula: ").split(',')
    
    # Cria um dicionário para representar o pedido, com as chaves 'numero_mesa', 'itens' e 'quantidades'
    pedido = {'numero_mesa': numero_mesa, 'itens': {}, 'quantidades': {}}
    
    # Adiciona os itens e suas quantidades ao dicionário do pedido
    for item, quantidade in zip(itens, quantidades): #iterar sobre os itens e suas quantidades ao mesmo tempo
        pedido['itens'][item] = quantidade #Acessa o dicionário de itens , usa o nome do item como chave para acessar ou adicionar o item e atribui a quantidade correspondente ao item dentro do dicionário de itens.
    
    # Adiciona o pedido à lista de pedidos
    pedidos.append(pedido)
    print("Pedido registrado com sucesso!")

def exibir_pedidos(pedidos):
    # Exibe a mensagem de cabeçalho para os pedidos registrados
    print("\nPedidos registrados:")
    
    # Itera sobre a lista de pedidos com um índice numérico (começando em 1)
    for i, pedido in enumerate(pedidos, start=1):
        # Obtém o número da mesa do pedido atual
        numero_mesa = pedido['numero_mesa']
        
        # Obtém os itens do pedido atual
        itens = pedido['itens']
        
        # Exibe o número da mesa do pedido
        print(f"Mesa {numero_mesa}:")
        
        # Itera sobre os itens do pedido atual
        for item, quantidade in itens.items():
            # Exibe cada item com sua respectiva quantidade
            print(f"- {quantidade}x {item}")
        
        # Adiciona uma linha em branco para separar os pedidos
        print()


def main():
    pedidos = []  # Lista para armazenar os pedidos
    while True:
        print("\n1. Adicionar Pedido")
        print("2. Exibir Pedidos")
        print("3. Sair")
        opcao = input("\nEscolha uma opção: ")
        if opcao == "1":
            adicionar_pedido(pedidos)
        elif opcao == "2":
            exibir_pedidos(pedidos)
        elif opcao == "3":
            print("Saindo...")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
