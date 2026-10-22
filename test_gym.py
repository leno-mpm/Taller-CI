"""Unit tests for R4, R5 and R6 of the gym membership quote."""
from decimal import Decimal
import pytest

from gym import apply_group_discount, apply_special_offer, apply_premium_surcharge


def test_r4_one_member_no_discount():
    """R4: one member gets no discount."""
    assert apply_group_discount(73, 1) == 73


def test_r4_three_members_discount():
    """R4: three members get 10% off."""
    assert apply_group_discount(85, 3) == pytest.approx(76.5)


def test_r5_low_amount_no_offer():
    """R5: an amount far below 200 does not change."""
    assert apply_special_offer(137) == 137


def test_r5_no_offer_at_200():
    """R5: 200 is not over 200, so nothing is subtracted."""
    assert apply_special_offer(200) == 200


def test_r5_minus_20_over_200():
    """R5: over 200 subtracts 20."""
    assert apply_special_offer(263) == 243


def test_r5_minus_20_at_400():
    """R5: 400 is not over 400, so it still subtracts 20."""
    assert apply_special_offer(400) == 380


def test_r5_minus_50_over_400():
    """R5: over 400 subtracts 50 and not 70."""
    assert apply_special_offer(427) == 377


def test_r6_no_premium_no_surcharge():
    """R6: no premium extra, no surcharge."""
    assert apply_premium_surcharge(58, False) == 58


def test_r6_premium_adds_15_percent():
    """R6: a premium extra adds 15%."""
    assert apply_premium_surcharge(86, True) == Decimal("98.90")