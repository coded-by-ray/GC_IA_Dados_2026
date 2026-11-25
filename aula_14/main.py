from fastapi import FastAPI, HTTPException
from fruityvice import consultar_fruta, calcular_nutricao
from schemas import Suco, AtualizarSuco

app = FastAPI(title="API Casa de Sucos")


# Banco de dados em memória
sucos = {}


@app.get("/")
def inicio():
    return {
        "mensagem": "Bem-vindo à API Casa de Sucos! Acesse /docs"
    }


# GET - consultar informações nutricionais de uma fruta
@app.get("/frutas/{nome}")
def buscar_fruta(nome: str):
    return consultar_fruta(nome)


# POST - cadastrar um novo suco
@app.post("/sucos", status_code=201)
def criar_suco(suco: Suco):
    nutricao = calcular_nutricao(suco.frutas)

    novo_id = max(sucos.keys(), default=0) + 1

    novo_suco = {
        "id": novo_id,
        "nome": suco.nome,
        "frutas": suco.frutas,
        "tem_gosto_de": suco.tem_gosto_de,
        "total_calorias": nutricao["total_calorias"],
        "total_acucar": nutricao["total_acucar"]
    }

    sucos[novo_id] = novo_suco

    return novo_suco

# GET - listar todos os sucos cadastrados
@app.get("/sucos")
def listar_sucos():
    return list(sucos.values())

# PUT - atualizar as frutas de um suco
@app.put("/sucos/{id}")
def atualizar_suco(id: int, suco: AtualizarSuco):
    if id not in sucos:
        raise HTTPException(
            status_code=404,
            detail="Suco não encontrado."
        )

    nutricao = calcular_nutricao(suco.frutas)

    sucos[id]["frutas"] = suco.frutas
    sucos[id]["total_calorias"] = nutricao["total_calorias"]
    sucos[id]["total_acucar"] = nutricao["total_acucar"]

    return sucos[id]