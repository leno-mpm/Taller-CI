"""R9: end-to-end tests of the full quote pipeline (R1-R7), using the
table from the workshop handout."""
import pytest

from gym.membership import INVALID_QUOTE, quote_membership


@pytest.mark.parametrize(
    "plan, extras, members, expected",
    [
        ("BASIC", [], 1, 30),
        ("STANDARD", ["PERSONAL_TRAINING"], 1, 70),
        ("BASIC", ["GROUP_CLASSES"], 2, 81),
        ("BASIC", ["GROUP_CLASSES"], 3, 122),
        ("STANDARD", ["GROUP_CLASSES", "PERSONAL_TRAINING"], 4, 286),
        ("PREMIUM", ["GROUP_CLASSES", "SPA"], 2, 215),
        ("PREMIUM", ["SPA", "SPECIALIZED_PROGRAM"], 3, 412),
        ("PREMIUM", ["SPA", "SPECIALIZED_PROGRAM", "PERSONAL_TRAINING"], 4, 626),
        ("BASIC", ["SPA"], 1, -1),
        ("GOLD", [], 1, -1),
        ("BASIC", [], 0, -1),
    ],
)
def test_quote_membership_table(plan, extras, members, expected):
    """R9: the handout's table of examples, run through the full pipeline."""
    assert quote_membership(plan, extras, members)["total"] == expected


def test_quote_membership_breakdown_on_valid_selection():
    """R9: a valid selection also exposes the intermediate amounts."""
    quote = quote_membership("PREMIUM", ["GROUP_CLASSES", "SPA"], 2)

    assert quote["subtotal"] == 230
    assert quote["after_group_discount"] == 207
    assert quote["after_special_offer"] == 187
    assert quote["total"] == 215


def test_quote_membership_breakdown_on_invalid_selection():
    """R9: an invalid selection reports -1 for every step."""
    quote = quote_membership("GOLD", [], 1)

    assert quote == INVALID_QUOTE
