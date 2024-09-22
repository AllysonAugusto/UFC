# Função para adicionar uma nova pessoa
def adicionar_pessoa(pessoas):
    nome = input("Digite o nome da pessoa: ")  # Solicita o nome da pessoa ao usuário
    idade = int(input("Digite a idade da pessoa: "))  # Solicita a idade da pessoa ao usuário e converte para inteiro
    interesses = input("Digite os interesses da pessoa separados por vírgula: ").split(',')  # Solicita os interesses da pessoa ao usuário e os divide em uma lista
    pessoas[nome] = {'idade': idade, 'interesses': interesses}  # Adiciona as informações da pessoa ao dicionário 'pessoas'

# Função para adicionar uma nova atividade
def adicionar_atividade(atividades):
    nome = input("Digite o nome da atividade: ")  # Solicita o nome da atividade ao usuário
    data = input("Digite a data da atividade: ")  # Solicita a data da atividade ao usuário
    local = input("Digite o local da atividade: ")  # Solicita o local da atividade ao usuário
    atividades.append((nome, data, local))  # Adiciona uma tupla contendo informações da atividade à lista 'atividades'

# Função para associar atividades às pessoas com base nos interesses
def associar_atividades_pessoas(pessoas, atividades):
    for nome, info in pessoas.items():  # Itera sobre o dicionário de pessoas
        interesses = info['interesses']  # Obtém os interesses da pessoa
        atividades_interesse = []  # Lista para armazenar as atividades que interessam à pessoa
        for atividade in atividades:  # Itera sobre a lista de atividades
            if atividade[0] in interesses:  # Verifica se o nome da atividade está nos interesses da pessoa
                atividades_interesse.append(atividade)  # Se sim, adiciona a atividade à lista de atividades de interesse
        pessoas[nome]['atividades'] = atividades_interesse  # Associa as atividades de interesse à pessoa

# Função para listar informações de todas as pessoas
def listar_pessoas(pessoas):
    print("\nInformações das Pessoas:")  # Imprime cabeçalho
    for nome, info in pessoas.items():  # Itera sobre o dicionário de pessoas
        print(f"Nome: {nome}, Idade: {info['idade']}, Interesses: {', '.join(info['interesses'])}")  # Imprime informações da pessoa
        if 'atividades' in info:  # Verifica se a pessoa possui atividades associadas
            print("Atividades:", info['atividades'])  # Se sim, imprime as atividades associadas

# Função para listar informações de todas as atividades
def listar_atividades(atividades):
    print("\nInformações das Atividades:")  # Imprime cabeçalho
    for atividade in atividades:  # Itera sobre a lista de atividades
        print(f"Nome: {atividade[0]}, Data: {atividade[1]}, Local: {atividade[2]}")  # Imprime informações da atividade

# Função para verificar interesses duplicados
def verificar_interesses_duplicados(pessoas):
    interesses_duplicados = set()  # Conjunto para armazenar interesses duplicados
    interesses_vistos = set()  # Conjunto para armazenar interesses já vistos
    for nome, info in pessoas.items():  # Itera sobre o dicionário de pessoas
        interesses = info['interesses']  # Obtém os interesses da pessoa
        for interesse in interesses:  # Itera sobre os interesses da pessoa
            if interesse in interesses_vistos:  # Verifica se o interesse já foi visto anteriormente
                interesses_duplicados.add(interesse)  # Se sim, adiciona ao conjunto de interesses duplicados
            else:
                interesses_vistos.add(interesse)  # Se não, adiciona ao conjunto de interesses vistos
    if interesses_duplicados:  # Verifica se há interesses duplicados
        print("\nInteresses Duplicados:", interesses_duplicados)  # Se sim, imprime os interesses duplicados
    else:
        print("\nNão há interesses duplicados.")  # Se não, informa que não há interesses duplicados

# Função para verificar atividades no mesmo dia e local
def verificar_atividades_mesmo_dia_local(atividades):
    atividades_duplicadas = {}  # Dicionário para armazenar atividades duplicadas com base na data e local
    for atividade in atividades:  # Itera sobre a lista de atividades
        nome, data, local = atividade  # Desempacota a tupla de atividade
        chave = (data, local)  # Cria uma chave única com base na data e local da atividade
        if chave in atividades_duplicadas:  # Verifica se a chave já existe no dicionário
            atividades_duplicadas[chave].append(nome)  # Se sim, adiciona o nome da atividade à lista de atividades duplicadas
        else:
            atividades_duplicadas[chave] = [nome]  # Se não, cria uma nova entrada no dicionário
    for chave, atividades in atividades_duplicadas.items():  # Itera sobre o dicionário de atividades duplicadas
        if len(atividades) > 1:  # Verifica se há mais de uma atividade para a mesma data e local
            print(f"\nAtividades no mesmo dia e local ({chave}):", atividades)  # Se sim, imprime as atividades duplicadas

# Função principal
def main():
    pessoas = {}  # Dicionário para armazenar informações das pessoas
    atividades = []  # Lista de tuplas para armazenar informações das atividades

    while True:  # Loop principal do programa
        print("\n1. Adicionar Pessoa")
        print("2. Adicionar Atividade")
        print("3. Associar Atividades às Pessoas")
        print("4. Listar Pessoas")
        print("5. Listar Atividades")
        print("6. Verificar Interesses Duplicados")
        print("7. Verificar Atividades no Mesmo Dia e Local")
        print("8. Sair")
        opcao = input("\nEscolha uma opção: ")  # Solicita ao usuário que escolha uma opção

        if opcao == "1":  # Se a opção escolhida for adicionar pessoa
            adicionar_pessoa(pessoas)  # Chama a função para adicionar uma nova pessoa
        elif opcao == "2":  # Se a opção escolhida for adicionar atividade
            adicionar_atividade(atividades)  # Chama a função para adicionar uma nova atividade
        elif opcao == "3":  # Se a opção escolhida for associar atividades às pessoas
            associar_atividades_pessoas(pessoas, atividades)  # Chama a função para associar atividades às pessoas
        elif opcao == "4":  # Se a opção escolhida for listar pessoas
            listar_pessoas(pessoas)  # Chama a função para listar informações das pessoas
        elif opcao == "5":  # Se a opção escolhida for listar atividades
            listar_atividades(atividades)  # Chama a função para listar informações das atividades
        elif opcao == "6":  # Se a opção escolhida for verificar interesses duplicados
            verificar_interesses_duplicados(pessoas)  # Chama a função para verificar interesses duplicados
        elif opcao == "7":  # Se a opção escolhida for verificar atividades no mesmo dia e local
            verificar_atividades_mesmo_dia_local(atividades)  # Chama a função para verificar atividades no mesmo dia e local
        elif opcao == "8":  # Se a opção escolhida for sair do programa
            print("Saindo...")  # Informa que o programa está saindo
            break  # Encerra o loop
        else:  # Se a opção escolhida for inválida
            print("Opção inválida. Tente novamente.")  # Informa que a opção é inválida

if __name__ == "__main__":  # Verifica se o programa está sendo executado como o programa principal
    main()  # Chama a função principal
