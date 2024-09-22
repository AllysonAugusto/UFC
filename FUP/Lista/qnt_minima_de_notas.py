"""
Neste problema tem de ler um valor inteiro e calcular o menor número possível de notas em que o valor pode ser decomposto. As notas possíveis são 100, 50, 20, 10, 5, 2 e 1. Imprima o valor lido e a lista de notas.
Entrada

O ficheiro de entrada contém um valor inteiro N (0 < N < 1000000).
Saída

Imprime o número lido e a quantidade mínima de cada nota necessária em língua portuguesa, conforme o exemplo dado. Não se esqueça de imprimir o fim da linha após cada linha, caso contrário receberá a mensagem "Presentation Error".

"""

valor = int(input())

# Lista das notas possíveis
notas = [100, 50, 20, 10, 5, 2, 1]

# Calcular a quantidade mínima de cada nota necessária
for nota in notas:
    quantidade = valor // nota #divisao inteira do valor total pelo valor da nota.Por exemplo, se valor for 173 e nota for 100, quantidade será igual a 1. 
    print("{} nota(s) de R$ {},00".format(quantidade, nota))
    valor %= nota