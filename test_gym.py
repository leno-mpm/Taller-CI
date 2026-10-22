"""Unit tests for R1, R2, R3 and R7 of the gym membership quote."""
from gym import (is_valid_plan, get_plan_price, is_valid_extras,
                 get_extras_price, has_premium_extra, is_valid_members,
                 calculate_subtotal)

def test_r1_valid_plans():
    """R1: the three plans of the table are valid."""
    assert is_valid_plan("BASIC")
    assert is_valid_plan("STANDARD")
    assert is_valid_plan("PREMIUM")


def test_r1_unknown_plan_is_invalid():
    """R1: a plan that is not in the table is invalid."""
    assert not is_valid_plan("GOLD")


def test_r1_empty_plan_is_invalid():
    """R1: an empty plan is invalid."""
    assert not is_valid_plan("")


def test_r1_plan_prices():
    """R1: each plan has its price."""
    assert get_plan_price("BASIC") == 30
    assert get_plan_price("STANDARD") == 45
    assert get_plan_price("PREMIUM") == 70


def test_r1_invalid_plan_price():
    """R1: an invalid plan returns -1."""
    assert get_plan_price("PLATINUM") == -1



def test_r2_no_extras_is_valid():
    """R2: choosing zero extras is valid."""
    assert is_valid_extras("STANDARD", [])


def test_r2_normal_extras_with_any_plan():
    """R2: non premium extras work with any plan."""
    assert is_valid_extras("BASIC", ["GROUP_CLASSES", "PERSONAL_TRAINING"])


def test_r2_unknown_extra_is_invalid():
    """R2: an extra that is not in the table is invalid."""
    assert not is_valid_extras("PREMIUM", ["SAUNA"])


def test_r2_premium_extra_with_premium_plan():
    """R2: premium extras are valid with the PREMIUM plan."""
    assert is_valid_extras("PREMIUM", ["SPA", "SPECIALIZED_PROGRAM"])


def test_r2_premium_extra_with_other_plan():
    """R2: a premium extra with another plan is invalid."""
    assert not is_valid_extras("STANDARD", ["PERSONAL_TRAINING", "SPA"])


def test_r2_extras_price():
    """R2: no extras = 0, GROUP_CLASSES + SPECIALIZED_PROGRAM = 15 + 40 = 55."""
    assert get_extras_price([]) == 0
    assert get_extras_price(["GROUP_CLASSES", "SPECIALIZED_PROGRAM"]) == 55


def test_r2_has_premium_extra():
    """R2: detects when there is a premium extra."""
    assert has_premium_extra(["PERSONAL_TRAINING", "SPA"])
    assert not has_premium_extra(["GROUP_CLASSES"])




def test_r3_valid_members():
    """R3: one or more members is valid."""
    assert is_valid_members(1)
    assert is_valid_members(7)


def test_r3_zero_members_is_invalid():
    """R3: zero members is invalid."""
    assert not is_valid_members(0)


def test_r3_negative_members_is_invalid():
    """R3: a negative number of members is invalid."""
    assert not is_valid_members(-3)


def test_r3_subtotal_without_extras():
    """R3: subtotal with only the plan: 45 x 3 = 135."""
    assert calculate_subtotal("STANDARD", [], 3) == 135


def test_r3_subtotal_with_extras():
    """R3: (70 + 25 + 30) x 5 = 625."""
    assert calculate_subtotal("PREMIUM", ["PERSONAL_TRAINING", "SPA"], 5) == 625