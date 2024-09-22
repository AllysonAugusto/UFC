"""
Escreva um programa em Python que receba os dados de vários times e gere a tabela de classificação. 
Cada time será representado por uma lista contendo o nome do time, a quantidade de jogos disputados, a quantidade de vitórias, 
a quantidade de empates e a quantidade de derrotas. O programa deve calcular os pontos de cada time (3 pontos por vitória, 1 ponto 
por empate e 0 pontos por derrota) e exibir a tabela formatada.
"""


def calcular_pontos(vitorias, empates):
    return vitorias * 3 + empates

def gerar_tabela(times):
    # Imprimir cabeçalho da tabela
    print("+------------+-------+---------+--------+---------+-------+")
    print("| Time       | Jogos | Vitórias| Empates| Derrotas| Pontos|")
    print("+------------+-------+---------+--------+---------+-------+")

    # Imprimir cada linha da tabela
    for time in times:
        nome = time[0]
        jogos = time[1]
        vitorias = time[2]
        empates = time[3]
        derrotas = time[4]
        pontos = calcular_pontos(vitorias, empates)

        # Formatar e imprimir linha da tabela
        print("| {:<10} | {:>6} | {:>8} | {:>7} | {:>8} | {:>5} |".format(nome, jogos, vitorias, empates, derrotas, pontos))

    # Imprimir rodapé da tabela
    print("+------------+-------+---------+--------+---------+-------+")

# Dados dos times: nome, jogos, vitorias, empates, derrotas
times = [
    ["Time1", 10, 7, 2, 1],
    ["Time2", 10, 6, 3, 1],
    ["Time3", 10, 5, 4, 1],
    ["Time4", 10, 5, 3, 2]
]

# Gerar e imprimir a tabela de classificação
gerar_tabela(times)





