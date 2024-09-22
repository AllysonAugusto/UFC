"""
função que solicita ao usuário o peso de várias pessoas e armazena esses valores em uma lista. Em seguida, a função determina o maior e o menor peso entre os valores fornecidos, bem como a posição do menor peso na lista.
"""


# Função para encontrar o maior e menor peso

def encontrar_maior_menor():
    
    # Inicialização dos valores de maior e menor com o primeiro elemento da lista
    lista = []
    num_pessoas = int(input("Digite a quantidade de pessoas: "))
    

    #Entrada dos pesos e armazenando na lista
    for i in range (num_pessoas):
        peso = float(input(f"Digite o peso da pessoa {i+1}: "))
        lista.append(peso)

    # Inicialização dos valores de maior e menor com o primeiro elemento da lista
    maior = menor = lista[0]
    indice_maior = indice_menor = 0 

    for i, peso in enumerate(lista):
        if peso > maior:
            maior = peso
            indice_maior = i
        if peso < menor:
            menor = peso
            indice_menor = i
    return maior, menor, indice_maior, indice_menor


#chamando funcao
maior_peso, menor_peso, indice_maior, indice_menor = encontrar_maior_menor()
print(f'O maior peso foi {maior_peso} na posição {indice_maior}.')
print(f'O menor peso foi {menor_peso} na posição {indice_menor}.')


        
    