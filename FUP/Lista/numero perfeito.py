def verificar_numero_perfeito(numero):
    soma_divisores = 0
    # Itera de 1 até o número - 1, verificando os divisores
    for i in range(1, numero):
        # Se o número for divisível por i, adiciona i à soma
        if numero % i == 0:
            soma_divisores += i
    # Se a soma dos divisores for igual ao número, então é um número perfeito
    if soma_divisores == numero:
        return True
    else:
        return False

# Solicita ao usuário que digite um número para verificar se é perfeito
numero = int(input("Digite um número para verificar se é perfeito: "))

# Chama a função para verificar se o número é perfeito
if verificar_numero_perfeito(numero):
    print(numero, "é um número perfeito.")
else:
    print(numero, "não é um número perfeito.")
