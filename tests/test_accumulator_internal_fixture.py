from pages.accumulator import Accumulator
import pytest

#זהו fixture – פונקציה שמחזירה אובייקט של Accumulator
#pytest יריץ אותה לפני כל בדיקה שמבקשת את accum כפרמטר
@pytest.fixture
def accum():
    return Accumulator()


def test_accum_creation(accum):
    assert accum.count == 0


def test_add_counts_twice(global_accum):
    global_accum.add_counts()
    global_accum.add_counts()
    assert global_accum.count == 2

def test_add_counts_with_params():
    accum = Accumulator(10)
    assert accum.count == 10
