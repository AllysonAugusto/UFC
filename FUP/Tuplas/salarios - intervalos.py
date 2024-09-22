"""
Utilize uma lista para resolver o problema a seguir. Uma empresa paga seus vendedores com base em comissões. O vendedor recebe 
200 por semana mais 9 por cento de suas vendas brutas daquela semana. Por exemplo, um vendedor que teve vendas brutas de 3000 
em uma semana recebe 200 mais 9 por cento de 3000, ou seja, um total de 470. Escreva um programa (usando um array de contadores) 
que determine quantos vendedores receberam salários nos seguintes intervalos de valores:

a. $200 - $299
b. $300 - $399
c. $400 - $499
d. $500 - $599
e. $600 - $699
f. $700 - $799
g. $800 - $899
h. $900 - $999
i. $1000 em diante
"""



num_vendedores = int(input('Quantos vendedores a loja tem? '))

salarios = []
classe = []
for vendedor in range(1,num_vendedores+1):
    vendas = float(input('\nQuanto o vendedor '+str(vendedor)+' arrecadou essa semana? '))
    salarios.append(200+(vendas*0.09))

dicionario = {'1':[range(200,300),0],'2':[range(300,400),0], #contador igual a 0 associado a '1' em 1, indicando que um salário está dentro dessa faixa.
              '3':[range(400,500),0],'4':[range(600,700),0],
              '5':[range(700,800),0],'7':[range(800,900),0],
              '8':[range(900,1000),0],'9':[range(1000,100000),0]}  

#dicionario.keys() - pega o valor das chaves de cada dicionário

for salario in salarios:
    print(salario)
    for idx in dicionario.keys(): #mexendo com chaves
        print(idx)
        if salario in dicionario[idx][0]: #Verifica se o valor de salario está presente na faixa de números associada à chave idx no dicionário.acessa o primeiro elemento da lista associada à chave '1', que é o objeto range(200, 300). Então, o [0] se referindo ao primeiro elemento da lista.
            classe.append(idx)
            dicionario[idx][1] = dicionario[idx][1] + 1 #atualizando o contador de ocorrências para a faixa salarial correspondente ao índice idx (chave atual do dicionário) quantos salários estão dentro de cada faixa salarial e atualizando os contadores correspondentes no dicionário.   
            
#for idx in dicionario.keys():
#    inicial = dicionario[idx][0][0]
#    final = dicionario[idx][0][-1]
#    quant = dicionario[idx][1]
#    if final == 99999:
#        print('Número de funcionários com salário acima de R$1000,00 iguai a '+str(quant))
#    else:
#        print('Nuúmero de funcionários com salário de R$'+str(inicial)+ ' a R$'+str(final)+' igual a: '+s