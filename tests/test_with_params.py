import os #ספריה  לעבודה עם קבצים ונתיבים
import pytest
from assertpy import assert_that
import json #כדי לקרוא קובץ JSON שמכיל נתוני בדיקה


print("Current working directory:", os.getcwd())
print("File exists:", os.path.exists("tests/test_data.json"))


test_data = [
    (3, 5, 15),
    (4, 5, 20),
    (5, 5, 25),
    (2, 10, 20),
    (10, 10, 100),
    (0, 5, 0),
    (-1, 5, -5),
    (-2, -5, 10),
    (100, 1, 100),
    (7, 3, 21)
]


@pytest.mark.parametrize("x, y, result", test_data)
def test_result_of_multiplication(x, y, result):
    assert x * y == result
    assert_that(x * y).is_equal_to(result) #נותן שגיאות יותר ברורות וקריאות

#פונקציה זו מחזירה רשימה של טפלות עם (x, y, result) בדיוק כמו ברשימה הפנימית
def load_test_data_from_json():
    path = os.path.join(os.path.dirname(__file__), 'test_data.json')
    with open(path, 'r') as f:
        data = json.load(f)
    return [(item['x'], item['y'], item['result']) for item in data]

#פונקצית בדיקה ממש כמו הבדיקה הראשונה – רק שהפעם הנתונים מגיעים מקובץ חיצוני
@pytest.mark.parametrize("x, y, result", load_test_data_from_json())
def test_result_of_multiplication_with_external_json(x, y, result):
    assert x * y == result
    assert_that(x * y).is_equal_to(result)

# def test_result_of_multiplication():
#     x = 3
#     y = 5
#     assert x * y == 15


# def test_result_of_multiplic ation_2():
#     x = 4
#     y = 5
#     assert x * y == 20


# def test_result_of_multiplication_3():
#     x = 5
#     y = 5
#     assert x * y == 25

