import requests
from fastapi import HTTPException

URL_BASE = "https://www.fruityvice.com/api/fruit"

def consultar_fruta(nome: str):
    nome = nome.strip().lower()

    try:
        resposta = requests.get(f"{URL_BASE}/{nome}", timeout=10)

    except requests.exceptions.RequestException:
        raise HTTPException(
            status_code=503,
            detail="Não foi possível conectar à API Fruityvice."
        )

    if resposta.status_code == 404:
        raise HTTPException(
            status_code=404,
            detail=f"Fruta '{nome}' não encontrada."
        )

    if resposta.status_code != 200:
        raise HTTPException(
            status_code=502,
            detail="Erro ao consultar a API Fruityvice."
        )

    dados = resposta.json()
    nutri = dados["nutritions"]

    return {
        "nome": dados["name"],
        "calorias": nutri["calories"],
        "acucar": nutri["sugar"]
    }

def calcular_nutricao(frutas: list[str]):
    total_calorias = 0
    total_acucar = 0

    for fruta in frutas:
        dados = consultar_fruta(fruta)

        total_calorias += dados["calorias"]
        total_acucar += dados["acucar"]

    return {
        "total_calorias": total_calorias,
        "total_acucar": round(total_acucar, 2)
    }