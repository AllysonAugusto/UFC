"""
#Escreva uma função em Python chamada "substrings_comuns" que recebe duas strings como parâmetros e retorna uma lista contendo todas as substrings comuns a ambas as strings. Uma substring comum é uma sequência de caracteres que aparece em ambas as strings. A lista resultante não deve conter substrings duplicadas.
"""

def substrings_comuns(frase1, frase2):
    substrings = []
    for i in range(len(frase1)):
        for j in range(i+1, len(frase2) + 1):
            substring = frase1[i:j]
            # Verificando se a substring está em frase2 e não está na lista de substrings comuns
            if substring in frase2 and substring not in substrings:
                substrings.append(substring)
    return substrings # Adicionando o retorno da lista de substrings comuns






#Pedindo pra digitar as frases
frase1 = input("Digite a frase 1: ")
frase2 = input("Digite a frase 2: ")

resultado = substrings_comuns(frase1, frase2) 

print("As substrings comuns a ambas as frases são:")
for substring in resultado:
    print(substring)