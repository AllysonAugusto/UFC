"""
buscar uma chave em uma lista de números e imprimir a posição onde a chave foi encontrada
"""

chaves = []

# Solicitar ao usuário a quantidade de elementos na lista
n = int(input('Quantidade de números na lista: '))

for i in range(n):
    num = int(input(f"Digite o número {i+1}: "))
    chaves.append(num)

chave_busca = int(input("Qual chave deseja procurar? "))

for i, elemento in enumerate(chaves): #retornando índice-elemento
    if elemento == chave_busca:
        indice = i # Armazena o índice onde a chave foi encontrada
        break

# Imprimir a posição onde a chave foi encontrada
    
if i:
    print(f'A chave {elemento} está na posição {indice} da lista.')
else:
    print('A chave não foi encontrada na lista.')