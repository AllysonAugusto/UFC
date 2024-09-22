def print_diamond(rows):
    for i in range(1, rows +1): #percorre de 1 até o número de linhas
        print(" " * (rows - i) + "*" * (2 * i-1)) #espaços para centralizar os asteriscos e criação da forma do diamente
    for i in range (rows -1, 0, -1):
        print(" " * (rows -i) + "*" * (2*i-1))

    
print_diamond(5)