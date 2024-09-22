"""
Escreva um programa em Python chamado "Ocorrência" que solicita ao usuário que insira um texto e uma palavra. O programa contará quantas vezes a palavra ocorre no texto e imprimirá o resultado na tela.
"""
def ocorrencia():
    text = input("Digite um texto: ")
    palavra = input("Digite uma palavra: ")
    
    cont = 0
    
    for i in range(len(text)):
        if text[i:i+len(palavra)] == palavra:
            cont += 1
    return cont

resultado = ocorrencia()
print(f'A palavra ocorre {resultado} vezes no texto.')

