"""
Dada uma lista de números inteiros, desenvolva um programa em Python chamado "Remover_Repetidos" que remova os elementos repetidos, mantendo apenas a primeira ocorrência de cada número. O programa deve solicitar ao usuário que insira a quantidade de números que deseja adicionar à lista e, em seguida, pedir que insira os números inteiros. Após isso, o programa deve imprimir a lista resultante, contendo apenas os elementos únicos.

O programa deve conter uma função chamada "verificar_numero" que recebe a lista como argumento e retorna uma nova lista contendo apenas os elementos únicos.

Exemplo de entrada/saída:
Digite a quantidade de números que deseja adicionar: 5
Digite os números inteiros: 3
Digite os números inteiros: 2
Digite os números inteiros: 3
Digite os números inteiros: 5
Digite os números inteiros: 2
Lista resultante: [3, 2, 5]
"""


def verificar_numero(lista):
    nova_lista = [] #Lista para armazenar valores unicos

    for number in lista:
        if number not in nova_lista:
            nova_lista.append(number)
    return nova_lista



# Pedir ao usuário a quantidade de elementos e preencher a lista
n = int(input("Digite a quantidade de elementos: "))

numeros = []
for i in range(n):
    number = int(input(f"Digite o {i+1} numero: "))
    numeros.append(number)


# Chamar a função para verificar e remover elementos repetidos
lista_sem_repeticao = verificar_numero(numeros)

# Exibir a lista resultante
print("Lista resultante:", lista_sem_repeticao)