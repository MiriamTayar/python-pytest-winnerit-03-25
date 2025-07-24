import requests
import pytest
from assertpy import assert_that
from dotenv import load_dotenv
import os

load_dotenv()

headers = {"x-api-key": os.getenv("X_API_KEY")}
base_api_url = "https://reqres.in/api"

def test_get_user_by_id():
    response = requests.get(f"{base_api_url}/users/2", headers=headers)
    assert_that(response.status_code).is_equal_to(200)
    response_body = response.json()
    # print(response.ok)
    # print(response.reason)
          
    assert response_body["data"]["id"] == 2
    assert_that(response_body["data"]["email"]).is_equal_to("janet.weaver@reqres.in")
    assert_that(response_body["support"]).contains_key("url")
    assert_that(response_body["support"]).contains_key("text")
    

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
    

def test_delete_user_by_id():
    response = requests.delete(f"{base_api_url}/users/2", headers=headers)
    assert response.status_code == 204
    assert response.reason == "No Content"
    

def test_patch_user_by_id():
    payload = {"name": "morpheus", "job": "zion resident"}
    response = requests.patch(f"{base_api_url}/users/2", json=payload, headers=headers)
    assert response.status_code == 200
    assert response.reason == "OK"
    
    
    
    
    