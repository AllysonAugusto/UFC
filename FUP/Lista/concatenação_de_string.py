def concatenar_palavras(frase):
    palavras = frase.split()
    frase_concatenada = "".join(palavras)
    return frase_concatenada

# Solicitar ao usuário para digitar a frase
frase = input("Digite uma frase: ")

frase_concatenada = concatenar_palavras(frase)
print("Frase concatenada:", frase_concatenada)



'''
# Solicitando ao usuário que digite duas strings
string1 = input("Digite a primeira string: ")
string2 = input("Digite a segunda string: ")

# Concatenando as strings
concatenada = string1 + string2

# Exibindo a string concatenada
print("A concatenação das strings é:", concatenada)


'''
