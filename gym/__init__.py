"""Gym membership quote package: catalog, discounts and the quote pipeline."""

from .descuentos import (
    aplicar_descuento_grupal,
    aplicar_oferta_especial,
    aplicar_recargo_premium,
)

# Nombres compatibles con las pruebas del equipo
apply_group_discount = aplicar_descuento_grupal
apply_special_offer = aplicar_oferta_especial
apply_premium_surcharge = aplicar_recargo_premium
