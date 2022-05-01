import json
from flask import Flask, request, jsonify, render_template, redirect
import requests

from models.company import Company
from models.employee import Employee

app = Flask(__name__)
try:
    COMPANY = Company("BCIT")
except:
    print("Error, invalid JSON data")


def student_obj_to_dict(employees):
    employee_list = []
    for employee in employees:
        employee_dict = employee.to_dict()
        employee_list.append(employee_dict)
    return employee_list


@app.route("/", methods=["GET", "POST"])
def homepage():
    try:
        if request.method=="GET":
            return render_template("home.html", company=COMPANY), 201
        if request.method=="POST":
            department=request.form.get("department")
            print(department)
            return redirect("/department/"+department)
    except:
        return "Error", 404

@app.route("/view/<employee_id>")
def view(employee_id):
    employee=COMPANY.find_employee_by_id(employee_id)
    if employee!=None:
        return render_template("view.html", employee=employee, company=COMPANY), 201
    else:
        return "Employee not found", 404


@app.route("/create", methods=["GET", "POST"])
def create_page():
    if request.method == "GET":
        return render_template("create.html")

    if request.method == "POST":
        employee_fname = request.form.get("first_name")
        employee_lname = request.form.get("last_name")
        employee_id = request.form.get("employee_id")
        employee_department = request.form.get("employee_department")
        employee_salary = request.form.get("employee_salary")
        employee_age = request.form.get("employee_age")
        new_emp = Employee(employee_fname, employee_lname, employee_id, employee_department, int(employee_salary), int(employee_age))
        COMPANY.add(new_emp)
        COMPANY.save()
        return redirect("/")


@app.route("/delete/<employee_id>")
def delete(employee_id):
    if COMPANY.delete(employee_id):
        COMPANY.save()
        return redirect("/")
    else:
        return "Unsucessful", 404


@app.route("/edit/<employee_id>", methods=["GET", "POST"])
def put_user(employee_id):
    emp=COMPANY.find_employee_by_id(employee_id)
    if request.method=="GET":
        return render_template("edit.html", emp=emp)
    if request.method=="POST":
        emp_fname=request.form.get("first_name")
        emp_lname=request.form.get("last_name")
        emp_id=request.form.get("employee_id")
        emp_department=request.form.get("employee_department")
        emp_salary=request.form.get("employee_salary")
        emp_age=request.form.get("employee_age")
        if emp.first_name != emp_fname:
            emp.first_name = emp_fname
        if emp.last_name != emp_lname:
            emp.last_name=emp_lname
        if emp.employee_id!= emp_id:
            emp.employee_id=emp_id
        if emp.employee_department!= emp_department:
            emp.employee_department=emp_department
        if emp.employee_salary!=emp_salary:
            emp.employee_salary=int(emp_salary)
        if emp.employee_age!= emp_age:
            emp.employee_age= int(emp_age)
        COMPANY.save()
        return render_template("view.html", employee=emp, company=COMPANY)

@app.route("/department/<employee_department>")
def show_department(employee_department):
    print(employee_department)
    department=COMPANY.find_employees_by_department(employee_department)
    print(department[0].first_name)
    return render_template("department.html", department=department)

if __name__ == "__main__":
    app.run(debug=True)
