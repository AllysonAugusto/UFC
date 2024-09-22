"""
Este código Python implementa uma função chamada transformar_vetor_em_numero, que recebe uma lista de inteiros como entrada e retorna um único número inteiro formado pela concatenação dos elementos da lista. Abaixo está o enunciado para o problema:

Transformação de Vetor em Número

Implemente um programa em Python que receba uma lista de inteiros como entrada e retorne um único número inteiro formado pela concatenação dos elementos da lista.


Exemplo de saida:

5
1
2
3
4
5
12345

"""


def transformar_vetor_em_numero(list):
    concatenar_elementos = ""
    for elemento in list:
        concatenar_elementos += str(elemento)
    return concatenar_elementos


list = []

tamanho = int(input("Digite o tamanho da lista: "))
for i in range(tamanho):
    number = int(input(f"Digite o {i+1} numero: "))
    list.append(number)


transformar = transformar_vetor_em_numero(list)
print(transformar)