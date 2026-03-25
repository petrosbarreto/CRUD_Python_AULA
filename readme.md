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
