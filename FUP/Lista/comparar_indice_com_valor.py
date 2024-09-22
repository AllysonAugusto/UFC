"""
Escreva um programa em Python que inicialize uma lista com os seguintes valores: [1, 2, 3, 4, 5]. Em seguida, solicite ao usuário que informe um índice dentro da lista e um valor para comparar com o elemento no índice especificado. O programa deve verificar se o índice fornecido está dentro dos limites da lista e, se estiver, comparar o elemento no índice com o valor especificado pelo usuário. Se o elemento no índice for maior que o valor fornecido, o programa deve imprimir "O índice {índice} é maior do que {valor}". Caso contrário, deve imprimir "O índice {índice} é menor do que o {valor}".
"""
def listas():
    lista1 = []
    lista2 = []

    # Lista onde o usuário vai digitar os seus números

    n1 = int(input("Digite a quantidade de elementos na lista 1: "))
    for _ in range(n1):
        number_user = int(input("Digite os números para a 1 lista: "))
        lista1.append(number_user)

    n2 = int(input("Digite a quantidade de elementos na lista 2: "))
    for _ in range(n2):
        number_user = int(input("Digite os números para a 2 lista: "))
        lista2.append(number_user)

    indice = int(input("Informe qual índice quer comparar: "))
    valor = int(input("Informe qual valor quer comparar com o índice: "))

    if indice < len(lista1) and indice < len(lista2):
        if lista1[indice] > valor:
            print("O índice {} é maior do que o valor {}.".format(lista1[indice], valor))
        elif lista2[indice] > valor:
            print("O índice {} é maior do que o valor {}.".format(lista2[indice], valor))
        else:
            print("O valor {} é maior do que o índice {} em ambas as listas.".format(valor, indice))
    else:
        print("ERRO: O índice fornecido está fora do intervalo válido para uma das listas.")


# Chamada da função
listas()











"""
  for i, elemento in enumerate(lista1):
        if i == indice:
            if elemento > valor:
                print("O índice {} da lista 1 é maior do que o valor {}.".format(indice, valor))
            else:
                print("O índice {} da lista 1 não é maior do que o valor {}.".format(indice, valor))

    for i, elemento in enumerate(lista2):
        if i == indice:
            if elemento > valor:
                print("O índice {} da lista 2 é maior do que o valor {}.".format(indice, valor))
            else:
                print("O índice {} da lista 2 não é maior do que o valor {}.".format(indice, valor))


"""