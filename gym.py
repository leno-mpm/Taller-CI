"""Calculation functions for the gym membership quote."""

PLAN_PRICES = {
    "BASIC": 30,
    "STANDARD": 45,
    "PREMIUM": 70,
}


def is_valid_plan(plan):
    """R1: the plan must be one of the plans in the table."""
    return plan in PLAN_PRICES


def get_plan_price(plan):
    """R1: price per member of the plan, or -1 if the plan is invalid."""
    if not is_valid_plan(plan):
        return -1
    return PLAN_PRICES[plan]