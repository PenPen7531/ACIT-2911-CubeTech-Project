import pytest
from employee import Employee
def test_init():
    new_employee=Employee("Jeff", "Wang", "A01", "Accounting", 25000, 23)
    assert new_employee.first_name=="Jeff"
    assert new_employee.last_name=="Wang"
    assert new_employee.employee_id=="A01"
    assert new_employee.employee_department=="Accounting"
    assert new_employee.employee_salary==25000
    assert new_employee.employee_age==23

def test_invalid__init__():
    with pytest.raises(TypeError):
        Employee(0, 'bob', '19449', 'Emp Depart.', 200, 22) #first name
    with pytest.raises(TypeError):
        Employee('George', 5, '5531', 'Department 3', 5325, 45) #last name
    with pytest.raises(TypeError):
        Employee('George', 'Bob', 5325, 'George Dept.', 142, 16) #employee id
    with pytest.raises(TypeError):
        Employee('Jake', 'Lod', '335', 5253, 444, 56) #employee dept
    with pytest.raises(TypeError):
        Employee('Chris', 'Man', '553', '5253', '$152', 52) #employee salary
    with pytest.raises(TypeError):
        Employee('Rob', 'Forger', '5253', '55521', 225, '17') #employee age

def test_to_dict():
    christ = Employee(first_name="Christ", last_name="Rob", employee_id="247", employee_department="33162", employee_salary=75, employee_age=24)
    assert christ.to_dict() == {"first_name": "Christ", "last_name": "Rob", "employee_id": "247", "employee_department": "33162", "employee_salary": 75, "employee_age": 24}










# Example testing w/ dictionaries:
# def test_student_to_dict():
#     tim = Student(name="Tim", student_id="A01209697", term=3)
#     assert tim.to_dict() == {"name": "Tim",
#                              "student_id": "A01209697", "term": 3}