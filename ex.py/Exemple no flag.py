# Crie um programa que leia vários números inteiros pelo teclado. 
# O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada. No final, mostre quantos números foram digitados e qual foi a soma entre eles (desconsiderando o flag).

número = 0
total = 0
cont = 0
while True:
    print(10 * '-=')
    número = int(input('Digite um número (digite 999 para parar): '))
    if número == 999:
        break
    total = total + número
    cont += 1
print(f'Foi digitado {cont} números e a soma entre eles é {total}!')