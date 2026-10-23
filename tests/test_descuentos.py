"""Unit tests for R4, R5 and R6 of the gym membership quote."""
from decimal import Decimal

import pytest

from gym.descuentos import (
    aplicar_descuento_grupal,
    aplicar_oferta_especial,
    aplicar_recargo_premium,
)


# ==================================================
# R4: DESCUENTO GRUPAL
# ==================================================

@pytest.mark.parametrize(
    "monto, miembros, esperado",
    [
        (100, 1, 100),    # Un miembro: sin descuento
        (100, 2, 90),     # Dos miembros: 10% de descuento
        (200, 3, 180),    # Tres miembros: 10% de descuento
        (500, 4, 450),    # Cuatro miembros: 10% de descuento
    ],
)
def test_descuento_grupal(monto, miembros, esperado):
    """R4: descuento del 10% con dos o más miembros."""
    resultado = aplicar_descuento_grupal(monto, miembros)

    assert resultado == Decimal(str(esperado))


# ==================================================
# R5: OFERTA ESPECIAL
# ==================================================

@pytest.mark.parametrize(
    "monto, esperado",
    [
        (100, 100),    # Menor a 200: sin descuento
        (200, 200),    # Exactamente 200: sin descuento
        (201, 181),    # Mayor a 200: descuento de 20
        (300, 280),    # Descuento de 20
        (400, 380),    # Exactamente 400: descuento de 20
        (401, 351),    # Mayor a 400: descuento de 50
        (500, 450),    # Descuento de 50
    ],
)
def test_oferta_especial(monto, esperado):
    """R5: oferta especial según el monto, sin acumular descuentos."""
    resultado = aplicar_oferta_especial(monto)

    assert resultado == Decimal(str(esperado))


# ==================================================
# R6: RECARGO PREMIUM
# ==================================================

@pytest.mark.parametrize(
    "monto, tiene_premium, esperado",
    [
        (100, False, 100),  # Sin extra premium
        (100, True, 115),   # Recargo del 15%
        (200, True, 230),   # Recargo del 15%
        (300, False, 300),  # Sin recargo
        (400, True, 460),   # Recargo del 15%
    ],
)
def test_recargo_premium(monto, tiene_premium, esperado):
    """R6: recargo del 15% cuando hay un extra premium."""
    resultado = aplicar_recargo_premium(
        monto,
        tiene_premium
    )

    assert resultado == Decimal(str(esperado))


# ==================================================
# PRUEBA DE INTEGRACION: R4 + R5 + R6
# ==================================================

def test_calculo_completo():
    """
    Verifica que los tres requerimientos
    funcionen correctamente en conjunto.
    """

    subtotal = Decimal("500")

    # R4: Descuento grupal del 10%
    monto = aplicar_descuento_grupal(subtotal, 3)

    assert monto == Decimal("450")

    # R5: Descuento especial de 50
    monto = aplicar_oferta_especial(monto)

    assert monto == Decimal("400")

    # R6: Recargo premium del 15%
    monto = aplicar_recargo_premium(monto, True)

    assert monto == Decimal("460")
