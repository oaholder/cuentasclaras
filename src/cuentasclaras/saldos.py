"""Lógica central de CuentasClaras: saldos de gastos compartidos.

Los montos se manejan en centavos (enteros) para evitar errores de redondeo.
"""

from dataclasses import dataclass


@dataclass(frozen=True)
class Gasto:
    descripcion: str
    pagador: str
    monto_centavos: int
    participantes: tuple


def dividir_en_partes_iguales(monto_centavos, participantes):
    """Reparte un monto entre los participantes sin perder centavos.

    El resto (monto % n) se asigna de a 1 centavo a los primeros participantes.
    La diferencia entre dos partes nunca supera 1 centavo.
    """
    if monto_centavos <= 0:
        raise ValueError("El monto debe ser mayor que cero")
    if not participantes:
        raise ValueError("Debe haber al menos un participante")
    n = len(participantes)
    base, resto = divmod(monto_centavos, n)
    return {p: base + (1 if i < resto else 0) for i, p in enumerate(participantes)}


def calcular_saldos(gastos):
    """Devuelve {persona: saldo}. Positivo = le deben; negativo = debe."""
    saldos = {}
    for g in gastos:
        partes = dividir_en_partes_iguales(g.monto_centavos, list(g.participantes))
        saldos[g.pagador] = saldos.get(g.pagador, 0) + g.monto_centavos
        for persona, parte in partes.items():
            saldos[persona] = saldos.get(persona, 0) - parte
    return saldos
