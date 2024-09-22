"""
permite que o usuário compare duas partes diferentes de uma string e verifica se elas são idênticas.
"""

def comparar_substrings(string, inicio1, fim1, inicio2, fim2):
    substring1 = string[inicio1:fim1]
    substring2 = string[inicio2:fim2]
    
    if substring1 == substring2:
        return True
    else:
        return False

string = input("Digite uma string: ")
inicio1 = int(input("Digite o índice de início da primeira substring: "))
fim1 = int(input("Digite o índice de fim da primeira substring: "))
inicio2 = int(input("Digite o índice de início da segunda substring: "))
fim2 = int(input("Digite o índice de fim da segunda substring: "))

resultado = comparar_substrings(string, inicio1, fim1, inicio2, fim2)
if resultado:
    print("As substrings são iguais.")
else:
    print("As substrings são diferentes.")
