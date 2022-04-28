import json
from flask import Flask, request, jsonify, render_template, redirect
import requests

from models.company import Company
from models.employee import Employee

app = Flask(__name__)

COMPANY = Company("BCIT")

@app.route("/")
def homepage():
    company = Company("BCIT")

    return render_template("home.html", company=COMPANY)

if __name__ == "__main__":
    app.run(debug=True)

