"""
Escreva um programa em Python chamado "Ordenar_e_Imprimir_Índices" que solicita ao usuário que insira o tamanho de um vetor de inteiros e, em seguida, os próprios elementos desse vetor. O programa deve ordenar o vetor em ordem crescente e imprimir os elementos ordenados juntamente com os índices originais correspondentes.

O programa deve conter uma função chamada "ordenar_e_imprimir_indices" que recebe o vetor como parâmetro e realiza a ordenação, mantendo os índices originais. Em seguida, essa função imprime o vetor ordenado e os índices originais.
"""

def Ordenar_e_Imprimir_Indices(vetor):
    
    indices = list(range(len(vetor)))
    for i in range(len(vetor)):
        for j in range(i+1, len(vetor)):
            if vetor[j] < vetor[i]:
                vetor[i], vetor[j] = vetor[j], vetor[i]
                indices[j], indices[i] = indices[j], indices[i]

    print("Vetor ordenado: ", vetor)
    print("Vetor original: ", indices)

#Lista para armazenar valores    
vetor = []

#Quantidade de números para digitar
n = int(input("Digite a quantidade de números que deseja: "))


for i in range (n):
    number = int(input(f"Digite o {i+1} número: "))
    vetor.append(number)

Ordenar_e_Imprimir_Indices(vetor)