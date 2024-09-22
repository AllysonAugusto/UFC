"""
Crie um programa que vai gerar cinco números aletórios e colocar em uma tupla.Depois disso, mostre a listagem de numeros gerados e tambem indique o menor e maior valor que estao na tupla
"""


from random import randint

numeros = (randint(1,10), randint(1,10), randint(1,10))
print(f'Eu sortiei o valor {numeros}')

#Inicialização para comparação com o valor atual
maior = menor = numeros[0]
indice_menor = indice_maior = 0
for elemento in numeros:
    if elemento > maior:
        maior = elemento
        indice_maior += 1
    elif elemento < menor:
        menor = elemento
        indice_menor += 1

    
#Mostrar os elementos e nao pular
print(f'\n{elemento}', end='')

print(f'\nO maior valor foi {maior} no indice {indice_maior}')
print(f'\nO menor valor foi {menor} no indice {indice_menor}')
