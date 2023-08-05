# lendo o primeiro termo e a razão de uma PA, mostrando os 10 primeiros termos da progressão usando a estrutura while.

print(20 * "=")
print('GERADOR DE PA')
print(20 * "=")

primeiro_termo = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
termo = primeiro_termo
cont = 1
décimo = primeiro_termo + (11 -1) * razao

while cont <= 10:
    print(f'{termo} ->', end=" ")
    termo += razao
    cont += 1
print('FIM')