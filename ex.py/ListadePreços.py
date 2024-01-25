#  Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços, na sequência. No final, mostre uma listagem de preços, organizando os dados em forma tabular.

infoproduto = ('Sabão em pó', 20, 
               'Detergente', 12, 
               'Amaciante', 22,
               'Sabonete', 2.75,
               'Colgate', 5.25,
               'Chuveiro', 9)
print('-' * 40)
print(f'{"LISTAGEM DE PREÇOS":^40}')
print('-' * 40)
for pos in range(0, len(infoproduto)):
    if pos % 2 == 0:    
        print(f'\n{infoproduto[pos]:.<30}', end='')
    else:
        print(f'R${infoproduto[pos]:.2f}', end='')
print('-' * 40)