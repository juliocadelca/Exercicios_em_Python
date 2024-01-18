# Crie um programa que tenha uma tupla totalmente preenchida com uma contagem por extenso, de zero até vinte. Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso.

# 1 Tupla totalmente preenchida com uma contagem por extenso de zero a vinte.

contagem = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 
            'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 
            'quatorze', 'quinze', 'dezeseis', 'dezesete', 'dezoito', 
            'dezenove', 'vinte')

# 2 Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso.

while True:
    digito = int(input("Digite um numero de 0 a 20: "))

    if 0 <= digito <= 20:
        print(f'Você digitou o número {contagem[digito]}')
        while True:
            continuar = str(input('Quer continuar? [S/N]'))
            if continuar == 'S':
                break
            if continuar == 'N':
                exit(print('Programa finalizado'))
            
            else:
                print('Tente novamente! >>[S/N]<< ', end="")
    else:
        print('Tente novamente! ', end="")