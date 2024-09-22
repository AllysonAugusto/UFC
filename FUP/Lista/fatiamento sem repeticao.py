'''
O programa "Fatiamento_Sem_Repeticao" permite ao usuário inserir uma string e um índice inicial. Ele remove caracteres repetidos da string e, em seguida, fatia a string resultante a partir do índice inicial especificado.

O funcionamento do programa é descrito a seguir:

O usuário é solicitado a inserir uma string.
Em seguida, é solicitado que o usuário insira um índice inicial.
O programa remove os caracteres repetidos da string fornecida, mantendo apenas uma ocorrência de cada caractere.
Após remover os caracteres repetidos, o programa fatia a string resultante a partir do índice inicial especificado pelo usuário.
O programa exibe a string resultante após o fatiamento.
'''


string = input("Digite uma string: ")
indice_inicial = int(input("Digite o índice inicial: "))


string_sem_repeticao = ""
for caractere in string:
    if caractere not in string_sem_repeticao: #ficar adicionando caractere, se não tiver em string_sem_repeticao é porque já está dentro
        string_sem_repeticao += caractere #adicionando dentro da string

string_fatiada = string_sem_repeticao[indice_inicial:]
print("String fatiada:", string_fatiada)
