# 1 Melhorando e versionando este programa de PA.
# 2 Pergunte para o usuário se ele quer mostrar mais alguns termos.
# 3 O programa encerrará quando ele disser que quer mostrar 0 termos.



# Decoração
print(20 * "-=")
print('GERADOR DE PA 3.0')
print(20 * "-=")

# Lendo o primeiro termo e a razão da PA
primeiro_termo = int(input('Primeiro termo: '))
razao = int(input('Razão da PA: '))

# Criando acumuladores e contadores para funcionar dentro do while
termo = primeiro_termo
cont = 1
décimo = primeiro_termo + (11 -1) * razao
mais = 10
total = 0
while mais != 0:
    total = total + mais
    while cont <= total:
        print(f'{termo} ->', end=" ")
        termo += razao
        cont += 1
    mais = int(input('Quantos termos você quer mostrar a mais? '))
print(f'PA finalizada com {total} termos mostrados.')