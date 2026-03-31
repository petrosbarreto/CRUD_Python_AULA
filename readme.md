petros passou aqui 2 com owner UNIFG

# CRUD de Tasks com FastAPI

API simples de CRUD para cadastro de tasks, feita em Python com FastAPI.

## Requisitos

- Python 3.10+

## Como executar no Windows (PowerShell)

1. Criar ambiente virtual:

```powershell
python -m venv .venv
```

2. Ativar ambiente virtual:

```powershell
.\.venv\Scripts\Activate.ps1
```

3. Instalar dependências:

```powershell
python -m pip install -r requirements.txt
```

4. Iniciar a API:

```powershell
python -m uvicorn main:app --reload --host 127.0.0.1 --port 8000
```

## Como executar no Windows (CMD)

1. Criar ambiente virtual:

```cmd
python -m venv .venv
```

2. Ativar ambiente virtual:

```cmd
.venv\Scripts\activate.bat
```

3. Instalar dependências:

```cmd
python -m pip install -r requirements.txt
```

4. Iniciar a API:

```cmd
python -m uvicorn main:app --reload --host 127.0.0.1 --port 8000
```

## macOS/Linux (opcional)

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
python -m uvicorn main:app --reload --host 127.0.0.1 --port 8000
```

## Endereços

- API: http://127.0.0.1:8000
- Docs Swagger: http://127.0.0.1:8000/docs
- Docs ReDoc: http://127.0.0.1:8000/redoc

## Endpoints principais

- `GET /`
- `GET /tasks`
- `POST /tasks`
- `GET /tasks/{task_id}`
- `PUT /tasks/{task_id}`
- `DELETE /tasks/{task_id}`

## Continuidade da Aula: Repetição e Condicionais

Além do CRUD, este repositório agora inclui um módulo didático para prática de laços e controle de fluxo.

### Arquivo da aula

- `aula_repeticao.py`

Conteúdo implementado:

- Resumo teórico de cada estrutura para apoio à explicação
- Estrutura repetitiva com `while`
- Estrutura repetitiva com `for` e `range()`
- Loops aninhados
- Controle de fluxo com `break` e `continue`
- Exercícios integrados (condicional + repetição) com `TODO`

### Endpoints de apoio didático

- `GET /aula/repeticao/teoria`
- `GET /aula/repeticao/exemplos`
- `GET /aula/repeticao/while`
- `GET /aula/repeticao/for`
- `GET /aula/repeticao/controle-fluxo`
- `GET /aula/repeticao/exercicios`

### Como executar apenas os exemplos da aula

```bash
python aula_repeticao.py
```

## Entrega dos alunos via Pull Request

Objetivo: cada aluno deve resolver os exercícios no arquivo `aula_repeticao.py` e enviar a solução por PR.

Regras de entrega:

1. Criar branch a partir da main:

```bash
git checkout -b feat/exercicios-repeticao-<seu-nome>
```

2. Implementar apenas as funções com `TODO`:

- `ex1_contar_pares_while`
- `ex2_somar_impares_for`
- `ex3_login_tentativas_while`
- `ex4_condicional_repeticao_fizzbuzz`
- `ex5_media_aprovacao`

3. Fazer commit:

```bash
git add aula_repeticao.py
git commit -m "Resolve exercícios de repetição e condicional"
```

4. Enviar branch e abrir Pull Request para `main`.

Critérios de avaliação sugeridos:

- Correção lógica
- Uso adequado de laços e condicionais
- Legibilidade do código
- Cumprimento das regras de cada exercício

O repositório contém um template de PR em `.github/pull_request_template.md` para padronizar as entregas.

Boas práticas:

- Não manter gabaritos de resolução dentro deste repositório.
- Pedir que os alunos alterem apenas `aula_repeticao.py`.
- Revisar a lógica e o uso correto das estruturas de repetição no PR.

python -m pip install fastapi uvicorn

.venv\Scripts\python.exe -m uvicorn main:app --reload --host 127.0.0.1 --port 8000

python -m uvicorn main:app --reload
