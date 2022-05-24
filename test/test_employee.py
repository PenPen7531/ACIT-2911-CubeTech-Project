import pytest
from models.employee import Employee


def test__init__():
    with pytest.raises(TypeError):
        Employee(0, 'bob', '19449', 'Emp Depart.', 200, 22, "something@something.com",
                 "7778889999", "75 Westend Ave", "male", "sunday june 22,2021")  # first name
    with pytest.raises(TypeError):
        Employee('George', 5, '5531', 'Department 3', 5325, 45, "something@something.com",
                 "7778889999", "75 Westend Ave", "male", "sunday june 22,2021")  # last name
    with pytest.raises(TypeError):
        Employee('George', 'Bob', 5325, 'George Dept.', 142, 16, "something@something.com",
                 "7778889999", "75 Westend Ave", "male", "sunday june 22,2021")  # employee id
    with pytest.raises(TypeError):
        Employee('Jake', 'Lod', '335', 5253, 444, 56, "something@something.com",
                 "7778889999", "75 Westend Ave", "male", "sunday june 22,2021")  # employee dept
    with pytest.raises(TypeError):
        Employee('Chris', 'Man', '553', '5253', '$152', 52, "something@something.com",
                 "7778889999", "75 Westend Ave", "male", "sunday june 22,2021")  # employee salary
    with pytest.raises(TypeError):
        Employee('Rob', 'Forger', '5253', '55521', 225, '17', "something@something.com",
                 "7778889999", "75 Westend Ave", "male", "sunday june 22,2021")  # employee age
    with pytest.raises(TypeError):
        Employee('Rob', 'Forger', '5253', '55521', 225, 17, 0, "7778889999",
                 "75 Westend Ave", "male", "sunday june 22,2021")  # employee email
    with pytest.raises(TypeError):
        Employee('Rob', 'Forger', '5253', '55521', 225, 17, "something@something.com",
                 777, "75 Westend Ave", "male", "sunday june 22,2021")  # employee phone
    with pytest.raises(TypeError):
        Employee('Rob', 'Forger', '5253', '55521', 225, 17, "something@something.com",
                 "7778889999", 000, "male", "sunday june 22,2021")  # employee address
    with pytest.raises(TypeError):
        Employee('Rob', 'Forger', '5253', '55521', 225, 17, "something@something.com",
                 "7778889999", "75 Westend Ave", 9, "sunday june 22,2021")  # employee gender
    with pytest.raises(TypeError):
        Employee('Rob', 'Forger', '5253', '55521', 225, 17, "something@something.com",
                 "7778889999", "75 Westend Ave", "male", 6789)  # employee date hired


def test_to_dict():
    christ = Employee(first_name="Christ", last_name="Rob", employee_id="247", employee_department="33162", employee_salary=75, employee_age=24,
                      employee_email="something@something.com", employee_phone="604-999-1212", employee_address="75 Westend Ave", employee_gender="male", date_hired="sunday june 12")
    assert christ.to_dict() == {"first_name": "Christ", "last_name": "Rob", "employee_id": "247", "employee_department": "33162", "employee_salary": 75, "employee_age": 24,
                                "employee_email": "something@something.com", "employee_phone": "604-999-1212", "employee_address": "75 Westend Ave", "employee_gender": "male", "date_hired": "sunday june 12"}


# Example testing w/ dictionaries:
# def test_student_to_dict():
#     tim = Student(name="Tim", student_id="A01209697", term=3)
#     assert tim.to_dict() == {"name": "Tim",
#                              "student_id": "A01209697", "term": 3}
