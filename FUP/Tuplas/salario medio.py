# Função para ler as informações de um funcionário e retorná-las como uma tupla
def ler_informacoes_funcionario():
    nome = input("Digite o nome do funcionário: ")
    cargo = input("Digite o cargo do funcionário: ")
    salario = float(input("Digite o salário do funcionário: "))
    return nome, cargo, salario

# Lista vazia para armazenar os funcionários
funcionarios = []

# Pedindo ao usuário para adicionar funcionários até que ele deseje parar
while True:
    adicionar = input("Deseja adicionar um novo funcionário? (S/N): ")
    if adicionar.upper() == "N":
        break
    novo_funcionario = ler_informacoes_funcionario()
    funcionarios.append(novo_funcionario)

# Função para calcular o salário médio dos funcionários
def calcular_salario_medio(funcionarios):
    total_salarios = sum(salario for _, _, salario in funcionarios)  # Somando os salários
    numero_funcionarios = len(funcionarios)  # Contando o número de funcionários
    return total_salarios / numero_funcionarios  # Calculando a média

# Exibindo informações sobre os funcionários
print("\nLista de Funcionários:")
for funcionario in funcionarios:
    print(f"Nome: {funcionario[0]}, Cargo: {funcionario[1]}, Salário: R$ {funcionario[2]:.2f}")

# Calculando e exibindo o salário médio dos funcionários
salario_medio = calcular_salario_medio(funcionarios)
print(f"\nSalário Médio: R$ {salario_medio:.2f}")
