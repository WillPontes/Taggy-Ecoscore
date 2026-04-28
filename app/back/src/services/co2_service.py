FATORES_EMISSAO = {
    "gasolina": 2.239,
    "diesel": 2.631,
    "etanol": 1.510,
}


def calcular_co2_evitado(tipo_combustivel: str, litros_economizados: float) -> dict:
    tipo = tipo_combustivel.lower()

    if tipo not in FATORES_EMISSAO:
        raise ValueError("Tipo de combustível não suportado")

    if litros_economizados < 0:
        raise ValueError("Litros economizados não pode ser negativo")

    fator = FATORES_EMISSAO[tipo]
    co2_evitado = litros_economizados * fator

    return {
        "tipo_combustivel": tipo,
        "litros_economizados": litros_economizados,
        "fator_emissao_kg_co2_por_litro": fator,
        "co2_evitado_kg": round(co2_evitado, 3)
    }