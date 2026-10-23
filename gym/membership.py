"""R1-R7: combines the plan, extras, subtotal, discounts and rounding into
a single quote, so that the CLI (R8) has one pure function to call."""

from .cotizacion import (
    calculate_subtotal,
    has_premium_extra,
    is_valid_selection,
    round_total,
)
from .descuentos import (
    aplicar_descuento_grupal,
    aplicar_oferta_especial,
    aplicar_recargo_premium,
)

INVALID_QUOTE = {
    "subtotal": -1,
    "after_group_discount": -1,
    "after_special_offer": -1,
    "after_premium_surcharge": -1,
    "total": -1,
}


def quote_membership(plan, extras, members):
    """R1-R7: full breakdown of a membership quote.

    Returns a dict with subtotal, after_group_discount, after_special_offer,
    after_premium_surcharge and total. Every value is -1 if the selection
    is invalid.
    """
    if not is_valid_selection(plan, extras, members):
        return dict(INVALID_QUOTE)

    subtotal = calculate_subtotal(plan, extras, members)
    after_group_discount = aplicar_descuento_grupal(subtotal, members)
    after_special_offer = aplicar_oferta_especial(after_group_discount)
    after_premium_surcharge = aplicar_recargo_premium(
        after_special_offer, has_premium_extra(extras)
    )
    total = round_total(after_premium_surcharge)

    return {
        "subtotal": subtotal,
        "after_group_discount": after_group_discount,
        "after_special_offer": after_special_offer,
        "after_premium_surcharge": after_premium_surcharge,
        "total": total,
    }
