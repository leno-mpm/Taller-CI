"""Calculation functions for the gym membership quote."""


def apply_group_discount(amount, members):
    """R4: 10% discount when there are 2 or more members."""
    if members >= 2:
        return amount * 0.9
    return amount


def apply_special_offer(amount):
    """R5: subtract 50 if the amount is over 400, or 20 if it is over 200."""
    if amount > 400:
        return amount - 50
    if amount > 200:
        return amount - 20
    return amount


def apply_premium_surcharge(amount, has_premium_extra):
    """R6: add 15% if the selection has a premium extra."""
    if has_premium_extra:
        return amount * 1.15
    return amount