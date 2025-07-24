from assertpy import  assert_that
import pytest

@pytest.mark.unit
def test_numbers_sum():
    assert  (2+2 == 5) == False

@pytest.mark.unit
def test_numbers_sum_assertpy():
    assert_that(2+2 == 5).is_false()

@pytest.mark.unit
def test_contains_substring():
    assert "abc" in "abcdefg"

@pytest.mark.unit
@pytest.mark.sanity
def test_contains_substring_assertpy():
    assert_that("abcdefg").contains("abc")

