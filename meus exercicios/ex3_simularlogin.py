list = []
senha_correta = "biel2308"
while len(list) < 3:
    senha = input("Digite sua senha: ")
    list.append(senha)
    if senha == senha_correta:
        print("login feito!")
        break
    elif len(list) < 3:
        print("Senha incorreta, tente novamente")

    elif len(list) == 3 and senha != senha_correta:
        print("Senha incorreta, contate seu banco!")