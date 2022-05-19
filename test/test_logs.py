import pytest 
from models.logs import Logs
from models.data import Data
from unittest.mock import mock_open, patch
import os

JSON_FILE = """[
    {
       "first_name" : "Abeeha",
       "last_name": "Faisal",
       "employee_id" : "hiu38r031",
       "employee_department":"Human Resources",
       "employee_salary": 50000,
       "employee_age": 25
    },
        {
       "first_name" : "Jerry",
       "last_name": "Seinfeld",
       "employee_id" : "9875bgek",
       "employee_department":"Finance",
       "employee_salary": 65000,
       "employee_age": 56
    },
        {
       "first_name" : "Hamna",
       "last_name": "Ammar",
       "employee_id" : "325tgwgda",
       "employee_department":"Accounting",
       "employee_salary": 90000,
       "employee_age": 34
    }
]"""



@patch("builtins.open", new_callable=mock_open, read_data="[]")
def test_open(mock_file):
    bcit = Logs("bcit")
    mock_file.assert_called_once()
    assert "data/bcit_logs.json" in mock_file.call_args[0]
    new_file=Logs("test123")

def test_invalid_name():
    with pytest.raises(TypeError):
        assert Logs(22)

def test_new_data():
    newfile=Logs("test123")
    new_data=Data("Jan 25", "12:00", "Access Data")
    newfile.add(new_data)

def test_invalid_add():
    newfile=Logs("test123")
    with pytest.raises(TypeError):
        newfile.add("Test")

def test_save():
    newfile=Logs("test123")
    new_data=Data("Jan 25", "12:00", "Access Data")
    newfile.add(new_data)
    newfile.save()
    os.remove("./data/test123_logs.json")
