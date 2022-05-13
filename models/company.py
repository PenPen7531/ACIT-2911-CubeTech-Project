import json
# from models.employee import Employee  # run this line when running the webapp
from employee import Employee


class Company():
    def __init__(self, name: str):
        if type(name) != str:
            raise TypeError
        self.name = name
        self.employees = []
        try:
            with open(f"data/{self.name}.json") as file:
                self.employees = [
                    Employee(
                        employee["first_name"],
                        employee["last_name"],
                        employee["employee_id"],
                        employee["employee_department"],
                        employee["employee_salary"],
                        employee["employee_age"],

                    ) for employee in json.load(file)
                ]
        except:
            self.employees = []

    def add(self, employee):
        if type(employee) is not Employee:
            raise TypeError
        self.employees.append(employee)

    def find_employee_by_id(self, employee_id):
        for employee in self.employees:
            if employee.employee_id == employee_id:
                return employee

    def find_employees_by_department(self, employee_department):
        employee_in_dept = []
        for employee in self.employees:
            if employee.employee_department == employee_department:
                employee_in_dept.append(employee)
        return employee_in_dept

    def delete(self, employee_id):
        employee = self.find_employee_by_id(employee_id)
        if employee:
            self.employees.remove(employee)
            return True
        return False

    def save(self):
        with open(f"data/{self.name}.json", "w") as file:
            json.dump([employee.to_dict()
                       for employee in self.employees], file)

    def salary_sum(self):
        total = 0
        for employees in self.employees:
            total += employees.employee_salary
        return total

    def employee_count(self):
        num_emp = len(self.employees)
        return num_emp
