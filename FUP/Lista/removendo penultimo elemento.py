
def remover_penultimo(lista):
    if len(lista) < 2:
        return "A lista precisa ter pelo menos dois elementos."
    else:
        nova_lista = []
        for i in range(len(lista)):
            if i != len(lista) - 2: #todos os elementos, exceto o penúltimo, são adicionados à nova lista
                nova_lista.append(lista[i])
        return nova_lista

# Solicitar ao usuário os elementos da lista
elementos = input("Digite os elementos da lista separados por espaço: ")
minha_lista = [int(elemento) for elemento in elementos.split()]

# Chamar a função para remover o penúltimo elemento
resultado = remover_penultimo(minha_lista)

# Exibir a lista resultante
print("Lista após remover o penúltimo elemento:", resultado)



'''
   if len(lista) < 2:
        return "A lista precisa ter pelo menos dois elementos."
    else:
        del lista[-2]
        return lista
'''