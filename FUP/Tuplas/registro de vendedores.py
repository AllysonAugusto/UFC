"""
Registro de Vendedores

Você foi designado para criar um programa que irá ajudar uma loja a registrar informações sobre seus vendedores. O programa deve solicitar ao usuário o número de vendedores na loja e, em seguida, coletar as seguintes informações para cada vendedor:

    Nome do vendedor
    Idade do vendedor
    Tempo de serviço do vendedor (em meses)

Após coletar essas informações para cada vendedor, o programa deve calcular e exibir algumas estatísticas, incluindo:

    A idade média dos vendedores na loja.
    O tempo médio de serviço dos vendedores na loja.
    O vendedor mais jovem e mais antigo na loja.
    O vendedor com o menor e maior tempo de serviço na loja.

Além disso, o programa deve permitir ao usuário visualizar os detalhes de um vendedor específico, fornecendo seu nome como entrada.

"""

num_clientes = int(input("Digite o número de vendedores na loja: "))

vendedores = {}  # Dicionário vazio para armazenar informações sobre os vendedores

for i in range(num_clientes):
    nome = input(f'Digite o nome do vendedor {i+1}:')
    vendedores[nome] = {} # Subdicionário para armazenar informações adicionais
    idade = int(input(f"Digite a idade do vendedor {i+1}: "))
    vendedores[nome]['idade'] = idade # Adiciona a idade ao subdicionário do vendedor
    tempo_servico = int(input("Digite o tempo de serviço (em meses): "))
    vendedores[nome]['tempo_servico'] = tempo_servico

print("\nRegistro de vendedores concluído!")
print("\nInformações dos vendedores:")

print(f"{'Nome:':<15} {'Idade:':<10} {'Tempo de Serviço (meses)':<25}")
print("-" * 50)

for nome, info in vendedores.items(): #iterar sobre cada par chave-valor
    print(f"{nome:<15} {info['idade']:<10} {info['tempo_servico']:<25}")