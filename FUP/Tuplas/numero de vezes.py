"""
Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla.NO final mostre:

A) Quantas vezes apareceu o valor 9
B) Em que posição foi digitado o primeiro valor
C) Quais foram os nuemros pares
"""

num = ()

for i in range(1, 5):
    numero = int(input(f"Digite o {i}º número: "))
    num += (numero,)
print(f'Você digitou os valores {num}')

contador = 0
for elemento in num:
    if elemento == 9:
        contador += 1
print(f"O valor 9 apareceu {contador} vezes")


contador3 = 0
for elemento in num:
    if elemento == 3:
        contador3 += 1
print(f"O valor 3 apareceu {contador3} vezes")


pares = [elemento for elemento in num if elemento %2 == 0]

for elemento in pares:
    pass
print("Valores pares: ", pares)