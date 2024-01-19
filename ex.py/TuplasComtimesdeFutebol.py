# Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de Futebol, na ordem de colocação.

Campeonato = 'Palmeira', 'Grêmio', 'AtléticoMG', 'Flamengo', 'Botafogo', 'Bragantino', 'Fluminense', 'AtléticoPR', 'Internacional', 'Fotaleza', 'São Paulo', 'Cuiabá', 'Corinthians', 'Cruzeiro', 'Vasco', 'Bahia', 'Santos', 'Goiás', 'Coritiba', 'AméricaMG', 'Vitória'

# Depois mostre:
# a) Os 5 primeiros times.
print(('CAMPEONATO BASILEIRO DE FUTEBOL'))

for t in Campeonato:
    print(t)

cincopri = Campeonato[0:5]
print(30 * '-=-')
print(f'Os 5 primeiros colocados são {cincopri}')
print(30 * '-=-')

# b) Os últimos 4 colocados.

quatroulti = Campeonato[17:]
print(f'Os últimos 4 colocados são {quatroulti}')
print(30 * '-=-')

# c) Times em ordem alfabética.

print(sorted(Campeonato))
print(30 * '-=-')

# d) Em que posição está o time da São Paulo.

Position = Campeonato.index('São Paulo')
print(f'São paulo está na posição do campeonato {Position + 1}º e na tupla {Position}')
print(30 * '-=-')
print('FIM DO PROGRAMA')
