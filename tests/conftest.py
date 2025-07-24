from pages.accumulator import Accumulator
import pytest

@pytest.fixture
def global_accum():
    return Accumulator()

@pytest.fixture
def global_accum_with_10():
    return Accumulator(10)

@pytest.fixture
def bace_price():
    return 100