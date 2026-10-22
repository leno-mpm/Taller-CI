import pytest

from gym import apply_group_discount, apply_special_offer, apply_premium_surcharge

def test_r4_one_member_no_discount():
    assert apply_group_discount(100, 1) == 100

def test_r4_two_members_discount():
    assert apply_group_discount(100, 2) == 90

def test_r5_no_offer_at_200():
    assert apply_special_offer(200) == 200


def test_r5_minus_20_over_200():
    assert apply_special_offer(201) == 181


def test_r5_minus_20_at_400():
    assert apply_special_offer(400) == 380


def test_r5_minus_50_over_400():
    assert apply_special_offer(401) == 351

def test_r6_no_premium_no_surcharge():
    assert apply_premium_surcharge(100, False) == 100


def test_r6_premium_adds_15_percent():
    assert apply_premium_surcharge(100, True) == pytest.approx(115)