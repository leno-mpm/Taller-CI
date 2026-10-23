
import pytest
from decimal import Decimal

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
def aplicar_descuento_grupal(monto, miembros):
    """
    Aplica un descuento del 10% cuando hay dos o más miembros.

    Args:
        monto (Decimal): Subtotal de la membresía antes del descuento.
        miembros (int): Número de miembros de la membresía.

    Returns:
        Decimal: Monto después de aplicar el descuento grupal.
    """
    monto = Decimal(str(monto))

    if miembros >= 2:
        return monto * Decimal("0.90")

    return monto


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
def aplicar_oferta_especial(monto):
    """
    Aplica una oferta especial según el monto recibido.

    Se descuentan $50 si el monto es mayor a $400,
    o $20 si es mayor a $200. Los descuentos no se acumulan.

    Args:
        monto (Decimal): Monto después del descuento grupal.

    Returns:
        Decimal: Monto después de aplicar la oferta especial.
    """
    monto = Decimal(str(monto))

    if monto > 400:
        return monto - Decimal("50")

    if monto > 200:
        return monto - Decimal("20")

    return monto


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
def aplicar_recargo_premium(monto, tiene_extra_premium):
    """
    Aplica un recargo del 15% cuando se selecciona un extra Premium.

    Los extras Premium son SPA y SPECIALIZED_PROGRAM.

    Args:
        monto (Decimal): Monto después de aplicar la oferta especial.
        tiene_extra_premium (bool): Indica si existe un extra Premium.

    Returns:
        Decimal: Monto después de aplicar el recargo Premium.
    """
    monto = Decimal(str(monto))

    if tiene_extra_premium:
        return monto * Decimal("1.15")

    return monto


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
