# Crie um programa que leia dois valores e mostre um menu na tela:

# [ 1 ] somar
# [ 2 ] multiplicar
# [ 3 ] maior
# [ 4 ] novos números
# [ 5 ] sair do programa

# Seu programa deverá realizar a operação solicitada em cada caso.


from time import sleep
primeiro_valor = int(input('Digite o primeiro valor: '))
segundo_valor = int(input('Digite o segundo valor: '))
escolha_menu = 0
while escolha_menu != 5:
    print('''[ 1 ] somar
[ 2 ] multiplicar
[ 3 ] maior
[ 4 ] novos números
[ 5 ] sair do programa''')
    escolha_menu = int(input('Qual é a sua opção: '))
    if escolha_menu == 1:
        somar = primeiro_valor + segundo_valor
        print(f'A soma entre {primeiro_valor} + {segundo_valor} é {somar}')
    elif escolha_menu == 2:
        multiplicar = primeiro_valor * segundo_valor
        print(f'A multiplicação de {primeiro_valor} x {segundo_valor} é {multiplicar}')
    elif escolha_menu == 3:
        if primeiro_valor > segundo_valor:
            maior = primeiro_valor
        else:
            maior = segundo_valor
        print(f'Entre {primeiro_valor} e {segundo_valor} o maior deles é {maior}')
    elif escolha_menu == 4:
        print('Informe os novos números:')
        primeiro_valor = int(input('Digite o primeiro valor: '))
        segundo_valor = int(input('Digite o segundo valor: '))
    elif escolha_menu == 5:
        print('Finalizando...')
    else:
        print('Opção inválida,tente novamente!')
    print('=-=' * 10)
    sleep(2)
print('Fim do programa! Volte sempre.')