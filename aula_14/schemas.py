from pydantic import BaseModel, Field


# Modelo para cadastro de sucos
class Suco(BaseModel):
    nome: str
    frutas: list[str] = Field(min_length=1)
    tem_gosto_de: str


# Modelo para atualização das frutas de um suco
class AtualizarSuco(BaseModel):
    frutas: list[str] = Field(min_length=1)