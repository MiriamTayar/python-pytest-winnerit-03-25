from pages.calculator import add
from pages.discount_calculator import calculate_discount
import pytest

@pytest.mark.parametrize("x, y, result",[
    (1, 2, 3),
    (-1, 1, 0),
    (0, 0, 0),
    (5, 5, 10),
    (-3, -3, -6)
])
def test_addition(x, y, result):
    assert x + y == result


@pytest.mark.parametrize("discount_percent, expected",[
    (0, 100),  # בלי הנחה
    (10, 90),  # 10% הנחה
    (50, 50),  # 50% הנחה
    (100, 0),  # הנחה מלאה
])
def test_calculate_discount(bace_price, discount_percent, expected):
    assert calculate_discount(bace_price, discount_percent) == expected


