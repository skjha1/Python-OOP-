class Employee:

    def __init__(self, first, last, pay): 
        self.first = first
        self.last = last
        self.email = first + '.' + last + '@email.com'
        self.pay = pay

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

emp_1 = Employee('shivendra', 'jha', 50000)
emp_2 = Employee('Test', 'Employee', 60000)


# The __init__ method is the Python equivalent of the C++ constructor in an object-oriented approach. 
# The __init__ function is called every time an object is created from a class. 
# The __init__ method lets the class initialize the object's attributes and serves no other purpose. It is only used within classes.
