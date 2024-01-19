# Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final, mostre:

valores = (int(input('Digite um número de 1 a 9: ')), int(input('Digite um número de 1 a 9: ')), int(input('Digite um número de 1 a 9: ')), int(input('Digite um número de 1 a 9: ')))

# A) Quantas vezes apareceu o valor 9.

print(f'O número 9 apareceu {valores.count(9)} vezes.')

# B) Em que posição foi digitado o primeiro valor 3.
if valores == 3:
    position = (valores.index(3)+1)
    print(f'A posição do primeiro valor 3 é {position}º')
else:
    print('O valor 3 não foi digitado em nenhum momento.')

# C) Quais foram os números pares.
print('Os valores que são pares é: ', end='')
for v in valores:
    if v % 2 == 0:
        
        print(v, end=' ')