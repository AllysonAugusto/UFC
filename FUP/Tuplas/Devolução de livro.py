def verificar_emprestimos(emprestimos):
    if not emprestimos:  # Verifica se a lista de empréstimos está vazia
        print("Não há livros atualmente emprestados.")  # Se estiver vazia, exibe uma mensagem
    else:
        print("Livros atualmente emprestados:")  # Se não estiver vazia, exibe os livros emprestados
        for livro, usuario, data_devolucao in emprestimos:  # Itera sobre cada empréstimo na lista
            print(f"Nome do livro: {livro}\nNome do usuário: {usuario}\nData de devolução prevista: {data_devolucao}\n")  # Exibe as informações do empréstimo

def marcar_devolucao(emprestimos, livro_devolvido):
    emprestimos_atualizados = []  # Inicializa uma lista para armazenar os empréstimos atualizados
    livro_devolvido_encontrado = False  # Inicializa uma variável para verificar se o livro foi encontrado
    for livro, usuario, data_devolucao in emprestimos:  # Itera sobre cada empréstimo na lista
        if livro == livro_devolvido:  # Verifica se o livro atual é o livro a ser devolvido
            livro_devolvido_encontrado = True  # Marca o livro como encontrado
        else:
            emprestimos_atualizados.append((livro, usuario, data_devolucao))  # Adiciona o empréstimo à lista de empréstimos atualizados, exceto se for o livro a ser devolvido
    if livro_devolvido_encontrado:  # Verifica se o livro foi encontrado
        print(f"O livro '{livro_devolvido}' foi devolvido com sucesso.")  # Se encontrado, exibe uma mensagem de sucesso
    else:
        print(f"O livro '{livro_devolvido}' não foi encontrado nos empréstimos em andamento.")  # Se não encontrado, exibe uma mensagem de erro
    return emprestimos_atualizados  # Retorna a lista de empréstimos atualizados

def main():
    emprestimos = []  # Inicializa uma lista para armazenar os empréstimos
    while True:  # Loop infinito para o menu de opções
        print("\n1. Verificar empréstimos")
        print("2. Marcar devolução")
        print("3. Sair")
        opcao = input("\nEscolha uma opção: ")  # Solicita ao usuário que escolha uma opção
        if opcao == "1":  # Se a opção for verificar empréstimos
            verificar_emprestimos(emprestimos)  # Chama a função para verificar os empréstimos
        elif opcao == "2":  # Se a opção for marcar devolução
            livro = input("Digite o nome do livro emprestado: ")  # Solicita ao usuário o nome do livro emprestado
            usuario = input("Digite o nome do usuário: ")  # Solicita ao usuário o nome do usuário
            data_devolucao = input("Digite a data de devolução prevista (AAAA-MM-DD): ")  # Solicita ao usuário a data de devolução prevista
            emprestimo = (livro, usuario, data_devolucao)  # Cria uma tupla com as informações do empréstimo
            emprestimos.append(emprestimo)  # Adiciona o empréstimo à lista de empréstimos
        elif opcao == "3":  # Se a opção for sair
            print("Saindo...")  # Exibe uma mensagem de saída
            break  # Sai do loop
        else:  # Se a opção for inválida
            print("Opção inválida. Tente novamente.")  # Exibe uma mensagem de opção inválida

if __name__ == "__main__":  # Verifica se o programa está sendo executado como o programa principal
    main()  # Chama a função principal
