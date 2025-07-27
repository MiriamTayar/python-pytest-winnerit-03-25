import requests # שליחת בקשות HTTP (GET, POST, DELETE וכו')
import pytest
from assertpy import assert_that
from dotenv import load_dotenv  # טעינת משתני סביבה מקובץ .env
import os  # גישה למשתני סביבה

load_dotenv() # טוען משתני סביבה מתוך קובץ .env

headers = {"x-api-key": os.getenv("X_API_KEY")}
base_api_url = "https://reqres.in/api"

#קריאה למשתמש לפי ID(GET)
def test_get_user_by_id():
    response = requests.get(f"{base_api_url}/users/2", headers=headers)
    assert_that(response.status_code).is_equal_to(200) # בדיקה שהתשובה מהשרת מחזירה קוד סטטוס 200
    response_body = response.json() # המרת תגובת השרת לפורמט JSON (כלומר למילון – dictionary) ושמירתו במשתנה בשם response_body.
    # print(response.ok)
    # print(response.reason)
          
    assert response_body["data"]["id"] == 2 # בדיקה שהתשובה כוללת id בתוך אובייקט data, ושווה ל־2.
    assert_that(response_body["data"]["email"]).is_equal_to("janet.weaver@reqres.in") #בדיקה שכתובת האימייל של המשתמש שהוחזר זה הכתובת הזו
    assert_that(response_body["support"]).contains_key("url")# בדיקה שבתוך האובייקט support (בתשובה) יש מפתח בשם "url"


    assert_that(response_body["support"]).contains_key("text") # בדיקה נוספת שבתוך support קיים גם המפתח "text"
    

# יצירת משתמש חדש (POST)
def test_create_new_user():
    payload  = {
        "name": "alex", 
        "job": "teacher"
    }
    
    response = requests.post(f"{base_api_url}/users", json=payload, headers=headers)
    assert response.status_code == 201
    response_body = response.json()
    assert_that(response_body["name"]).is_equal_to(payload["name"])
    assert_that(response_body["job"]).is_equal_to(payload["job"])
    assert_that(response_body).contains_key("id")
    assert_that(response_body).contains_key("createdAt")
    assert response.reason == "Created"
    

# מחיקת משתמש לפי ID (DELETE)
def test_delete_user_by_id():
    response = requests.delete(f"{base_api_url}/users/2", headers=headers)
    assert response.status_code == 204
    assert response.reason == "No Content"
    

# עדכון משתמש לפי ID (PATCH)
def test_patch_user_by_id():
    payload = {"name": "morpheus", "job": "zion resident"}
    response = requests.patch(f"{base_api_url}/users/2", json=payload, headers=headers)
    assert response.status_code == 200
    assert response.reason == "OK"
    
    
# class work ~~~~

# Single User Not Found
def test_single_user_not_found():
    response = requests.get(f"{base_api_url}/users/999", headers=headers)
    assert response.status_code == 404
    assert response.reason == "Not Found"

# Login - Successful
def test_login_successful():
    payload = {
        "email": "eve.holt@reqres.in",  # אימייל תקין לפי האתר
        "password": "cityslicka"        # סיסמה תקינה לפי הדוקומנטציה
    }
    response = requests.post(f"{base_api_url}/login", json=payload, headers=headers)
    assert_that(response.status_code).is_equal_to(200)

    response_body = response.json()
    assert "token" in response_body


# הפונקציה הזו דרושה תיקון!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# Login - Unsuccessful
def test_login_unsuccessful():
    payload = {
        "email": "eve.holt@reqres.in"  
    }
    response = requests.post(f"{base_api_url}/login", json=payload)
    assert_that(response.status_code).is_equal_to(400)  
    response_json = response.json()
    assert_that(response_json).contains_key("error")
    assert_that(response_json["error"]).is_equal_to("Missing password")