def agrupar_por_idade(lista_pessoas):
    #Dicionario para agrupar pessoas por idade
    dicionario_idade = {}

    for nome, idade in lista_pessoas:
        # Se a idade não estiver no dicionário, adiciona com uma lista vazia
        if idade not in dicionario_idade:
            dicionario_idade[idade] = []
        # Adiciona o nome da pessoa à lista correspondente à sua idade
        dicionario_idade[idade].append(nome)
    return dicionario_idade

num_pessoas = int(input("Quantas pessoas deseja adicionar? "))
lista_pessoas = []


for _ in range (num_pessoas):
    nome = input("Digite o nome da pessoa: ")
    idade = int(input("Digite a idade da pessoa: "))

    # Adiciona uma tupla com o nome e idade à lista de pessoas
    lista_pessoas.append((nome, idade))


# Chama a função para agrupar pessoas por idade
resultado = agrupar_por_idade(lista_pessoas)

# Imprime o dicionário resultante que agrupa pessoas por idade
print("Pessoas agrupadas por idade:", resultado)