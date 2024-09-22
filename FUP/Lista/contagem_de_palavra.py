"""
Escreva um programa em Python que solicite ao usuário que digite uma palavra e, 
em seguida, conte o número de ocorrências das letras 'a' e 'o' nessa palavra. 
Para a letra 'o', apenas as primeiras 20 letras da palavra devem ser consideradas.
"""

frase = input("Digite uma frase: ")
letra = input("Digite uma letra para saber a ocorrência: ")

indice_ocorrencia = []
for i, caractere in enumerate(frase):
    if caractere == letra:
        indice_ocorrencia.append(i)

if len(indice_ocorrencia) > 0:
    print(f"A letra '{letra}' ocorre nas posições:", indice_ocorrencia)
else:
    print("Essa letra não existe na frase.")


