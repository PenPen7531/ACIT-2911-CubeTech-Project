import json
from models.employee import Employee


class Company():
    def __init__(self, name: str):
        if type(name) != str:
            raise TypeError
        self.name = name
        self.employees = []
        file = open("data/employees.json")
        employees = json.load(file)
        for employee in employees:
            employee_first_name = employee.get("first_name")
            employee_last_name = employee.get("last_name")
            employee_id = employee.get("employee_id")
            employee_department = employee.get("employee_department")
            employee_salary = employee.get("employee_salary")
            employee_age = employee.get("employee_age")
            employee_obj = Employee(employee_first_name, employee_last_name,
                                    employee_id, employee_department, employee_salary, employee_age)
            self.employees.append(employee_obj)
