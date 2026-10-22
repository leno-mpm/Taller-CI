def apply_group_discount(amount, members):
    if members >= 2:
        return amount * 0.9
    return amount