def print_inverted_triangle(rows):
    for i in range(rows, 0 , -1): #indo e  decrementamos i a cada iteração até atingir 1
        print("*" * i) # O número de asteriscos em cada linha é igual ao valor atual de i (que diminui a cada interação)

print_inverted_triangle(5)