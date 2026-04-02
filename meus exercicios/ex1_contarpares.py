inicio = int(input("Digite o início: "))
fim = int(input("Digite o fim: "))
contagem = 0
numero = inicio
while numero <= fim:
    if numero % 2 == 0:
        contagem += 1
    numero += 1 
print(contagem)