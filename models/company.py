import enum
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

    def save(self):
        employee_list = []
        for employee in self.employees:
            emp_dict = employee.to_dict()
            employee_list.append(emp_dict)
        file = open("data/employees.json", "w")
        file.write(json.dumps(employee_list))

    def delete(self, emp_id):
        for i, employee in enumerate(self.employees):
            if employee.employee_id == emp_id:
                self.employees.pop(i)
                return True
        return False
