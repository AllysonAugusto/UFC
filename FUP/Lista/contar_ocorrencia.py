"""
Escreva um programa em Python que solicite ao usuário que insira uma lista de números inteiros. 
O programa deve determinar o maior valor na lista e imprimir todas as ocorrências desse valor na 
lista, juntamente com suas posições.

Entrada:

    A entrada consiste em uma linha contendo uma lista de números inteiros separados por espaços.

Saída:

    A saída deve ser uma mensagem indicando o maior valor na lista, seguida pelas posições em que esse valor ocorre na lista.

Exemplo de entrada e saída:

Entrada:

5 8 2 10 8 3 8

Saída:

less

O maior valor é 10
Ocorrências do maior valor: [10] nas posições [3]

"""

n = int(input("Digite o tamanho da lista: "))
lista = []

for i in range(n):
    number = int(input("Digite um número: "))
    lista.append(number)
    i+=1

maior_valor = lista[0] #inicializa a comparação com 0
indice_maior_valor = [] #guardar o indice, permitindo armazenar múltiplos índices
for i, elemento in enumerate (lista):
    if elemento > maior_valor:
        maior_valor = elemento #colocando o maior valor dentro da variavel maior_valor
        indice_maior_valor = [i] #recebendo o indice do maior
    elif elemento == maior_valor:
        indice_maior_valor.append(i)  # Adiciona o índice à lista de índices do maior valor
        

print("Ocorrência do maior valor: {} nas posições {}".format(maior_valor, indice_maior_valor))

"""
--ALTERNATIVA--:
maior_valor = max(lista)
indice_maior_valor = lista.index(maior_valor)
"""