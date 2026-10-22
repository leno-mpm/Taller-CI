from gym import apply_group_discount

def test_r4_one_member_no_discount():
    assert apply_group_discount(100, 1) == 100