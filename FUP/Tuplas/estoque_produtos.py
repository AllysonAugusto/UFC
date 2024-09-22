# Função para adicionar um novo produto ao estoque
def adicionar_produto(estoque):
    nome = input("Digite o nome do produto: ")
    preco = float(input("Digite o preço do produto: "))
    quantidade = int(input("Digite a quantidade em estoque: "))
    fornecedor = input("Digite o nome do fornecedor: ")
    data_entrada = input("Digite a data de entrada (DD/MM/AAAA): ")
    novo_produto = (nome, preco, quantidade, fornecedor, data_entrada) #criando uma tupla 
    estoque.append(novo_produto) #tupla é adicionada à lista estoque
    print("Produto adicionado ao estoque com sucesso!")

# Função para atualizar a quantidade de um produto no estoque
def atualizar_estoque(estoque):
    nome_produto = input("Digite o nome do produto que deseja atualizar: ")
    for produto in estoque:
        if produto[0] == nome_produto:  #buscando o produto se o nome satisfazer ao 'nome_produto'
            nova_quantidade = int(input("Digite a nova quantidade em estoque: "))
            produto[2] = nova_quantidade
            print("Estoque atualizado com sucesso!")
            return
    print("Produto não encontrado no estoque.")

# Função para exibir todos os produtos em estoque
def exibir_estoque(estoque):
    print("\nLista de Produtos em Estoque:")
    print("-" * 90)
    print(f"{'Nome':<20} {'Preço':<10} {'Quantidade':<15} {'Fornecedor':<20} {'Data de Entrada':<15}")
    print("-" * 90)
    for produto in estoque:
        print(f"{produto[0]:<20} R$ {produto[1]:<10.2f} {produto[2]:<15} {produto[3]:<20} {produto[4]:<15}")
    print("-" * 90)

# Função para calcular o valor total do estoque
def calcular_valor_total(estoque):
    total = sum(produto[1] * produto[2] for produto in estoque)
    print(f"O valor total do estoque é: R$ {total:.2f}")

# Função principal
def main():
    estoque = []  # Lista para armazenar os produtos em estoque para armazenar múltiplos produtos em uma única estrutura de dados. Cada produto é representado por uma tupla contendo várias informações, como nome, preço, quantidade em estoque, fornecedor e data de entrada.
    while True:
        print("\n1. Adicionar Produto")
        print("2. Atualizar Estoque")
        print("3. Exibir Estoque")
        print("4. Calcular Valor Total do Estoque")
        print("5. Sair")
        opcao = input("\nEscolha uma opção: ")
        if opcao == "1":
            adicionar_produto(estoque)
        elif opcao == "2":
            atualizar_estoque(estoque)
        elif opcao == "3":
            exibir_estoque(estoque)
        elif opcao == "4":
            calcular_valor_total(estoque)
        elif opcao == "5":
            print("Saindo...")
            break
        else:
            print("Opção inválida. Tente novamente.")

# Executar o programa
if __name__ == "__main__": #verifica se o código está sendo executado como o programa principal
    main()
