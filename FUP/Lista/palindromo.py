def ehpalindromo(palavra):
        # Remove espaços em branco e converte para minúsculas
        palavra = palavra.replace(" ", "").lower()
        # Verifica se a palavra é igual à sua inversa
        return palavra == palavra[::-1]


#Teste
palavra = input("Digite uma palavra para verificar se é palíndromo: ")
if ehpalindromo(palavra):
    print(f'{palavra} é um palíndromo.')
else:
    print((f'{palavra} não é um palíndromo'))