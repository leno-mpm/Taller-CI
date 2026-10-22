def apply_group_discount(amount, members):
    if members >= 2:
        return amount * 0.9
    return amount

def apply_special_offer(amount):
    if amount > 400:
        return amount - 50
    if amount > 200:
        return amount - 20
    return amount

def apply_premium_surcharge(amount, has_premium_extra):
    if has_premium_extra:
        return amount * 1.15
    return amount