from random import randint
print(20*'-=')
print('VAMOS JOGAR PAR OU ÍMPAR') 
print(20*'-=')
v = 0
while True:
    n = int(input('Digite um valor: '))
    computador = randint(1, 10)
    total = n + computador
    tipo = " "
    while tipo not in 'PI':
        tipo = str(input('Par ou Ímpar? [P/I]')).strip().upper()[0]
    print(f'Você jogou {n} e o computador {computador}. Total de {total}', end=' ')
    print(f'DEU PAR' if total % 2 == 0 else 'DEU IMPAR')
    if tipo == 'P':
        if total % 2 == 0:
            print('Você ganhou!')
            v += 1
        else:
            print('Você perdeu!')
            break
    elif tipo == 'I':
        if total % 2 == 0:
            print('Você perdeu!')
            break
        else:
            print('Você ganhou!')
            v += 1
    print('Vamos jogar novamente...')
print(f'GAME OVER! Você venceu {v} vezes.')
        


