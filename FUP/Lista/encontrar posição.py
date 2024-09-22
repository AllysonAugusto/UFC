"""
Escreva um programa em Python chamado "Encontrar_Posicao" que permite ao usuário encontrar a posição de um elemento em uma lista. O programa deve solicitar ao usuário que insira os elementos da lista separados por vírgulas e o número que deseja procurar. Em seguida, ele deve encontrar e imprimir todas as posições em que o número ocorre na lista.

"""

def Encontrar_posicao():
    
    # Solicitar ao usuário os elementos da lista separados por vírgula
    entrada = input("Digite os elementos separados por vírgula: ")
    numbers = [int(num) for num in entrada.split(',')] # Converter cada string na lista resultante em um número inteiro
    
    # Número que deseja procurar
    numero_procura = int(input("Digite qual número deseja procurar: "))
    
    # Lista para armazenar os índices do elemento encontrado
    indices_encontrados = []
    for indice, elemento in enumerate(numbers):
        if elemento == numero_procura:
            indices_encontrados.append(indice)

    return indices_encontrados



indices = Encontrar_posicao()

if indices:
    print("O número foi encontrado nas seguintes posições: ", indices)
else:
    print("O número não foi encontrado na lista.")