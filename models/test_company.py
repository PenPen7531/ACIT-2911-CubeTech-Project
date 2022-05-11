import pytest
from unittest.mock import mock_open, patch
from company import Company
from employee import Employee

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
                    employee_department="IT", employee_salary=90234, employee_age=36)
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
