# Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo usuário.
# O programa será interrompido quando o número solicitado for negativo.
# **** obs: Melhorei o exercício 67 de python mundo 2 do Curso em Vídeo colocando um menu com mais opções de tabuada! ****

while True:
    n = int(input('Quer ver a tabuada de qual valor? (número negativo para o software!): '))
    print('_' * 70)
    if n < 0:
        break
    print(''' MENU DA TABUADA MELHORADA
    [ 1 ] Multiplicação
    [ 2 ] Divisão 
    [ 3 ] Subtração
    [ 4 ] Adição
    [ 5 ] Resto divisão
    [ 6 ] Potência
    Digite um número negativo (-1) para sair do programa!''')
    menu = int(input('Digite uma opção: '))
    if menu == 1:
        for c in range(1, 11):
            print(f'{n} x {c} = {n*c}')
    if menu == 2:
        for c in range (1, 11):
            print(f'{n} / {c} = {n/c:.2f}')
    if menu == 3:
        for c in range (1, 11):
            print(f'{n} - {c} = {n-c}')
    if menu == 4:
        for c in range (1, 11):
            print(f'{n} + {c} = {n+c}')
    if menu == 5:
        for c in range (1, 11):
            print (f'{n} / {c} resto = {n%c:.2f}')
    if menu == 6:
        for c in range (1, 11):
            print(f'{n} ^ {c} = {n**c}')
    print('_' * 70)
print('POGRAMA TABUADA ENCERRADO. Volte sempre!')