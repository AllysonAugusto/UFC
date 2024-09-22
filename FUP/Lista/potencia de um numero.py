def calcular_potencia(base, expoente):
    # Inicializa o resultado como 1
    resultado = 1
    # Verifica se o expoente é negativo
    if expoente < 0:
        # Se o expoente for negativo, inverte a base e o expoente
        base = 1 / base
        expoente = -expoente
    # Calcula a potência iterativamente
    for _ in range(expoente):
        resultado *= base
    # Retorna o resultado
    return resultado

# Solicita ao usuário que digite a base e o expoente
base = float(input("Digite a base: "))
expoente = int(input("Digite o expoente: "))

# Chama a função para calcular a potência
resultado = calcular_potencia(base, expoente)

# Imprime o resultado
print("Resultado:", resultado)
