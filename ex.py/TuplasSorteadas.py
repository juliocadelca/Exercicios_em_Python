#  Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla. Depois disso, mostre a listagem de números gerados e também indique o menor e o maior valor que estão na tupla.

# 1° Gerar 5 números aleatórios e colocar em uma tupla.

from random import randint
Alet = (randint(0,9), randint(0,9), randint(0,9), randint(0,9), randint(0,9))
print(f'Os números sorteados foram: ', end='')
for n in Alet:
    print(f'{n}', end=' ')

# 3° Mostre o menos e o maior número.

maior = max(Alet)
menor = min(Alet)
print(f'\nO maior valor dentre eles é {maior}')
print(f'O menor valor dentre eles é {menor}')