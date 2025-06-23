from assertpy import assert_that

def test_negative_sum_scenario():
    x = 2
    y = 4
    assert x + y == 6

def test_negative_sum_scenario_assertpy():
    x = 2
    y = 4
    print(f"\nTesting if {x} + {y} equals 6")
    assert_that(x + y).is_equal_to(6)