from unittest.util import strclass


class Admin:
    def __init__(self, admin_username, admin_password, admin_database):
        if type(admin_username) != str:
            raise TypeError
        self.username = admin_username
        if type(admin_password) != str:
            raise TypeError
        self.password = admin_password
        if type(admin_database) != str:
            raise TypeError
        self.database = admin_database
        

     

    def to_dict(self):
        '''
        this methods creates an array of employees
        and returns the dict of all the employees
        '''
        return {
            "username": self.username,
            "password": self.password,
            "database": self.database
            
        }