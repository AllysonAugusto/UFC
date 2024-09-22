"""
Desenvolva um programa em Python que permita encontrar a posição de um número em uma lista. A entrada consistirá na quantidade de elementos da lista seguida pelos próprios elementos. Após isso, o programa solicitará a chave que deseja encontrar na lista e imprimirá sua posição.

Além disso, implemente uma função chamada "busca" que recebe uma lista e uma chave como parâmetros e retorna a posição da chave na lista, se encontrada, ou -1 caso contrário. Essa função deve ser capaz de fazer a mesma operação que o programa principal.
"""

def posicao_numero():

    list = []
    n = int(input("Digite a quantidade de números: "))

    for i in range(n):
        numbers = int(input(f"Digite o {i+1} elemento: "))
        list.append(numbers)

    chave = int(input("Digite a chave que deseja encontrar: "))
    for i, elemento in enumerate (list): 
        if chave == elemento:
            indice = i
            print("\nElemento encontrado!")
            print("O {} está na posição {}".format(elemento, indice))

    return elemento, indice

posicao_numero()


"""
def busca (l, chave):
    indice = -1 #indica que nao foi encontrada
    i = 0
    for i in l:
        if l[i] == chave: #se elemento atual é igual chave
            return i

    return -1

print (busca(l, chave))

"""