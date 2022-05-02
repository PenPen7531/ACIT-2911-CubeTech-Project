
import json
from flask import Flask, request, jsonify, render_template, redirect
import requests

from models.company import Company
from models.employee import Employee
from models.admin import Admin
from models.login import Login

app = Flask(__name__)

LOGIN = False


def student_obj_to_dict(employees):
    employee_list = []
    for employee in employees:
        employee_dict = employee.to_dict()
        employee_list.append(employee_dict)
    return employee_list


@app.route("/", methods=["GET", "POST"])
def login():
    global LOGIN
    LOGIN = False
    if request.method == "GET":
        return render_template("login.html"), 201
    if request.method == "POST":
        user = Login()
        username = request.form.get("username")
        password = request.form.get("password")
        authenicate = user.login_authenticate(username, password)
        if authenicate:

            user_data = user.find_login_by_username(username)

            global COMPANY
            COMPANY = Company(user_data.database)

            LOGIN = True
            return redirect("/view")
        else:
            return "Incorrect Credentials", 404


@app.route("/view", methods=["GET", "POST"])
def homepage():
    if LOGIN:
        try:
            if request.method == "GET":
                return render_template("home.html", company=COMPANY), 201
            if request.method == "POST":
                department = request.form.get("department")
                return redirect("/department/"+department)
        except:
            return "Error", 404
    else:
        return "Invalid Credentials. Unable to view data", 404


@app.route("/view/<employee_id>")
def view(employee_id):
    if LOGIN:
        employee = COMPANY.find_employee_by_id(employee_id)
        if employee != None:
            return render_template("view.html", employee=employee, company=COMPANY), 201
        else:
            return "Employee not found", 404
    else:
        return "Invalid Credentials. Unable to view employee", 404


@app.route("/create", methods=["GET", "POST"])
def create_page():
    if LOGIN:
        if request.method == "GET":
            return render_template("create.html")

        if request.method == "POST":
            employee_fname = request.form.get("first_name")
            employee_lname = request.form.get("last_name")
            employee_id = request.form.get("employee_id")
            employee_department = request.form.get("employee_department")
            employee_salary = request.form.get("employee_salary")
            employee_age = request.form.get("employee_age")
            employee_email = request.form.get("employee_email")
            employee_phone = request.form.get("employee_phone")
            employee_address = request.form.get("employee_address")
            employee_gender = request.form.get("employee_gender")
            date_hired = request.form.get("date_hired")
            new_emp = Employee(employee_fname, employee_lname, employee_id, employee_department, int(employee_salary), int(
                employee_age), employee_email, employee_phone, employee_address, employee_gender, date_hired)
            COMPANY.add(new_emp)
            COMPANY.save()
            return redirect("/view")
    else:
        return "Invalid Credentials. Unable to create new employee", 404


@app.route("/delete/<employee_id>")
def delete(employee_id):
    if LOGIN:
        if COMPANY.delete(employee_id):
            COMPANY.save()
            return redirect("/view")
        else:
            return "Unsucessful", 404
    else:
        return "Invalid Credentials. Unable to delete employee", 404


@app.route("/edit/<employee_id>", methods=["GET", "POST"])
def put_user(employee_id):
    if LOGIN:
        emp = COMPANY.find_employee_by_id(employee_id)
        if request.method == "GET":
            return render_template("edit.html", emp=emp)
        if request.method == "POST":
            emp_fname = request.form.get("first_name")
            emp_lname = request.form.get("last_name")
            emp_id = request.form.get("employee_id")
            emp_department = request.form.get("employee_department")
            emp_salary = request.form.get("employee_salary")
            emp_age = request.form.get("employee_age")
            if emp.first_name != emp_fname:
                emp.first_name = emp_fname
            if emp.last_name != emp_lname:
                emp.last_name = emp_lname
            if emp.employee_id != emp_id:
                emp.employee_id = emp_id
            if emp.employee_department != emp_department:
                emp.employee_department = emp_department
            if emp.employee_salary != emp_salary:
                emp.employee_salary = int(emp_salary)
            if emp.employee_age != emp_age:
                emp.employee_age = int(emp_age)
            COMPANY.save()
            return render_template("view.html", employee=emp, company=COMPANY)
    else:
        return "Invalid Credentials. Unable to edit employee", 404


@app.route("/department/<employee_department>")
def show_department(employee_department):
    if LOGIN:
        print(employee_department)
        department = COMPANY.find_employees_by_department(employee_department)
        return render_template("department.html", department=department)
    else:
        return "Invalid Credentials. Unable to view department", 404


@app.route("/logout")
def logout():
    if LOGIN:
        return redirect("/")
    else:
        return "Invalid Credentials. Login has not been done", 404


@app.route("/createAdmin", methods=["GET", "POST"])
def create_admin():
    if request.method == "GET":
        return render_template("createAdmin.html")

    if request.method == "POST":
        admin_username = request.form.get("username")
        admin_password = request.form.get("password")
        admin_database = request.form.get("database_name")
        new_admin = Admin(admin_username, admin_password, admin_database)
        users = Login()
        users.add_login(new_admin)
        users.save()
        new_company = Company(new_admin.database)
        new_company.save()
        return redirect("/")


if __name__ == "__main__":
    app.run(debug=True)
