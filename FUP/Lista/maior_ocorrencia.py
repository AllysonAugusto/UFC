"""
    A função maior(L) recebe uma lista como parâmetro e retorna o maior elemento presente na lista.
    A função ocorrencia(L, ele) recebe uma lista e um número como parâmetros e retorna a quantidade de vezes que o número especificado aparece na lista.
    O programa principal solicita ao usuário que insira uma lista de números inteiros, armazenando-os em uma lista. Em seguida, o programa pede ao usuário que digite um número para consultar suas ocorrências na lista. Utilizando as funções definidas anteriormente, o programa imprime na tela o maior elemento da lista, o menor elemento da lista e o número de ocorrências do número digitado na lista.

O programa continua solicitando que o usuário insira números até que ele insira 0 para sair do loop. Após a entrada de números, o usuário informa o número que deseja consultar as ocorrências. O programa então exibe na tela o maior elemento da lista, o menor elemento da lista e o número de ocorrências do número consultado na lista.

Se desejar, você pode compactar o código definindo as funções maior(L) e ocorrencia(L, ele) em apenas uma função chamada encontrar_menor_maior_ocorrencias(), seguindo um estilo mais funcional.
"""

L = []
def maior(L):

    if len(L) == 0:
        return None
    # Inicializa o maior elemento como o primeiro elemento da lista
    maior = L[0]
    for elemento in L:
        if elemento > maior:
            maior = elemento
    return maior

def menor(L):

    if len(L) == 0: 
        return None
    menor = L[0]
    for elemento in L:
        if elemento < menor:
            menor = elemento
    return menor

L = [] 
def ocorrencia(L, ele):
    if len(L) == 0:
        return None

    contador = 0
    for elemento in L:
        if elemento == ele:
            contador += 1
    return contador

# Usuário digitando
while True:
    num = int(input('Digite um número (0 para sair): '))
    if num == 0:
        break
    L.append(num)

numero_consulta = int(input('Digite o número para contar as ocorrências: '))

maior = maior(L)
menor = menor(L)
ocorrencias = ocorrencia(L, numero_consulta)

print('O maior elemento da lista é:', maior)
print('O menor elemento da lista é:', menor)
print('O número de ocorrências de', numero_consulta, 'na lista é:', ocorrencias)
