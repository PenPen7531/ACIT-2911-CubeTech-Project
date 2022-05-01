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


@app.route("/")
def homepage():
    try:
        return render_template("home.html", company=COMPANY), 201
    except:
        return "Error", 404


@app.route("/create", methods=["GET", "POST"])
def create_page():
    if request.method == "GET":
        return render_template("create.html")
    if request.method == "POST":
        employee_fname = request.form.get("firstname")
        employee_lname = request.form.get("last_name")
        employee_id = request.form.get("employee_id")
        employee_department = request.form.get("employee_department")
        employee_salary = request.form.get("employee_salary")
        employee_age = request.form.get("employee_age")
        new_emp = Employee(employee_fname, employee_lname, employee_id,
                           employee_department, employee_salary, employee_age)
        COMPANY.add(new_emp)
        COMPANY.save()
        return render_template("home.html", company=COMPANY)


if __name__ == "__main__":
    app.run(debug=True)
