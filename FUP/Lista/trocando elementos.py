"""
#Implemente um programa que receba duas listas de inteiros de mesmo tamanho e troque os elementos entre as duas listas de índices pares, depois imprima os vetores modificados. 

#ATENÇÃO: Você somente pode imprimir as listas depois de fazer as modificações.

#OBS: Considere o índice 0 como sendo par.

"""

n = int(input("Digite o tamanho da lista: "))

lista1 = []
lista2 = []


# Preenchendo as listas
print("=== Lista 1 ===")
for i in range(n):
    number_lista1 = int(input(f"Digite o {i+1} elemento da lista 1: "))
    lista1.append(number_lista1)

print("=== Lista 2 ===")
for i in range(n):
    number_lista2 = int(input(f"Digite o {i+1} elemento da lista 2: "))
    lista2.append(number_lista2)

# Trocando os elementos nos índices pares
for i in range(n):
    if i % 2 == 0:
        lista1[i], lista2[i] = lista2[i], lista1[i]

# Imprimindo as listas modificadas
print("Lista 1 modificada:", lista1)
print("Lista 2 modificada:", lista2)