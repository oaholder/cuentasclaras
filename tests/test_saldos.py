import pytest

from cuentasclaras.saldos import Gasto, calcular_saldos, dividir_en_partes_iguales


def test_division_exacta():
    partes = dividir_en_partes_iguales(3000, ["ana", "luis", "marta"])
    assert partes == {"ana": 1000, "luis": 1000, "marta": 1000}


def test_division_no_pierde_centavos():
    partes = dividir_en_partes_iguales(1000, ["ana", "luis", "marta"])
    assert sum(partes.values()) == 1000
    assert max(partes.values()) - min(partes.values()) <= 1


def test_monto_invalido():
    with pytest.raises(ValueError):
        dividir_en_partes_iguales(0, ["ana"])
    with pytest.raises(ValueError):
        dividir_en_partes_iguales(500, [])


def test_saldos_suman_cero():
    gastos = [
        Gasto("renta", "ana", 1000001, ("ana", "luis", "marta")),
        Gasto("compras", "luis", 2501, ("ana", "luis")),
        Gasto("internet", "marta", 99999, ("ana", "luis", "marta")),
    ]
    assert sum(calcular_saldos(gastos).values()) == 0
