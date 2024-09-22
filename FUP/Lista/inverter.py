"""
Escreva uma função em Python chamada inverter_vetor() que solicita ao 
usuário que insira o número de elementos de um vetor, seguido pelos 
elementos do vetor. A função deve inverter o vetor e retornar o vetor invertido.
"""

def inverter_vetor():
    # Lê o número de elementos do vetor
    num_elementos = int(input("Digite o número de elementos: "))

    # Lê os elementos do vetor
    vetor = []
    for _ in range(num_elementos):
        elemento = int(input("Digite um elemento: "))
        vetor.append(elemento)

    #inverter o vetor
    vetor_invertido = vetor[::-1]
    return vetor_invertido


vetor_invertido = inverter_vetor()

print(vetor_invertido)
