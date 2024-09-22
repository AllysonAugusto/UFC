"""

# Sistema de Gerenciamento de Notas dos Alunos

Escreva um programa em Python chamado "Gerenciamento_Notas" que permite ao usuário inserir os nomes e as notas de alunos, calcular as médias e exibir um relatório com os nomes, as médias e as notas de cada aluno. O programa deve permitir que o usuário escolha ver as notas de um aluno específico.

1. O programa solicitará ao usuário que insira o nome e as notas (2 notas) de cada aluno.
2. Após inserir os dados de um aluno, o programa calculará a média das notas.
3. O usuário poderá escolher continuar inserindo mais alunos ou encerrar o programa.
4. Após encerrar a entrada de dados dos alunos, o programa exibirá um relatório com o nome, a média e as notas de cada aluno.
5. O usuário poderá escolher visualizar as notas de um aluno específico digitando o número correspondente a esse aluno. Se desejar encerrar o programa, o usuário pode digitar -1.

O relatório exibido incluirá o número do aluno, o nome, a média e as notas. 


Digite o nome do aluno: Alice
Digite a nota 1º do aluno: 8.5
Digite a nota 2º do aluno: 9.0
Deseja continuar? [S/N]: S
Digite o nome do aluno: Bob
Digite a nota 1º do aluno: 7.5
Digite a nota 2º do aluno: 8.0
Deseja continuar? [S/N]: N
-=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*
[['Alice', [8.5, 9.0], 8.75], ['Bob', [7.5, 8.0], 7.75]]
No.  NOME       MÉDIA
--------------------------
0    Alice       8.8
1    Bob         7.8
------------------------------
Para sair, digite -1.
Qual aluno deseja ver a nota?: 0
As notas de Alice são [8.5, 9.0]
<<< VOLTE SEMPRE >>>
------------------------------
Para sair, digite -1.
Qual aluno deseja ver a nota?: -1
FINALIZANDO...
"""

lista_notas = []

while True:
    nome = str(input("Digite o nome do aluno(a): "))
    nota1 = float(input("Digite a nota 1 do aluno(a): "))
    nota2 = float(input("Digite a nota 2 do aluno(a): "))
    media = (nota1 + nota2)/2
    lista_notas.append([nome, [nota1, nota2], media])

    #Perguntando se deseja continuar
    opcao = str(input("Deseja continuar [Y/N]? "))
    if opcao in 'Nn':
        break

print ('-='*30)
print ("Relatório de notas: ")

#Exibindo o relatório de notas
print(f'{"No.":<4} {"NOME":<10} {"NOTAS":<20} {"MÉDIA":>8}')
print('-' * 50)


for nome, aluno in enumerate (lista_notas): #nome será o índice do aluno na lista, e aluno será a lista de informações sobre o aluno
    print(f'{nome:<4} {aluno[0]:<10} {aluno[2]:>8.1f}') #alinhamento do indice, nome e media do aluno



while True:
    print ("-" *30)
    print ('Para sair, digite -1.')
    escolha = int (input('Qual aluno deseja ver a nota?: '))
    if escolha == -1:
        print ('FINALIZANDO...')
        break
    if escolha <= len (lista_notas) -1:
        print (f'As notas de {lista_notas[escolha][0]} são {lista_notas[escolha] [1]}') #nome na posição 1 e nota na posição 2
    print ('<<< VOLTE SEMPRE >>>')