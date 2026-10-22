"""Calculation functions for the gym membership quote."""
from decimal import Decimal, ROUND_HALF_UP

PLAN_PRICES = {
    "BASIC": 30,
    "STANDARD": 45,
    "PREMIUM": 70,
}

# extra: (price per member, is premium)
EXTRAS = {
    "GROUP_CLASSES": (15, False),
    "PERSONAL_TRAINING": (25, False),
    "SPA": (30, True),
    "SPECIALIZED_PROGRAM": (40, True),
}


def is_valid_plan(plan):
    """R1: the plan must be one of the plans in the table."""
    return plan in PLAN_PRICES


def get_plan_price(plan):
    """R1: price per member of the plan, or -1 if the plan is invalid."""
    if not is_valid_plan(plan):
        return -1
    return PLAN_PRICES[plan]


def is_valid_extras(plan, extras):
    """R2: every extra must exist, and premium extras need the PREMIUM plan."""
    for extra in extras:
        if extra not in EXTRAS:
            return False
        is_premium = EXTRAS[extra][1]
        if is_premium and plan != "PREMIUM":
            return False
    return True


def get_extras_price(extras):
    """R2: sum of the prices per member of the chosen extras."""
    total = 0
    for extra in extras:
        total += EXTRAS[extra][0]
    return total


def has_premium_extra(extras):
    """R2: True if at least one of the extras is premium."""
    for extra in extras:
        if EXTRAS[extra][1]:
            return True
    return False




def is_valid_members(members):
    """R3: the number of members must be a whole number of at least 1."""
    return isinstance(members, int) and members >= 1


def calculate_subtotal(plan, extras, members):
    """R3: (plan price + price of the extras) x number of members."""
    return (get_plan_price(plan) + get_extras_price(extras)) * members



def is_valid_selection(plan, extras, members):
    """R7: the selection is valid only if the plan, extras and members are valid."""
    return (is_valid_plan(plan) and is_valid_extras(plan, extras)
            and is_valid_members(members))


def round_total(amount):
    """R7: round half up to a whole number (121.5 -> 122, 122.5 -> 123)."""
    return int(Decimal(str(amount)).quantize(Decimal("1"), rounding=ROUND_HALF_UP))


def final_result(plan, extras, members, amount):
    """R7: the rounded total, or -1 if the selection is invalid."""
    if not is_valid_selection(plan, extras, members):
        return -1
    return round_total(amount)