"""
Uma empresa de pesquisas precisa tabular os resultados da seguinte enquete feita a um grande quantidade de organizações:

    "Qual o melhor Sistema Operacional para uso em servidores?" As possíveis respostas são:
        1 - Windows Server
        2- Unix
        3- Linux
        4- Netware
        5- Mac OS
        6- Outro

Você foi contratado para desenvolver um programa que leia o resultado da enquete e informe ao final o resultado da mesma. O programa deverá ler os valores até ser informado o valor 0, que encerra a entrada dos dados. Não deverão ser aceitos valores além dos válidos para o programa (0 a 6). Os valores referentes a cada uma das opções devem ser armazenados num vetor. Após os dados terem sido completamente informados, o programa deverá calcular a percentual de cada um dos concorrentes e informar o vencedor da enquete. O formato da saída foi dado pela empresa, e é o seguinte:

"""
# Inicializando a variável 'opcao' com o valor 10
opcao = 10

# Inicializando a lista 'lista_opcoes' com 6 elementos, todos com valor 0
lista_opcoes = 6 * [0]

# Inicializando a variável 'num_votos' com o valor 0
num_votos = 0

# Loop while que executa enquanto a variável 'opcao' for diferente de 0
while opcao != 0:    
    # Solicita ao usuário que digite a opção de sistema operacional utilizado
    opcao = int(input("Digite a opção de sistema operacional utilizado na sua organização:\n1 - Windows Server\n2 - Unix\n3 - Linux\n4 - Netware\n5 - Mac OS\n6 - Outro\nOpção escolhida:  "))
    
    # Verifica se a opção digitada é inválida ou se o número de votos é menor que zero
    if opcao > 6 or num_votos < 0:
        # Imprime uma mensagem de número inválido
        print('Número inválido, tente outra opção!')
    # Verifica se a opção digitada é 0, indicando o fim da pesquisa
    elif opcao == 0:
        # Imprime uma mensagem informando que a pesquisa foi finalizada e encerra o loop
        print('\nPesquisa finalizada!')
        break
    else:
        # Atualiza a contagem de votos para a opção escolhida
        lista_opcoes[opcao - 1] = lista_opcoes[opcao - 1] + 1 
        # Incrementa o número total de votos
        num_votos =+ 1   

# Lista com os nomes dos sistemas operacionais
opcoes = ['Windows Server', 'Unix', 'Linux', 'Netware', 'Mac OS', 'Outro']

# Variável para armazenar o índice do sistema operacional com maior número de votos
melhor = 0

# Imprime cabeçalho da tabela
print('Sistema Operacional     Votos  %')
print('----------------------------------')

# Loop para percorrer cada opção e calcular a porcentagem de votos
for idx in range(len(lista_opcoes)):
    # Calcula a porcentagem de votos para a opção atual
    porcentagem = (lista_opcoes[idx] / num_votos) * 100
    # Imprime a linha da tabela com o nome do sistema, quantidade de votos e porcentagem
    print(f'{opcoes[idx]}   -  {str(lista_opcoes[idx])}  -  {porcentagem:.2f}')
    # Verifica se a quantidade de votos para a opção atual é maior que a do melhor até o momento
    if lista_opcoes[idx] > lista_opcoes[melhor]:
        # Atualiza o índice do sistema operacional com maior número de votos
        melhor = idx

    
        
    

    
print(f'\nTotal de votos: {num_votos}')
porcentagem_melhor = (lista_opcoes[melhor]/num_votos)*100
print(f'O Sistema Operacional mais votado foi o {opcoes[melhor]}, com {lista_opcoes[melhor]} votos, correspondendo a {porcentagem_melhor:.2f} dos votos.')

