"""
O programa "Descendentes_Geracao" tem como objetivo calcular a porcentagem de descendentes em cada geração em uma festa de família. Ele solicita ao usuário que insira dois valores: o número de gerações na família (n) e o número de participantes na festa (m). Em seguida, o usuário é solicitado a fornecer os IDs dos participantes presentes na família e na festa.

Para calcular as porcentagens de descendentes em cada geração na festa, o programa realiza os seguintes passos:

Para cada participante na festa, o programa calcula o número total de descendentes em cada geração até a última geração na família.
Em seguida, calcula a porcentagem de descendentes em cada geração em relação ao número total de descendentes.
Finalmente, o programa exibe as porcentagens de descendentes para cada geração presente na festa, arredondadas para duas casas decimais.
"""

n = int(input("Digite o número de gerações na família: "))
m = int(input("Digite o número de participantes na festa: "))

# Solicitar os IDs dos participantes presentes na família e na festa
pais = [int(input("Digite o ID do participante da família: ")) for _ in range(n)]
festa = [int(input("Digite o ID do participante na festa: ")) for _ in range(m)]

porcentagens_festa = []

# Calcular as porcentagens de descendentes em cada geração para cada participante na festa
for i in range(m):
    descendentes_geracao = [festa[i]]

    for j in range(1, n):
        descendentes_geracao.append(pais[j-1] * descendentes_geracao[j-1])

    total_descendentes = sum(descendentes_geracao)
    porcentagens_geracao = [(desc / total_descendentes) * 100 for desc in descendentes_geracao]
    porcentagens_festa.append(porcentagens_geracao)

# Exibir as porcentagens de descendentes para cada geração presente na festa
for porcentagens_geracao in porcentagens_festa:
    for i, porcentagem in enumerate(porcentagens_geracao):
        geracao = i + 1
        print(f"Porcentagem de descendentes da geração {geracao}: {porcentagem:.2f}%")
