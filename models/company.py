import json
from models.employee import Employee


class Company():
    def __init__(self, name: str):
        if type(name) != str:
            raise TypeError
        self.name = name
        self.employees = []
        try:
            file = open(f"data/{self.name}.json")
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
        except:
            self.employees = []

    def save(self):
        employee_list = []
        for employee in self.employees:
            emp_dict = employee.to_dict()
            employee_list.append(emp_dict)
        file = open(f"data/{self.name}.json", "w")
        file.write(json.dumps(employee_list))

    def delete(self, emp_id):
        for i, employee in enumerate(self.employees):
            if employee.employee_id == emp_id:
                self.employees.pop(i)
                return True
        return False

    def add(self, employee):
        if isinstance(employee, Employee):
            self.employees.append(employee)

    def find_employee_by_id(self, emp_id):
        for employee in self.employees:
            if employee.employee_id == emp_id:
                return employee

    def find_employees_by_department(self, department):
        employee_in_dept = []
        for employee in self.employees:
            if employee.employee_department == department:
                employee_in_dept.append(employee)
        return employee_in_dept
