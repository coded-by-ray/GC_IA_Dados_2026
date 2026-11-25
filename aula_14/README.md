# API Casa de Sucos

Projeto desenvolvido individualmente para a Aula 14
da trilha de Inteligência Artificial & Dados do
Geração Caldeira 2026.

## Sobre o projeto

A API Casa de Sucos permite consultar informações
nutricionais de frutas, cadastrar sucos, listar
os sucos cadastrados e atualizar suas composições.

A aplicação utiliza a API pública Fruityvice para
obter informações nutricionais e calcular o total
de calorias e açúcar, considerando 100 g de cada
fruta informada.

## Objetivos

- Desenvolver uma API REST com Python e FastAPI.
- Consumir uma API externa.
- Aplicar os métodos HTTP GET, POST e PUT.
- Manipular dados em formato JSON.
- Implementar validação de dados e tratamento de erros.
- Realizar testes utilizando o Swagger.

## Tecnologias utilizadas

- Python 3.12
- FastAPI
- Uvicorn
- Requests
- Pydantic
- Swagger UI
- Git e GitHub

## Estrutura do projeto

```text
aula_14/
├── evidencias/
├── .gitignore
├── fruityvice.py
├── main.py
├── schemas.py
├── requirements.txt
└── README.md
```

- `main.py`: aplicação principal e endpoints.
- `fruityvice.py`: integração com a API externa
  e cálculos nutricionais.
- `schemas.py`: modelos e validação dos dados.
- `evidencias/`: registros dos testes no Swagger.
- `requirements.txt`: dependências do projeto.
- `.gitignore`: arquivos ignorados pelo Git.

## Como executar

### 1. Acessar a pasta do projeto

```bash
cd aula_14
```

### 2. Criar o ambiente virtual

```bash
python -m venv .venv
```

### 3. Ativar o ambiente virtual

Windows (Git Bash):

```bash
source .venv/Scripts/activate
```

Windows (PowerShell):

```powershell
.\.venv\Scripts\Activate.ps1
```

Linux ou macOS:

```bash
source .venv/bin/activate
```

### 4. Instalar as dependências

```bash
python -m pip install -r requirements.txt
```

### 5. Executar a aplicação

```bash
python -m uvicorn main:app --reload
```

### 6. Acessar a documentação interativa

http://127.0.0.1:8000/docs

## 📡 Endpoints

| Método | Rota | Descrição |
|--------|------|-----------|
| GET | `/` | Página inicial |
| GET | `/frutas/{nome}` | Consultar uma fruta |
| POST | `/sucos` | Cadastrar um suco |
| GET | `/sucos` | Listar os sucos cadastrados |
| PUT | `/sucos/{id}` | Atualizar as frutas de um suco |

## Exemplo de cadastro

Requisição POST para `/sucos`:

```json
{
    "nome": "Vitamina Tropical",
    "frutas": ["banana", "strawberry"],
    "tem_gosto_de": "Tamarindo"
}
```

Resposta HTTP 201:

```json
{
    "id": 1,
    "nome": "Vitamina Tropical",
    "frutas": ["banana", "strawberry"],
    "tem_gosto_de": "Tamarindo",
    "total_calorias": 125,
    "total_acucar": 22.6
}
```

Os valores nutricionais são consultados diretamente
na Fruityvice, podendo variar conforme os dados
disponibilizados pela API externa.

## Desafio bônus

O endpoint PUT `/sucos/{id}` permite atualizar
as frutas de um suco cadastrado e recalcular
automaticamente seus valores nutricionais.

Exemplo de atualização:

```json
{
    "frutas": ["banana", "apple"]
}
```

## Tratamento de erros

| Código HTTP | Descrição |
|-------------|-----------|
| 200 | Requisição realizada com sucesso |
| 201 | Suco cadastrado com sucesso |
| 404 | Fruta ou suco não encontrado |
| 422 | Dados inválidos |
| 502 | Erro na resposta da API externa |
| 503 | Falha na conexão com a Fruityvice |

## Testes realizados

Os testes foram realizados utilizando o Swagger UI.

- Consulta de fruta existente.
- Consulta de fruta não encontrada.
- Cadastro de suco.
- Listagem dos sucos cadastrados.
- Atualização das frutas de um suco.
- Consulta do suco após atualização.
- Tentativa de atualização de suco inexistente.
- Tentativa de cadastro com fruta não encontrada.
- Tentativa de cadastro sem frutas.

As evidências dos testes estão disponíveis
na pasta `evidencias/`.

## Observações

- Os nomes das frutas devem ser informados em inglês.
- Os campos retornados pela aplicação estão em português.
- Os valores nutricionais consideram 100 g de cada fruta.
- As calorias são expressas em kcal e o açúcar em gramas.
- Os dados são armazenados em memória, portanto são
  perdidos quando o servidor é reiniciado.
- A aplicação depende de conexão com a internet
  para consultar a Fruityvice.

## Referências

- [Fruityvice](https://www.fruityvice.com/)
- [FastAPI](https://fastapi.tiangolo.com/)
- [Código de referência da Aula 14](https://github.com/lisiELD/GC_IA_DADOS_2026/tree/main/aula_14)

## Autora

Rayssa Soares da Silva

Estudante de Desenvolvimento de Sistemas |
Geração Caldeira 2026 — IA & Dados

[GitHub](https://github.com/coded-by-ray)