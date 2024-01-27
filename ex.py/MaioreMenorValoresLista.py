# Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista. Caso o número já exista lá dentro, ele não será adicionado. No final, serão exibidos todos os valores únicos digitados, em ordem crescente.

valores = list()
menor = 0
maior = 0
for c in range(0, 5):
    valores.append(int(input(f'Digite um valor na posição {c}: ')))
    if c == 0:
        maior = menor = valores[c]
    else:
        if valores[c] > maior:
            maior = valores[c]
        if valores[c] < menor:
            menor = valores[c]
    
print('=-' *40)
print(f'Você digitou os valores: {valores}')
print(f'\nO maior valor digitado foi {maior} nas posições', end=' ')
for p, v in enumerate(valores):
    if v == maior:
        print(f'{p}....', end=' ')

print(f'\nO menor valor digitado foi {menor} nas posições', end='')
for po, va in enumerate(valores):
    if va == menor:
        print(f'{po}....', end='')




