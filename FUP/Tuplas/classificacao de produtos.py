"""
Classificação de Produtos:

Implemente um programa que permite classificar produtos com base em seus tipos, como eletrônicos, vestuário, alimentos, entre outros. O programa deve solicitar ao usuário informações sobre cada produto, incluindo seu nome e tipo. Em seguida, ele deve armazenar essas informações em um dicionário, onde as chaves são os tipos de produtos e os valores são listas de produtos pertencentes a cada categoria.

Além disso, o programa deve calcular quantos produtos pertencem a cada categoria e exibir essas informações ao usuário.

Por exemplo, após inserir informações sobre vários produtos, o programa deve ser capaz de informar quantos produtos de eletrônicos, quantos de vestuário, quantos de alimentos, e assim por diante.

Implemente esse programa considerando os seguintes pontos:

    Solicite ao usuário que insira o número de produtos a serem classificados.
    Para cada produto, solicite seu nome e seu tipo.
    Armazene as informações em um dicionário, onde as chaves são os tipos de produtos e os valores são listas de produtos pertencentes a cada categoria.
    Após inserir todas as informações dos produtos, calcule quantos produtos pertencem a cada categoria.
    Exiba essas informações ao usuário de forma organizada.
"""

# Inicializa a variável 'produto' como uma string vazia
produto = ' '

# Inicializa um dicionário vazio para armazenar os produtos classificados por tipo
produtos = {}

# Inicia um loop que continuará enquanto o usuário continuar inserindo nomes de produtos
# O loop será interrompido quando o usuário pressionar Enter sem digitar nenhum nome de produto
while produto != '':

    # Solicita ao usuário o nome do produto
    try:
        produto = input("Digite o nome do produto (ou pressione <enter> para sair): ")
        
        # Verifica se o usuário pressionou Enter sem digitar nada
        if produto == '':
            break

        # Solicita ao usuário o tipo do produto
        tipo = input("Digite o tipo do produto: ")

        # Verifica se o tipo já existe como uma chave no dicionário 'produtos'
        if tipo in produtos:
            # Se o tipo já existir no dicionário, o nome do produto é adicionado à lista de produtos desse tipo
            produtos[tipo].append(produto)
        else:
            # Se o tipo não existir no dicionário, é criada uma nova entrada com o tipo como chave e uma lista contendo o nome do produto como valor
            produtos[tipo] = [produto]
    
    # Captura qualquer exceção que ocorra durante a execução do bloco de código dentro do 'try'
    except Exception as e:
        print("Ocorreu um erro:", e)

# Exibe uma mensagem indicando que os produtos serão listados por tipo
print("\nProdutos classificados por tipo:")

# Itera sobre os itens do dicionário 'produtos', onde 'tipo' é a chave (ou tipo de produto) e 'lista_produtos' é a lista de produtos desse tipo
for tipo, lista_produtos in produtos.items():
    # Exibe o tipo de produto com a primeira letra em maiúscula
    print(f"\n{tipo.capitalize()}:")
    
# Lista vazia para armazenar os tipos de produtos já processados
tipos_processados = []

# Exibe uma mensagem indicando que os produtos serão listados por tipo
print("\nProdutos classificados por tipo:\n")

# Exibe os títulos das tabelas fora do loop
print(f"{'Nome do Produto':<20}{'Tipo':<20}")
print("-" * 40)

# Itera sobre os itens do dicionário 'produtos', onde 'tipo' é a chave (ou tipo de produto) e 'lista_produtos' é a lista de produtos desse tipo
for tipo, lista_produtos in produtos.items():
    # Verifica se o tipo atual já foi processado
    if tipo not in tipos_processados:
        # Adiciona o tipo atual à lista de tipos processados
        tipos_processados.append(tipo)
        
        # Exibe o tipo de produto com a primeira letra em maiúscula
        print(f"\n{tipo.capitalize()}:\n")
        
        # Itera sobre cada produto na lista de produtos do tipo atual
        for produto in lista_produtos:
            # Exibe o nome do produto e o tipo
            print(f"{produto:<20}{tipo.capitalize():<20}")
