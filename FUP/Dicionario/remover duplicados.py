#Descrição: Você receberá uma lista de números com duplicatas. Use um set para remover as duplicatas e depois converta de volta para uma lista.



def remover_duplicatas(lista):
    #Converte a lista para um set
    set_sem_duplicatas = set(lista)

    #Converte o set de volta para uma lista
    lista_sem_duplicata = list(set_sem_duplicatas)
    return lista_sem_duplicata

entrada = input("Digite uma lista de numeros separados por virgula: ")
lista_numeros = [int(numero.strip()) for numero in entrada.split(',')]

resultado = remover_duplicatas(lista_numeros)
print("Lista sem duplicatas:", resultado)