# calcula a distância entre esses dois pontos usando a fórmula euclidiana

x1, y1 = map (float, input().split())
x2, y2 = map(float, input().split())

#distancia entre dois pontos
distancia = ((x2 - x1)** 2 + (y2-y1)**2)** 0.5

print("{:.4f}".format(distancia))