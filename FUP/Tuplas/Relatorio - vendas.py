"""
Você é um analista de dados em uma empresa de varejo e recebeu um arquivo CSV contendo dados de vendas anuais de diferentes produtos. Cada linha do arquivo contém o nome do produto, o mês em que as vendas ocorreram e o valor das vendas para esse produto e mês.

Você precisa criar um programa Python para processar esses dados e gerar um relatório que inclua as seguintes informações:

    Total de vendas para cada produto ao longo do ano.
    Mês em que cada produto teve o maior volume de vendas.
    Produto com o maior volume de vendas total no ano.
    Produto com o menor volume de vendas total no ano.
    Média mensal de vendas para todos os produtos.

Crie funções separadas para cada uma dessas tarefas e organize o código de forma modular e legível.
"""

# Função para adicionar uma venda aos dados de vendas
def adicionar_venda():
    produto = input("Digite o nome do produto: ")
    mes = input("Digite o mês da venda: ")
    valor_venda = float(input("Digite o valor da venda: "))
    return (produto, mes, valor_venda)

# Lista para armazenar os dados de vendas
dados_vendas = []

# Solicitar ao usuário que insira os dados de vendas
while True:
    opcao = input("Deseja adicionar uma venda? (S/N): ").upper()
    if opcao == 'S':
        dados_vendas.append(adicionar_venda())
    elif opcao == 'N':
        break
    else:
        print("Opção inválida. Por favor, digite S para sim ou N para não.")

# Total de vendas para cada produto ao longo do ano
total_vendas_produto = {}
for produto, mes, valor_venda in dados_vendas:
    if produto not in total_vendas_produto:
        total_vendas_produto[produto] = 0 #adiciona o produto ao dicionário com um total de vendas inicializado como zero
    total_vendas_produto[produto] += valor_venda # total de vendas para cada produto ao longo do ano

# Mês em que cada produto teve o maior volume de vendas
mes_maior_volume = {}
for produto, mes, valor_venda in dados_vendas:
    if produto not in mes_maior_volume or valor_venda > mes_maior_volume[produto][1]: #se o valor de venda atual é maior do que o valor de venda registrado anteriormente para esse produto
        mes_maior_volume[produto] = (mes, valor_venda) #atualiza o dicionário com o novo mês e valor de venda
 
# Produto com o maior volume de vendas total no ano
produto_maior_volume = max(total_vendas_produto, key=total_vendas_produto.get)

# Produto com o menor volume de vendas total no ano
produto_menor_volume = min(total_vendas_produto, key=total_vendas_produto.get)

# Média mensal de vendas para todos os produtos
total_meses = len(set(mes for _, mes, _ in dados_vendas))
total_vendas = sum(valor_venda for _, _, valor_venda in dados_vendas)
media_mensal_vendas = total_vendas / total_meses

# Exibindo o relatório
print("\nRelatório de Vendas:")
print("-------------------")
print("Total de vendas para cada produto ao longo do ano:")
for produto, total_vendas in total_vendas_produto.items():
    print(f"{produto}: R$ {total_vendas:.2f}")
print("\nMês em que cada produto teve o maior volume de vendas:")
for produto, (mes, valor_venda) in mes_maior_volume.items():
    print(f"{produto}: {mes} (R$ {valor_venda:.2f})")
print(f"\nProduto com o maior volume de vendas total no ano: {produto_maior_volume}")
print(f"Produto com o menor volume de vendas total no ano: {produto_menor_volume}")
print(f"Média mensal de vendas para todos os produtos: R$ {media_mensal_vendas:.2f}")
