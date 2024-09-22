n = int(input("Digite o tamanho das listas: "))

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


# Somar os elementos das duas listas, posição a posição, de trás para frente
for i in range(n - 1, -1, -1):
    soma_das_listas.append(lista1[i] + lista2[i])

print("Lista resultante da soma dos elementos das duas listas:")
print(soma_das_listas)