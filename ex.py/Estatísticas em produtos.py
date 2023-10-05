'''Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se o usuário vai continuar ou não. No final, mostre:

A) qual é o total gasto na compra.

B) quantos produtos custam mais de R$1000.

C) qual é o nome do produto mais barato'''

soma = totalmil = cont = menor = 0
barato = ''
while True:
    nomep = str(input('Nome do produto: '))
    preço = float(input('Preço do produto R$'))
    cont += 1
    if cont == 1 or preço < menor:
        menor = preço
        barato = nomep
    soma += preço
    if preço > 1000:
        totalmil += 1
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N]')).strip().upper()[0]
    if resp == 'N':
        break
print('{:-^40}'.format( 'FIM DO PROGRAMA' ))
print(f'O total gasto na compra foi de R${soma:.2f} reais')
print(f'{totalmil} produtos custam mais que R$1000.')
print(f'O produto {barato} é o mais barato custando {menor}')