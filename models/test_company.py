from unittest.mock import mock_open, patch
import pytest 

from employee import Employee
from company import Company

JSON_TEST_FILE = """[
    {
        "first_name": "Hickman ",
        "last_name": "Mcmahon",
        "employee_id": "62702df9256cac249abe4d37",
        "employee_department": "Accounting",
        "employee_salary": 71623,
        "employee_age": 32,
        "employee_email": "hickmanmcmahon@silodyne.com",
        "employee_phone": " +1 (938) 494-3013",
        "employee_address": "631 Hendrickson Place, Marenisco, Nebraska, 8566",
        "employee_gender": "male",
        "date_hired": "Tue Dec 16 2014 12:36:58 GMT-0800 (Pacific Standard Time)"
    },

    {
    "first_name": "Taylor ",
    "last_name": "Bennett",
    "employee_id": "62702df918e32f099cf2da99",
    "employee_department": "Accounting",
    "employee_salary": 114135,
    "employee_age": 25,
    "employee_email": "taylorbennett@silodyne.com",
    "employee_phone": " +1 (834) 527-2073",
    "employee_address": "456 Melba Court, Dotsero, American Samoa, 8536",
    "employee_gender": "male",
    "date_hired": "Mon Nov 16 2015 07:35:15 GMT-0800 (Pacific Standard Time)"
    },

    {
    "first_name": "Howard ",
    "last_name": "Nolan",
    "employee_id": "62702df9452db7d9a4714606",
    "employee_department": "Accounting",
    "employee_salary": 118826,
    "employee_age": 28,
    "employee_email": "howardnolan@silodyne.com",
    "employee_phone": " +1 (976) 584-2782",
    "employee_address": "631 Livingston Street, Bainbridge, New York, 5664",
    "employee_gender": "male",
    "date_hired": "Fri Oct 28 2016 03:52:02 GMT-0700 (Pacific Daylight Time)"
  }
]"""

@pytest.fixture
@patch("builtins.open", new_callable=mock_open, read_data="[]")
def apple_test(mock_file):
    return Company("Apple")

@patch("builtins.open", new_callable=mock_open, read_data="[]")
def test_open(mock_file):
    apple = Company("Apple")
    mock_file.assert_called_once()
    assert "data/company.json" in mock_file.call_args[0] # fix file name


def test_attributes_company(apple):
    assert apple.name == "Apple"
    for employee in apple.employees:
        assert type(employee) is Employee
    assert len(apple) == 3

def test_save(apple):
    pass

