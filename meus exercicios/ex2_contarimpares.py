inicio = int(input("Digite o inicio: "))
fim = int(input("Digite o fim: "))
soma = 0
for numero in range (inicio, fim + 1):
    if numero % 2 != 0:
        soma = soma + numero

print(soma)        