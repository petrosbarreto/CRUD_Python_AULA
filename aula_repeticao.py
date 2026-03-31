# -----------------------------
# EXERCÍCIOS (para os alunos)
# -----------------------------

def ex1_contar_pares_while(inicio: int, fim: int) -> int:
    contador = inicio
    quantidade_pares = 0

    while contador <= fim:
        if contador % 2 == 0:
            quantidade_pares += 1
        contador += 1

    return quantidade_pares


def ex2_somar_impares_for(inicio: int, fim: int) -> int:
    soma = 0

    for numero in range(inicio, fim + 1):
        if numero % 2 != 0:
            soma += numero

    return soma


def ex3_login_tentativas_while(senha_correta: str, tentativas: list[str]) -> bool:
    indice = 0

    while indice < 3 and indice < len(tentativas):
        if tentativas[indice] == senha_correta:
            return True
        indice += 1

    return False


def ex4_condicional_repeticao_fizzbuzz(n: int) -> list[str]:
    resultado: list[str] = []

    for numero in range(1, n + 1):
        if numero % 3 == 0 and numero % 5 == 0:
            resultado.append("FizzBuzz")
        elif numero % 3 == 0:
            resultado.append("Fizz")
        elif numero % 5 == 0:
            resultado.append("Buzz")
        else:
            resultado.append(str(numero))

    return resultado


def ex5_media_aprovacao(notas: list[float]) -> dict[str, float | str]:
    soma = 0.0

    for nota in notas:
        soma += nota

    media = soma / len(notas)

    if media >= 7:
        status = "Aprovado"
    elif media >= 5:
        status = "Recuperação"
    else:
        status = "Reprovado"

    return {
        "media": media,
        "status": status,
    }
print(ex1_contar_pares_while(1, 10))
print(ex2_somar_impares_for(1, 10))
print(ex3_login_tentativas_while("1234", ["1111", "1234"]))
print(ex4_condicional_repeticao_fizzbuzz(15))
print(ex5_media_aprovacao([7, 8, 6]))