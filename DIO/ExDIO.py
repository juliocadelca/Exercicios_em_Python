def validar_dados(nome, idade, email):
    if idade < 0 or idade > 120:
        mensagem = "Dados Invalidos: Idade fora do intervalo permitido!"
    elif "@" not in email or "." not in email:
        mensagem = "Dados Invalidos: E-mail no formato incorreto!"
    else:
        mensagem = "Dados Validados com Sucesso!"
    return mensagem


# Solicitar entrada do usuário
nome = input()
idade = int(input())
email = input()

# Chamar a função validar_dados com os valores inseridos pelo usuário
resultado = validar_dados(nome, idade, email)

# Exibir o resultado
print(resultado)