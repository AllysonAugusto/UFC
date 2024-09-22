"""
Encontrar Menor, Maior e Ocorrências
Escreva uma função em Python chamada encontrar_menor_maior_ocorrencias que solicita 
ao usuário uma quantidade de números e, em seguida, pede que ele digite esses números. 
A função então determina o menor e o maior número digitado, bem como o número de ocorrências 
de cada um deles na lista.
"""

def encontrar_menor_maior_ocorrencias ():
    #lista vazia pra armazenar numeros digitados
    list = []
    n = int(input("Digite a quantidade de numeros: "))

    #pedindo pra digitar e adicionando na list
    for i in range(n):
        numbers = int(input(f"Digite o {i+1} número: "))
        list.append(numbers)

        #Inicializadores de comparação - primeiro elemento da lista
        maior = menor = list[0]

        for elemento in list:
            if elemento > maior:
                maior = elemento
            if elemento < menor:
                menor = elemento
        
    return maior, menor

encontrar_valor = encontrar_menor_maior_ocorrencias()
print("Maior e menor valores", encontrar_valor)
