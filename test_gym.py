"""Unit tests for R1, R2, R3 and R7 of the gym membership quote."""
from gym import is_valid_plan, get_plan_price


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