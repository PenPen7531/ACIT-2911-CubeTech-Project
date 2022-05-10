import json
from models.admin import Admin
import os
from models.crypto import Crypto
class Login:
    def __init__(self):
        file = open("data/logins.json")
        logins = json.load(file)
        self.login=[]
        for login in logins:
            admin_username = login.get("username")
            admin_password = login.get("password")
            admin_database = login.get("database")

            admin_obj=Admin(admin_username, admin_password, admin_database)
            self.login.append(admin_obj)

    def find_login_by_username(self, username):
        for login in self.login:
            if login.username == username:
                return login
        return None

    def save(self):
        login_list = []
        for login in self.login:
            login_dict = login.to_dict()
            login_list.append(login_dict)
        file = open("data/logins.json", "w")
        file.write(json.dumps(login_list))

    def login_authenticate(self, username, password):
        enc_password=Crypto.enc_pass(password)
        print(enc_password)
        for login in self.login:
            print(login.password)
            if login.username==username and login.password==enc_password:
                return True
        return False 

    def add_login(self, admin):
        if isinstance(admin, Admin):
            self.login.append(admin)

    def check_database_name(self, database):
        for login in self.login:
            if login.database==database:
                return True
        return False

    def delete_admin(self, username):
        for i, user in enumerate(self.login):
            if user.username == username:
                self.login.pop(i)
                os.remove(f"./data/{user.database}.json")
                return True
        return False
            