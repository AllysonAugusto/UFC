def substituir_vogais_por_caractere(frase, caractere):
    # Lista de vogais
    vogais = 'aeiouAEIOU'
    # Inicializa uma string vazia para armazenar o resultado
    nova_frase = ''
    # Itera sobre cada caractere na frase
    for char in frase:
        # Verifica se o caractere é uma vogal
        if char in vogais:
            # Se for uma vogal, adiciona o caractere específico à nova string
            nova_frase += caractere
        else:
            # Se não for uma vogal, adiciona o próprio caractere à nova string
            nova_frase += char
    # Retorna a nova string com as vogais substituídas
    return nova_frase

# Teste da função
frase_original = input("Digite uma frase: ")
caractere_substituto = input("Digite o caractere para substituir as vogais: ")
frase_modificada = substituir_vogais_por_caractere(frase_original, caractere_substituto)
print("Frase modificada:", frase_modificada)
