"""
Crie um programa que tenha uma tupla totalmente preenchida com uma contagem por extenso de zero até vinte.

Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostra-lo por extenso.

"""


cont = (('Zero', 'Um', 'Dois', 'Tres', 'Quatro', 'Cinco'
         'Seis', 'Sete', 'Oito', 'Nove', 'Dez', 'Onze', 
         'Doze', 'Treze', 'Catorze', 'Quinze', 'Dezesseis',
         'Dezessete', 'Dezoito', 'Dezenove', 'Vinte'))



while True:
    numero = int(input('Digite um número de 0 a 20: '))
    if 0 <= numero <=20: #numero fora do escopo
        break 
    print('Tente novamente.', end='')

print(f'Você digiotu o número {cont[numero]}')