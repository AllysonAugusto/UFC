"""
Crie uma tupla preenchida com os 20 primeiros colocados da tabela do campeonato brasileiro de futebol, na ordem de colocação.Depois mostre:
Os 5 primeiros colocados, os ultimos 4 colocados, times em ordem alfabetica, em queposicao está o time da chapecoense
"""

times = ('Corinthians', 'Palmeiras', 'Santos', 'Gremio', 'Cruzeiro',
           'Flamengo', 'Vasco', 'Chapecoense', 'Atlético', 'Botafogo', 
           'Bahia', 'Sao Paulo', 'Fluminense', 'Sport-Recife', 'EC Vitoria', 
           'Coritiba', 'Avai', 'Ponte Preta', 'Atletico-GO')

print('-=' * 15)
for t in times:
    print(t)
print('-=' * 15)

print(f'Os 5 primeiros são :{times[0:5]}')
print('-=' * 15)
print(f'Os 4 ultimos são:{times[-4:]}')
print('-=' * 15)
print(f'Times em ordem alfabética: {sorted(times)}')
print('-=' * 15)
print(f'A chapecoense se encontra na posição {times.index("Chapecoense")}')
print('-=' * 15)


