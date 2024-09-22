"""

    Crie uma lista de filmes contendo uma única tupla. A tupla deve conter o título do filme, o nome do diretor, o ano de lançamento do filme e o orçamento do filme.
    Use a função input para coletar informações sobre outro filme. Você precisa de um título, nome do diretor, ano de lançamento e orçamento.
    Crie uma nova tupla a partir dos valores que você reuniu usando a entrada. Certifique-se de que eles estão na mesma ordem que a tupla que você escreveu na lista de filmes.
    Use uma string f para imprimir o nome do filme e o ano de lançamento, acessando sua nova tupla de filme.
    Adicione a nova tupla de filme à coleção de filmes usando append.
    Imprima ambos os filmes da coleção de filmes.
    Remova o primeiro filme dos filmes. Use o método que desejar.

"""

# Criação da lista de filmes contendo uma única tupla
filmes = [
         ("Matrix", "Lana Wachowski", 1999, 63000000)
]

# Coleta de informações sobre outro filme usando a função input
novo_titulo = input("Digite o título do novo filme: ")
novo_diretor = input("Digite o nome do diretor do novo filme: ")
novo_ano = int(input("Digite o ano de lançamento do novo filme: "))
novo_orcamento = int(input("Digite o orçamento do novo filme: "))

# Criação de uma nova tupla com as informações coletadas
novo_filme = (novo_titulo, novo_diretor, novo_ano, novo_orcamento)

# Impressão do nome do filme e do ano de lançamento usando a nova tupla de filme
print(f"Novo filme: {novo_filme[0]}, Ano de lançamento: {novo_filme[2]} ")

# Adição do novo filme à coleção de filmes usando append
filmes.append(novo_filme)

print('Filmes:')
for filme in filmes:
    print(filme)

filmes.pop(0)


# Impressão da coleção de filmes após a remoção do primeiro filme
print("Filmes após remoção do primeiro:")
print(filmes)