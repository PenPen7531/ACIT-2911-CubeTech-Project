class Data:
    def __init__(self, date,time, action):
        if type(date) != str:
            raise TypeError
        self.date = date

        if type(action) != str:
            raise TypeError
        self.action = action

        if type(time) != str:
            raise TypeError
        self.time=time
       

    def to_dict(self):
        '''
        this methods creates an array of employees
        and returns the dict of all the employees
        '''
        return {
            "date": self.date,
            "time": self.time,
            "action": self.action,
            
        }