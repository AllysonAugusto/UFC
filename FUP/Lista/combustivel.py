#código em Python para calcular o consumo médio de um carro 

distancia_total = int(input())
combustivel_total = float(input())

consumo_medio = distancia_total / combustivel_total

print("{:.3f} km/l".format(consumo_medio))