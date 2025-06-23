import pytest
from assertpy import assert_that


def test_assertion_raises():
    with pytest.raises(ZeroDivisionError) as err:
        5/0
    # assert "divisionnnnnnnn" in str(err.value)
    assert_that(f"{err.value}").is_equal_to('division by zero')