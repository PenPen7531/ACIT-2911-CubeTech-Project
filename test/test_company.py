import pytest
from unittest.mock import mock_open, patch
from models.company import Company
from models.employee import Employee

JSON_FILE = """[
    {
       "first_name" : "Abeeha",
       "last_name": "Faisal",
       "employee_id" : "hiu38r031",
       "employee_department":"Human Resources",
       "employee_salary": 50000,
       "employee_age": 25,
        "employee_email": "latoyaoconnor@silodyne.com",
        "employee_phone": " +1 (828) 400-2521",
        "employee_address": "698 Joralemon Street, Dragoon, Wyoming, 8136",
        "employee_gender": "female",
        "date_hired": "Tue Sep 22 2015 12:45:41 GMT-0700 (Pacific Daylight Time)"
    },
        {
       "first_name" : "Jerry",
       "last_name": "Seinfeld",
       "employee_id" : "9875bgek",
       "employee_department":"Finance",
       "employee_salary": 65000,
       "employee_age": 56,
        "employee_email": "cervanteshendricks@silodyne.com",
        "employee_phone": " +1 (951) 510-3172",
        "employee_address": "822 Lott Avenue, Gratton, Iowa, 7677",
        "employee_gender": "male",
        "date_hired": "Mon Jan 20 2020 02:32:15 GMT-0800 (Pacific Standard Time)"
    },
        {
       "first_name" : "Hamna",
       "last_name": "Ammar",
       "employee_id" : "325tgwgda",
       "employee_department":"Accounting",
       "employee_salary": 90000,
       "employee_age": 34,
        "employee_email": "ingramstephenson@silodyne.com",
        "employee_phone": " +1 (954) 536-2469",
        "employee_address": "570 Sands Street, Carrizo, Oklahoma, 5323",
        "employee_gender": "male",
        "date_hired": "Thu Nov 21 2019 10:05:43 GMT-0800 (Pacific Standard Time)"
    }
]"""


@pytest.fixture
@patch("builtins.open", new_callable=mock_open, read_data=JSON_FILE)
def bcit(mock_file):
    return Company("bcit")


@patch("builtins.open", new_callable=mock_open, read_data="[]")
def test_open(mock_file):
    bcit = Company(name="bcit")
    mock_file.assert_called_once()
    assert "data/bcit.json" in mock_file.call_args[0]


def test_invalid_name():
    with pytest.raises(TypeError):
        assert Company(name=22)


def test_attribute_company(bcit):
    assert bcit.name == "bcit"
    for employee in bcit.employees:
        assert type(employee) is Employee
    assert len(bcit.employees) == 3


def test_find_employee_by_id(bcit):
    mike = bcit.find_employee_by_id("hiu38r031")
    assert type(mike) is Employee
    assert mike.employee_id == "hiu38r031"


def test_find_employees_by_department(bcit):
    emps = bcit.find_employees_by_department("Finance")
    assert len(emps) == 1
    for employee in emps:
        assert employee.employee_department == "Finance"


def test_add_employee(bcit):
    john = Employee(first_name="John", last_name="Watts", employee_id="sdhhhh244",
                    employee_department="IT", employee_salary=90234, employee_age=36, employee_email="something@something.com", employee_phone="9999999", employee_address="56 w ave vancouver", employee_gender="male", date_hired="monday 22 april 2021")
    bcit.add(john)
    assert john in bcit.employees


def test_add_invalid(bcit):
    with pytest.raises(TypeError):
        john = None
        bcit.add(john)


def test_delete_employee(bcit):
    remove_emp = bcit.delete("hiu38r031")
    assert remove_emp is True

    for employee in bcit.employees:
        assert employee.employee_id != "hiu38r031"

    remove_emp = bcit.delete("hiu38r031")
    assert remove_emp is False


@patch("builtins.open", new_callable=mock_open)
def test_save(mock_file, bcit):
    bcit.save()
    mock_file.assert_called_once_with("data/bcit.json", "w")


JSON_STR_SALARY = """[
    {
       "first_name" : "Abeeha",
       "last_name": "Faisal",
       "employee_id" : "hiu38r031",
       "employee_department":"Human Resources",
       "employee_salary": "50000",
       "employee_age": 25,
        "employee_email": "latoyaoconnor@silodyne.com",
        "employee_phone": " +1 (828) 400-2521",
        "employee_address": "698 Joralemon Street, Dragoon, Wyoming, 8136",
        "employee_gender": "female",
        "date_hired": "Tue Sep 22 2015 12:45:41 GMT-0700 (Pacific Daylight Time)"
    },
    {
       "first_name" : "hareem",
       "last_name": "Fatima",
       "employee_id" : "kahh98y34",
       "employee_department":"IT",
       "employee_salary": "90000",
       "employee_age": 22,
        "employee_email": "ingramstephenson@silodyne.com",
        "employee_phone": " +1 (954) 536-2469",
        "employee_address": "570 Sands Street, Carrizo, Oklahoma, 5323",
        "employee_gender": "male",
        "date_hired": "Thu Nov 21 2019 10:05:43 GMT-0800 (Pacific Standard Time)"
    }
]"""


@pytest.fixture
@patch("builtins.open", new_callable=mock_open, read_data=JSON_STR_SALARY)
def bcit_fail(mock_file1):
    return Company("bcit")


@patch("builtins.open", new_callable=mock_open, read_data="[]")
def test_open1(mock_file1):
    bcit_fail = Company(name="bcit")
    mock_file1.assert_called_once()
    assert "data/bcit.json" in mock_file1.call_args[0]


def test_salary_sum_success(bcit):
    assert bcit.salary_sum() == 205000


def test_employee_count(bcit):
    assert bcit.employee_count() == 3


def test_employee_count_fail(bcit_fail):
    assert bcit_fail.employee_count() == 0
