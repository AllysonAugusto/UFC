def obter_preferencias_usuario():
    # Solicita ao usuário que insira suas preferências de produtos
    print("Digite suas preferências de produtos separadas por vírgula (ex: eletrônicos, vestuário, alimentos): ")
    # Obtém a entrada do usuário, remove espaços em branco extras e divide a entrada em uma lista usando a vírgula como separador
    preferencias = input().strip().split(',')
    # Converte a lista de preferências em um conjunto para remover duplicatas e facilitar a verificação de semelhanças entre os usuários
    return set(preferencias)

def main():
    # Inicializa uma lista vazia para armazenar os usuários e suas preferências
    usuarios = []

    # Loop principal para solicitar as preferências de cada usuário
    while True:
        # Solicita ao usuário que digite seu nome ou 'sair' para encerrar o programa
        nome_usuario = input("Digite seu nome (ou digite 'sair' para encerrar): ")
        
        # Verifica se o usuário deseja sair do programa
        if nome_usuario.lower() == 'sair':
            break
        
        # Chama a função para obter as preferências de produtos do usuário
        preferencias_usuario = obter_preferencias_usuario()
        
        # Cria um dicionário para armazenar o nome do usuário e suas preferências
        usuario = {'nome': nome_usuario, 'preferencias': preferencias_usuario}
        
        # Adiciona o dicionário do usuário à lista de usuários
        usuarios.append(usuario)

    # Exibe os nomes dos usuários e suas preferências de produtos
    print("\nUsuários e suas preferências de produtos:")
    for usuario in usuarios:
        print(f"{usuario['nome']}: {usuario['preferencias']}")

    # Verifica se há usuários com preferências de produtos semelhantes
    for i in range(len(usuarios)):
        for j in range(i + 1, len(usuarios)):
            # Obtém os dicionários de usuários atualmente comparados
            usuario1 = usuarios[i]
            usuario2 = usuarios[j]
            # Verifica se há interseção entre os conjuntos de preferências de produtos dos usuários
            if usuario1['preferencias'].intersection(usuario2['preferencias']):
                # Exibe uma mensagem indicando que os usuários têm preferências de produtos semelhantes
                print(f"\n{usuario1['nome']} e {usuario2['nome']} têm preferências de produtos semelhantes.")

# Função principal para executar o programa
if __name__ == "__main__":
    main()
