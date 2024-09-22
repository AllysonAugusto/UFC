"""
Escreva um programa em Python que solicite ao usuário que insira as notas de vários alunos. 
Cada aluno terá um nome e três notas. O programa deve calcular a média de cada aluno e determinar quais alunos têm a maior média.
"""

# Solicitar ao usuário o número de alunos
num_alunos = int(input("Número de alunos: "))
qnt_notas = int(input("Digite a quantidade de notas: "))

# Inicializar uma lista vazia para armazenar os dados dos alunos
nome_e_media = []
media_alunos = []

# Solicitar os dados de cada aluno e calcular a média
for i in range(1, num_alunos + 1): #de um ate alunos, incrementando
    nome = input(f"\nAluno {i}:\nNome: ")  

    notas = []
    for j in range((qnt_notas)): #pedindo pra o aluno digitar com base em qnt_notas
        nota = float(input(f"Nota {j} para {nome}: "))
        notas.append(nota)
    media = sum(notas) / len(notas)
    media_alunos.append (media)
    nome_e_media.append((nome, media))

print("\nAlunos e suas médias:")
for aluno in nome_e_media:
    print(f"Aluno: {aluno[0]} - Média: {aluno[1]:.2f}")


# Calcular o índice do aluno com a maior média
maior_nota = max(media_alunos)  # Encontrar a maior média na lista de médias
for i in range(len(media_alunos)):  # Iterar sobre os índices da lista de médias
    if media_alunos[i] == maior_nota:  # Verificar se a média no índice atual é igual à maior média
        indice_aluno = i  # Armazenar o índice do aluno com a maior média
        break  # Parar o loop quando o índice for encontrado

# Calcular o índice do aluno com a maior média
maior_media = max(media_alunos)  # Encontrar a maior média na lista de médias
indice_aluno_maior_media = media_alunos.index(maior_media)  # índice do aluno com a maior média 
print("O aluno {} obteve a maior média, com {:.2f}".format(nome_e_media[indice_aluno_maior_media][0], maior_media)) #[0] nome é o primeiro elemento da tupla.

