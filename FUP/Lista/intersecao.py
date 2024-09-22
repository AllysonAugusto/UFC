"""
Escreva um programa em Python que solicite ao usuário que digite os elementos de duas listas separadas por espaço. O programa deve determinar a interseção entre essas duas listas, ou seja, os elementos que estão presentes em ambas as listas, e imprimir o resultado.
"""

nova_lista = []

lista1 = input("Digite os elementos da primeira lista separados por espaço:").split()
lista2 = input("Digite os elementos da primeira lista separados por espaço:").split()

for i, elemento in enumerate (lista1):
    if elemento in lista1 and elemento in lista2:
        nova_lista.append(elemento)

print("A interseção é :", nova_lista)
