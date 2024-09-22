"Você receberá uma string com várias palavras. Crie um programa que conte a frequência de cada palavra usando um dicionário."


#função para contar a frequência de cada palavra
def contar_palavra(texto):
    
    #dividindo a string em palavras
    palavras = texto.split()

    #criando um dicionario vazio para armazenar a frequencia das palavras
    frequencia_palavras = {}

    #iterando sobre cada palavra na lista de palavras
    for palavra in palavras:
        # Se a palavra já está no dicionário, incrementa sua contagem
        if palavra in frequencia_palavras:
            frequencia_palavras[palavra] += 1
        # Se a palavra não está no dicionário, adiciona com contagem 1
        else:
            frequencia_palavras[palavra] = 1
        
    return frequencia_palavras

texto = input("Digite um texto: ")

resultado = contar_palavra(texto)
print("Frequência das palavras: ", resultado)