"""
#Escreva uma função em Python chamada "maior_substring_repetida" que 
recebe uma string como parâmetro e retorna a maior substring repetida nessa string. 
Uma substring repetida é uma sequência de caracteres que aparece mais de uma vez na string. 
Se houver várias substrings repetidas com o mesmo comprimento máximo, retorne a primeira encontrada.
"""

def maior_substring_repetida(string):
    max_substring = '' # Armazena a maior substring repetida encontrada até o momento
    max_length = 0 # Armazena o comprimento da maior substring repetida

    for i in range(len(string)):
        for j in range(i + 1, len(string) + 1):
            substring = string[i:j]
            
            # Verifica se a substring aparece mais de uma vez na string original
            if string.count(substring) > 1:
                if len(substring) > max_length:
                    max_substring = substring
                    max_length = len(substring)
    return max_substring, max_length
                    

string = "banana"
max_substring, max_length = maior_substring_repetida(string)
print("Maior substring repetida:", max_substring)
print("Comprimento:", max_length)
