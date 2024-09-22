
#Listas
lista1 = []
lista2 = []

#Entrada
n = int (input('Digite o tamanho da lista: '))

#Lista 1
i = 0
print("---LISTA 1---")

while i < n:
    number1 = int (input('Digite os números da lista 1: ')) 
    lista1.append(number1)
    i+= 1

#Lista 2
i = 0
print("---LISTA 2---")
while i < n:
    number2 = int (input('Digite os números da lista 2: '))
    lista2.append(number2)
    i+= 1

#Pedindo elemento
elemento = int (input('Digite o indice par que deseja trocar: '))


if elemento >= 0 and elemento < (len(lista1)) and elemento < (len(lista2)):
    if elemento %2== 0:
        lista1[elemento], lista2[elemento] = lista2[elemento], lista1[elemento]
    else:
        print("ERROR: Indice não é par.")

else:
    print("Indice inserido está fora dos limites das listas.")


# Imprimindo as listas
print('Lista 1:', lista1)
print('Lista 2:', lista2)
