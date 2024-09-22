"""
Função somar_primeiro_ultimo: Esta função recebe uma lista como entrada e retorna a soma do primeiro e último elemento. Se a lista tiver menos de dois elementos, a função retorna a mensagem "A lista precisa ter pelo menos dois elementos.
"""
"""
Função somar_primeiro_ultimo: Esta função recebe uma lista como entrada e retorna a soma do primeiro e último elemento. Se a lista tiver menos de dois elementos, a função retorna a mensagem "A lista precisa ter pelo menos dois elementos.
"""
n = int(input("Digite o tamanho da lista: "))

# Listas
lista1 = []
lista2 = []
soma_das_listas = []

print("------PRIMEIRA LISTA------")
for listando1 in range(n):
    numeros_lista1 = int(input(f"Digite o {listando1+1} elemento para a primeira lista: "))
    lista1.append(numeros_lista1)

print("------SEGUNDA LISTA------")
for listando2 in range(n):
    numeros_lista2 = int(input(f"Digite o {listando2+1} elemento para a segunda lista: "))
    lista2.append(numeros_lista2)

# Somar o primeiro elemento da lista1 com o último elemento da lista2
for i in range(len(lista1)):
    soma_das_listas.append(lista1[i] + lista2[-1])

print(soma_das_listas)



"""
- VARIAÇÃO DE CÓDIGO
#o i-= 1 vai percorrer -1 elemento a cada loop, onde vai somar o primeiro elemento da lista 1 com os ultimos da lista2
percorrer_final = len (lista2) -1
i = 0
while i < len(lista1):
    soma_das_listas.append(lista1[i] + lista2[percorrer_final])
    percorrer_final -= 1 #seja percorrida de trás para frente
    i += 1

print (soma_das_listas)
'''

"""


