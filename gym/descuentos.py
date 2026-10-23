
from decimal import Decimal


# ==================================================
# R4: DESCUENTO GRUPAL
# ==================================================

def aplicar_descuento_grupal(monto, miembros):
    """
    Aplica un descuento del 10% cuando hay
    dos o mas miembros.

    Parametros:
        monto: Subtotal de la membresia.
        miembros: Cantidad de miembros.

    Retorna:
        Monto despues de aplicar el descuento.
    """

    monto = Decimal(str(monto))

    if miembros >= 2:
        return monto * Decimal("0.90")

    return monto


# ==================================================
# R5: OFERTA ESPECIAL
# ==================================================

def aplicar_oferta_especial(monto):
    """
    Aplica una oferta especial sobre el monto
    obtenido despues del descuento grupal.

    Condiciones:
        Mayor a 400: descuento de 50.
        Mayor a 200: descuento de 20.
        200 o menos: sin descuento.

    Los descuentos no son acumulables.
    """

    monto = Decimal(str(monto))

    if monto > 400:
        return monto - Decimal("50")

    elif monto > 200:
        return monto - Decimal("20")

    return monto


# ==================================================
# R6: RECARGO PREMIUM
# ==================================================

def aplicar_recargo_premium(monto, tiene_extra_premium):
    """
    Aplica un recargo del 15% si el usuario
    selecciona al menos un extra premium.

    Extras premium:
        SPA
        SPECIALIZED_PROGRAM

    Parametros:
        monto: Valor despues de aplicar R5.
        tiene_extra_premium: True o False.

    Retorna:
        Monto con el recargo correspondiente.
    """

    monto = Decimal(str(monto))

    if tiene_extra_premium:
        return monto * Decimal("1.15")

    return monto
