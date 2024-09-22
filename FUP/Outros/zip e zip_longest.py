#Zip - Questão 1
nomes = ['Alice', 'Bob', 'Carol']
idades = [30, 29, 28]

for nome, idade in zip(nomes, idades):
    print(f"{nome} tem {idade} anos")

#Zip_Longest - Combinar listas de comprimentos diferentes com preenchimento
from itertools import zip_longest

def combinar_listas(list1, list2):
    return list(zip_longest(list1, list2, fillvalue=None))

lista1 = [1,2,3,4,5]
lista2 = ['a','b','c']
print(combinar_listas(lista1, lista2))