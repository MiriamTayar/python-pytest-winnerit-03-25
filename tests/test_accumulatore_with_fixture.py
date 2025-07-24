import pytest
from pages.accumulator import Accumulator

#🔧 הגדרת fixture בשם accum_2
@pytest.fixture(scope="function") #ה־fixture ירוץ מחדש עבור כל פונקציית בדיקה שמשתמשת בו
def accum_2():
    print("Setting up accum_2 fixture")
    return Accumulator()  #מחזיר מופע חדש של Accumulator

#בדיקה האם שכשיוצרים מופע של Accumulator, המונה (count) מתחיל מ־0
def test_accum_creation(accum_2):
    assert accum_2.count == 0

# בדיקה שקריאה פעמיים ל־add_counts() מעלה את count ל־2
def test_add_counts_twice(global_accum):
    global_accum.add_counts()
    global_accum.add_counts()
    assert global_accum.count == 2

#משנה את ערך count ישירות ל־10 ובודקת שהוא באמת השתנה
def test_add_counts_with_params(accum_2):
    accum_2.count = 10
    assert accum_2.count == 10

#בודקת שה־fixture global_accum_with_10 מחזיר מופע של Accumulator שהתחיל עם count=10
def test_add_counts_with_global_10_accum(global_accum_with_10):
    assert global_accum_with_10.count == 10

