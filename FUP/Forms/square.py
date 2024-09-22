def print_hellow_square(rows):
    for i in range (rows):
        if i == 0 or i == rows -1: #verificando se estamos na primeira linha ou na ultima
            print("*" * rows) #asteriscos com o comprimento igual a rows
        else:
            print("*" + " " * (rows -2) + "*") #ou seja, estamos nas linhas intermediarias (formato oca)

print_hellow_square(5)