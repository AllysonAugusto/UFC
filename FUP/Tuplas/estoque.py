'''
Crie um programa que recebe uma lista de tuplas, onde cada tupla contém o nome 
de um produto e sua quantidade em estoque. O programa deve calcular e exibir o total de produtos em estoque.
'''

estoque = ()

# Loop até que o usuário pressione Enter sem digitar nenhum nome de produto
while True:
    produto = input('Digite o nome do produto (ou deixe em branco para sair): ')
    if not produto: #se entrada é numerica
        break
    if produto == '':
        break

    # Verificação de entrada numérica
    try:
        quantidade_produto = int(input(f'Digite a quantidade do(a) {produto}: '))
        
    except ValueError: 
        print('ERROR: A quantidade deve ser um número inteiro.')
        continue

    # Verificação de quantidade positiva
    if quantidade_produto <= 0:
        print('ERROR: A quantidade do produto deve ser maior que zero.')
        continue

    estoque += ((produto, quantidade_produto),)
    print('Informações adicionadas com sucesso!')

# Calcular o total de produtos em estoque
total_estoque = 0

for _, quantidade in estoque: 
    total_estoque += quantidade

# Exibir o total de produtos em estoque
print(f'O total de produtos em estoque é: {total_estoque}')


titulo = "TABELA DE PRODUTOS"

# Calcula o número de espaços necessários para centralizar o título
espacos = (80 - len(titulo)) // 2

# Imprime os espaços seguidos do título
print("-" * 70)
print(" " * espacos + titulo)
print("-" * 70)

# Imprimir cabeçalho
print("Produto\t\tQuantidade") #espaço equivalente ao tamanho de duas tabulações
print("-" * 30)

# Iterar sobre os itens do estoque e imprimir cada um
for produto, quantidade in estoque:
    print(f"{produto}\t\t{quantidade}")

# Imprimir linha divisória entre produtos e quantidades
print("-" * 30)