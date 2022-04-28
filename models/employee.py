class Employee:
    def __init__(self, first_name, last_name, employee_id, employee_department, employee_salary, employee_age):
        if type(first_name) != str:
            raise TypeError
        self.first_name = first_name

        if type(last_name) != str:
            raise TypeError
        self.last_name = last_name

        if type(employee_id) != str:
            raise TypeError
        self.employee_id = employee_id

        if type(employee_department) != str:
            raise TypeError
        self.employee_department = employee_department

        if type(employee_salary) != int:
            raise TypeError
        self.employee_salary = employee_salary

        if type(employee_age) != int:
            raise TypeError
        self.employee_age = employee_age

    def to_dict(self):
        '''
        this methods creates an array of employees
        and returns the dict of all the employees
        '''
        return {
            "first_name": self.first_name,
            "last_name": self.last_name,
            "employee_id": self.employee_id,
            "employee_department": self.employee_department,
            "employee_salary": self.employee_salary,
            "employee_age": self.employee_age
        }
