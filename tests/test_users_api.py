#  ~~~~~~~~~~~~~~~~~~ Home Work ~~~~~~~~~~~~~~~~~~
import requests
from assertpy import assert_that
import pytest

def test_get_all_users():
    url = "https://jsonplaceholder.typicode.com/users"
    response = requests.get(url)
    assert_that(response.status_code).is_equal_to(200)
    users = response.json()
    assert_that(users).is_length(10)

#  בדיקת קבלת משתמש ספציפי לפי מזהה
def test_get_user_by_id():
    url = "https://jsonplaceholder.typicode.com/users/1"
    response = requests.get(url)
    assert_that(response.status_code).is_equal_to(200)
    user = response.json()
    assert_that(user["name"]).is_equal_to("Leanne Graham")
    assert_that(user["email"]).is_equal_to("Sincere@april.biz")

# בדיקת תגובה למשתמש לא קיים
def test_get_nonexistent_user():
    url = "https://jsonplaceholder.typicode.com/users/999"
    response = requests.get(url)
    assert_that(response.status_code).is_equal_to(404)

# בדיקת מבנה נתוני המשתמש
def test_user_structure():
    url = "https://jsonplaceholder.typicode.com/users/2"
    response = requests.get(url)
    assert_that(response.status_code).is_equal_to(200)
    user = response.json()
    assert_that(user).contains_key("id")
    assert_that(user).contains_key("username")
    assert_that(user).contains_key("address")
    assert_that(user).contains_key("company")

    assert_that(user["address"]).contains_key("street")
    assert_that(user["company"]).contains_key("name")

# בדיקת מספר משתמשים בו-זמנית
@pytest.mark.parametrize("user_id, expected_name", [
    (1, "Leanne Graham"),
    (2, "Ervin Howell"),
    (3, "Clementine Bauch"),
    (4, "Patricia Lebsack"),
    (5, "Chelsey Dietrich")
])
def test_multiple_users_names(user_id, expected_name):
    url = f"https://jsonplaceholder.typicode.com/users/{user_id}"
    response = requests.get(url)
    assert_that(response.status_code).is_equal_to(200)
    user = response.json()
    assert_that(user["name"]).is_equal_to(expected_name)

