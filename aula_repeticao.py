"""Exemplos e exercícios de estruturas de repetição.

Objetivo didático:
- Explicar o conceito de repetição de forma simples.
- Mostrar exemplos pequenos e previsíveis.
- Preparar o aluno para exercícios integrando condicional + repetição.

Organização:
- Bloco 1: teoria + exemplos resolvidos.
- Bloco 2: exercícios com TODO para entrega via PR.
"""


def teoria_repeticao_resumo() -> dict[str, str]:
    """Resumo teórico enxuto para apoiar explicação em sala.

    Linguagem simples para apresentar os conceitos antes do código.
    """
    return {
        "while": (
            "Use while quando a repetição depende de uma condição. "
            "Ele executa enquanto a condição for verdadeira."
        ),
        "for_range": (
            "Use for com range quando a quantidade de repetições é conhecida. "
            "Ex.: repetir de 1 até 10."
        ),
        "loops_aninhados": (
            "Loop dentro de loop. Muito usado para matrizes e tabelas. "
            "Ex.: linhas e colunas."
        ),
        "break": "Interrompe o laço imediatamente.",
        "continue": "Pula apenas a iteração atual e vai para a próxima.",
    }


def exemplo_while_contagem(limite: int) -> list[int]:
    """Retorna uma contagem de 1 até limite usando while.

    Teoria:
    - while é ideal quando a parada depende de uma condição.
    - Aqui, a condição é "contador <= limite".

    Passo a passo:
    1) Começa em 1
    2) Adiciona o valor atual na lista
    3) Incrementa contador
    4) Repete até passar do limite
    """
    numeros: list[int] = []
    contador = 1

    while contador <= limite:
        # Registra o estado atual antes de avançar o contador.
        numeros.append(contador)
        contador += 1

    return numeros


def exemplo_while_soma_ate_n(n: int) -> int:
    """Soma os números de 1 até n com while.

    Teoria:
    - Variável acumuladora: guarda o total parcial.
    - Variável de controle: indica em qual número estamos.
    """
    soma = 0
    atual = 1

    while atual <= n:
        # Acumula antes de passar para o próximo número.
        soma += atual
        atual += 1

    return soma


def exemplo_for_range_quadrados(inicio: int, fim: int) -> list[int]:
    """Retorna quadrados no intervalo [inicio, fim] com for e range.

    Teoria:
    - for percorre uma sequência.
    - range(inicio, fim + 1) gera valores incluindo o fim.
    """
    quadrados: list[int] = []

    for numero in range(inicio, fim + 1):
        # Regra de formação: quadrado = numero * numero.
        quadrados.append(numero * numero)

    return quadrados


def exemplo_for_range_tabuada(numero: int) -> list[str]:
    """Gera tabuada de 1 a 10 para o número informado.

    Teoria:
    - Exemplo clássico de repetição com quantidade fixa (10 vezes).
    """
    linhas: list[str] = []

    for multiplicador in range(1, 11):
        resultado = numero * multiplicador
        linhas.append(f"{numero} x {multiplicador} = {resultado}")

    return linhas


def exemplo_loops_aninhados_matriz_3x3() -> list[list[int]]:
    """Cria uma matriz 3x3 com loops aninhados.

    Teoria:
    - Loop externo controla linhas.
    - Loop interno controla colunas.
    """
    matriz: list[list[int]] = []
    valor = 1

    for _ in range(3):
        linha: list[int] = []
        for _ in range(3):
            linha.append(valor)
            valor += 1
        matriz.append(linha)

    return matriz


def exemplo_break_continue(valores: list[int]) -> dict[str, list[int] | int]:
    """Demonstra break e continue em uma lista de inteiros.

    Regras:
    - Ignora números negativos (continue)
    - Para no primeiro zero (break)
    - Acumula positivos processados
    """
    processados: list[int] = []

    for valor in valores:
        if valor < 0:
            # Continua o laço sem processar negativos.
            continue
        if valor == 0:
            # Interrompe toda a repetição ao encontrar zero.
            break
        processados.append(valor)

    return {
        "processados": processados,
        "quantidade": len(processados),
    }


# -----------------------------
# EXERCÍCIOS (para os alunos)
# -----------------------------


def ex1_contar_pares_while(inicio: int, fim: int) -> int:
    """Exercício 1: contar quantos números pares existem entre inicio e fim."""
    # TODO: implementar com while.
    raise NotImplementedError("Implemente o Exercício 1")


def ex2_somar_impares_for(inicio: int, fim: int) -> int:
    """Exercício 2: somar os números ímpares entre inicio e fim."""
    # TODO: implementar com for e range.
    raise NotImplementedError("Implemente o Exercício 2")


def ex3_login_tentativas_while(senha_correta: str, tentativas: list[str]) -> bool:
    """Exercício 3: simular login com no máximo 3 tentativas.

    Regras:
    - Usar while
    - Retornar True se acertar dentro de 3 tentativas
    - Retornar False caso contrário
    """
    # TODO: implementar.
    raise NotImplementedError("Implemente o Exercício 3")


def ex4_condicional_repeticao_fizzbuzz(n: int) -> list[str]:
    """Exercício 4: FizzBuzz de 1 até n.

    Regras:
    - múltiplo de 3: "Fizz"
    - múltiplo de 5: "Buzz"
    - múltiplo de 3 e 5: "FizzBuzz"
    - caso contrário: o próprio número em string
    """
    # TODO: implementar.
    raise NotImplementedError("Implemente o Exercício 4")


def ex5_media_aprovacao(notas: list[float]) -> dict[str, float | str]:
    """Exercício 5 (integrado):

    Calcular média das notas com repetição e retornar status:
    - "Aprovado" se média >= 7
    - "Recuperação" se média >= 5 e < 7
    - "Reprovado" se média < 5

    Dica: usar laço para somar as notas e condicional para status.
    """
    # TODO: implementar.
    raise NotImplementedError("Implemente o Exercício 5")


def executar_demos() -> dict[str, object]:
    """Retorna uma visão consolidada para demonstração em aula.

    Inclui teoria resumida + exemplos prontos para facilitar explicação.
    """
    return {
        "teoria_resumo": teoria_repeticao_resumo(),
        "while_contagem": exemplo_while_contagem(5),
        "while_soma_ate_10": exemplo_while_soma_ate_n(10),
        "for_quadrados_1_5": exemplo_for_range_quadrados(1, 5),
        "for_tabuada_7": exemplo_for_range_tabuada(7),
        "aninhados_matriz_3x3": exemplo_loops_aninhados_matriz_3x3(),
        "break_continue": exemplo_break_continue([5, -2, 9, 0, 12]),
    }


if __name__ == "__main__":
    from pprint import pprint

    pprint(executar_demos())
