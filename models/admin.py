class Admin:
    def __init__(self, admin_username, admin_password):
        if type(admin_username) != str:
            raise TypeError
        self.username = admin_username
        if type(admin_password) != str:
            raise TypeError
        self.password = admin_password

     

    def to_dict(self):
        '''
        this methods creates an array of employees
        and returns the dict of all the employees
        '''
        return {
            "username": self.username,
            "password": self.password,
            
        }
