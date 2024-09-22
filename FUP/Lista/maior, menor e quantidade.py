"""
Escreva um programa em Python chamado "Identificar_Quantidade" que solicita ao usuário que informe quantos números deseja digitar. Em seguida, o programa pede que o usuário insira os números. Após isso, o programa identifica o maior e o menor número digitado, contando quantas vezes cada um deles se repete na lista.
"""

def Identificar_quantidade():
    
    lista = []
    n = int(input("Digite a quantidade de números que deseja digitar: "))

    for i in range(n):
         numbers = int(input(f"Digite o {i+1} número: "))
         lista.append(numbers)

    #Inicializadores
    ocorrencia_maior = ocorrencia_menor = 0
    maior = menor = lista[0]

    
    for elemento in lista:
        
        if elemento == maior:
            ocorrencia_maior += 1

        elif elemento == menor:
            ocorrencia_menor += 1 #encontramos outro número que é igual ao menor número atual.Repetindo o menor numero

        elif elemento > maior:
            maior = elemento
            ocorrencia_maior = 1

        elif elemento < menor: #encontramos um novo menor número.Incrementando o menor valor
            menor = elemento
            ocorrencia_menor = 1
        
    # Retornando o maior e o menor número, junto com suas ocorrências
    return maior, menor, ocorrencia_maior, ocorrencia_menor


# Chamando a função e armazenando os resultados
maior, menor, ocorrencia_maior, ocorrencia_menor = Identificar_quantidade()

# Imprimindo os resultados
print(f'O maior número é {maior} e ocorre {ocorrencia_maior} vezes.')
print(f'O menor número é {menor} e ocorre {ocorrencia_menor} vezes.')