"""
Desenvolva um programa em Python chamado "Calcular_Soma_Maior_Menor" que recebe duas listas de números inteiros de mesmo tamanho como entrada e retorna a soma do maior e do menor elemento dessas listas. A função calcular_soma_maior_menor(lista1, lista2) deve ser implementada para realizar esse cálculo.

A função calcular_soma_maior_menor(lista1, lista2) recebe como parâmetros duas listas de números inteiros, lista1 e lista2, de mesmo tamanho, e retorna a soma do maior e do menor elemento dessas listas.
"""


def Calcular_Soma_Maior_Menor():
    n = int(input("Digite o tamanho das listas: "))

    lista1 = []
    lista2 = []
    nova_lista__com_maiores = []

    for listando1 in range(n):
        number_lista1 = int(input(f"Digite o número {listando1+1} da lista 1:"))
        lista1.append(number_lista1)

    for listando2 in range(n):
        number_lista2 = int(input(f"Digite o número {listando2+1} da lista 1:"))
        lista2.append(number_lista2)

    # Encontrar o maior elemento manualmente e Inicializar as variáveis para o maior e o menor elemento
    maior_lista1 = lista1[0]
    for num in lista1:
        if num > maior_lista1:
            maior_lista1 = num
    
    maior_lista2 = lista2[0]
    for num in lista2:
        if num > maior_lista2:
            maior_lista2 = num

    # Encontrar o menor elemento manualmente
    menor_lista1 = lista1[0]
    for num in lista1:
        if num < menor_lista1:
            menor_lista1 = num
    
    menor_lista2 = lista2[0]
    for num in lista2:
        if num < menor_lista2:
            menor_lista2 = num

    soma_maior = maior_lista1 + maior_lista2
    soma_menor = menor_lista1 + menor_lista2

    return soma_maior, soma_menor

# Chamada da função
soma_maior, soma_menor = Calcular_Soma_Maior_Menor()
print("A soma do maior elemento das duas listas é:", soma_maior)
print("A soma do menor elemento das duas listas é:", soma_menor)








'''

---ALTERNATIVA---

    maior_numero = max(lista1)
    maior_numero2 = max(lista2)
    menor_numero = min(lista1)
    menor_numero2 = min(lista2)

    soma_maior = maior_numero + maior_numero2
    soma_menor = menor_numero + menor_numero2

    return soma_maior, soma_menor

# Chamada da função
soma_maior, soma_menor = Calcular_Soma_Maior_Menor()
print("A soma do maior elemento das duas listas é:", soma_maior)
print("A soma do menor elemento das duas listas é:", soma_menor)
'''