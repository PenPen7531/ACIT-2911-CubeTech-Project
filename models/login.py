import json
from models.admin import Admin
class Login:
    def __init__(self):
        file = open("data/logins.json")
        logins = json.load(file)
        self.login=[]
        for login in logins:
            admin_username = login.get("username")
            admin_password = login.get("password")
            admin_obj=Admin(admin_username, admin_password)
            self.login.append(admin_obj)

    def save(self):
        login_list = []
        for login in self.login:
            login_dict = login.to_dict()
            login_list.append(login_dict)
        file = open("data/logins.json", "w")
        file.write(json.dumps(login_list))

    def login_authenticate(self, username, password):
        for login in self.login:
            if login.username==username and login.password==password:
                return True
        return False 
            