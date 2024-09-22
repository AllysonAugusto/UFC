"""
Crie um programa em Python chamado "Encontrando Ocorrências" que permite ao usuário preencher uma lista de elementos e encontrar as ocorrências de uma palavra dentro de um intervalo específico de índices da lista.
Para isso, implemente uma função denominada "encontrar_ocorrencias" que recebe como parâmetros a lista de elementos, a palavra a ser pesquisada, o índice inicial e o índice final do intervalo desejado na lista. Essa função retorna uma lista contendo os índices onde a palavra ocorre dentro do intervalo especificado.
"""

def encontrando_ocorrencias(lista, palavra, indice_inicial, indice_final):
    ocorrencia_indices = [] # guardar os indices na lista
    qnt_vezes = 0

    for indice in range(indice_inicial, indice_final + 1): #começando do indice_inicial até o indice_final
        if lista[indice] == palavra:
            ocorrencia_indices.append(indice)
            qnt_vezes += 1
    return ocorrencia_indices, qnt_vezes


#Lista de palavra
lista = []

#Quantidade e os proprios elementos
n = int(input("Digite a quantidade de elementos: "))
for i in range(n):
    elementos = input(f"Digite o {i+1} elemento: ")
    lista.append(elementos)

#Palavra a ser pesquisada
palavra = input("Digite a palavra: ")

#Indice inicial e final
indice_inicial = int(input("Digite o indice inicial: "))
indice_final = int(input("Digite o indice final: "))

ocorrencia_indices, qnt_vezes = encontrando_ocorrencias(lista, palavra, indice_inicial, indice_final)

# Exibir as ocorrências encontradas
print("Ocorrências da palavra '{}' {}x entre os índices {} e {}:".format(palavra, qnt_vezes, indice_inicial, indice_final))
if qnt_vezes > 0:
    for ocorrencia in ocorrencia_indices:
        print("Índice:", ocorrencia)
else:
    print("Nenhuma ocorrência encontrada.")
