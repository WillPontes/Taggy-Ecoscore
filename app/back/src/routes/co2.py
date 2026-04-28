from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

from src.services.co2_service import calcular_co2_evitado

router = APIRouter()


class CalculoCO2Request(BaseModel):
    tipo_combustivel: str
    litros_economizados: float


@router.post("/co2/calcular")
def calcular_co2(data: CalculoCO2Request):
    try:
        return calcular_co2_evitado(
            data.tipo_combustivel,
            data.litros_economizados
        )
    except ValueError as erro:
        raise HTTPException(status_code=400, detail=str(erro))