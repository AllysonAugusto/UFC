
"""
#Implemente um programa que recebe duas listas de inteiros de mesmo tamanho e crie uma nova lista onde os elementos dessa nova lista é soma dos elementos das duas listas, posição a posição. Ou seja, o primeiro elemento dessa nova lista será a soma dos primeiros elementos das duas listas de entrada. O segundo elemento será a soma dos segundos elementos das duas listas. E assim sucessivamente.

#ATENÇÃO: OBRIGATORIAMENTE VC DEVE CRIAR AS TRÊS LISTAS, AS DUAS PRIMEIRAS PARA ARMAZENAR AS LISTAS DE ENTRADA E A TERCEIRA COM O RESULTADO, SÓ AÍ VC VAI IMPRIMIR.
"""

#Listas
lista1 = []
lista2 = []
soma_listas = []

#Entrada
n = int (input('Digite o tamanho da lista: '))

print("------PRIMEIRA LISTA------")
for listando1 in range(n):
    numeros_lista1 = int(input(f"Digite o {listando1+1} elemento para a primeira lista: "))
    lista1.append(numeros_lista1)

print("------SEGUNDA LISTA------")
for listando2 in range(n):
    numeros_lista2 = int(input(f"Digite o {listando2+1} elemento para a segunda lista: "))
    lista2.append(numeros_lista2)

for i in range(len(lista1)):
    soma_listas.append(lista1[i] + lista2[i])
    
print(soma_listas)