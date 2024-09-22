"""
Dois automóveis (X e Y) partem na mesma direção. O carro X parte com uma velocidade constante de 60 km/h e o carro Y parte com uma velocidade constante de 90 km/h.

Numa hora (60 minutos), o carro Y pode distanciar-se 30 quilómetros do carro X, ou seja, pode afastar-se um quilómetro por cada 2 minutos.

Leia a distância (em km) e calcule quanto tempo leva (em minutos) para o carro Y percorrer essa distância em relação ao outro carro.
Entrada

O arquivo de entrada contém 1 valor inteiro.
Saída

Imprime o tempo necessário seguido da mensagem "minutos" que significa minutos em português.
"""

distancia = int(input())

# Calcular o tempo em minutos para o carro Y percorrer a distância
# O carro Y viaja 1 km a cada 2 minutos, então dividimos a distância pela velocidade do Y (30 km/h) e multiplicamos por 2

tempo_minutos = (distancia/30)*60

print("{:.0f} minutos".format(tempo_minutos))