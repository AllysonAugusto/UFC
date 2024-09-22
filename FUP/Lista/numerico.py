'''
Entrada de dados e método isnumeric():

Questão: Escreva um programa Python que solicite ao usuário que insira um número. Em seguida, verifique se o número inserido é numérico usando o método isnumeric() e imprima o resultado.
'''

try:
    numero = input("Digite um número: ")
    if numero.isnumeric():
        print("O número inserido é numérico.")
    else:
        print("O número inserido não é numérico")
except:
    print("ERROR: Entrada inválida.Certifique-se de inserir um númeroj")