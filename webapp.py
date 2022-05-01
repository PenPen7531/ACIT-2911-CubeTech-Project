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


if __name__ == "__main__":
    app.run(debug=True)
