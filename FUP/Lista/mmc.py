def calcular_mmc(n, m):
    # Encontra o maior número entre n e m
    maior = max(n, m)

    while True:
        if maior % n == 0 and maior % m == 0:
            # O maior número é divisível por n e m, portanto, é o MMC
            mmc = maior
            break
        maior += 1

    return mmc

# Solicita os números ao usuário
n = int(input("Digite o primeiro número: "))
m = int(input("Digite o segundo número: "))

# Chama a função para calcular o MMC
resultado = calcular_mmc(n, m)

# Imprime o resultado
print("O MMC de", n, "e", m, "é:", resultado)
