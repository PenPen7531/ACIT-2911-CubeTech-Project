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
            employee_email = employee.get("employee_email")
            employee_phone = employee.get("employee_phone")
            employee_address = employee.get("employee_address")
            employee_gender = employee.get("employee_gender")
            date_hired = employee.get("date_hired")
            employee_obj = Employee(employee_first_name, employee_last_name,
                                    employee_id, employee_department, employee_salary, employee_age, employee_email,
                                    employee_phone, employee_address, employee_gender, date_hired)
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
