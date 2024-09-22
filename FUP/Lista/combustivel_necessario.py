"""
O Joãozinho quer calcular e mostrar a quantidade de litros de combustível gasto numa viagem, utilizando um carro que faz 12 Km/L. Para isso, ele gostaria que o ajudasses através de um programa simples. Para efetuar o cálculo, é necessário ler o tempo gasto (em horas) e a mesma velocidade média (km/h). Desta forma, pode obter a distância e, em seguida, calcular quantos litros serão necessários. Apresenta o valor com três casas decimais após o ponto.
Entrada

O ficheiro de entrada contém dois números inteiros. O primeiro é o tempo gasto na viagem (em horas). O segundo é a velocidade média durante a viagem (em Km/h).

"""

tempo_gasto, velocidade_media = map(int, input().split()) #dois valores inteiros separados por espaço.

distancia = tempo_gasto * velocidade_media
litros_combustivel = distancia / 12

print ("{:.3f}".format(litros_combustivel))