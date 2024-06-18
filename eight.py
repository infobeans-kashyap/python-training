# Basics of Python part-8 (oops concepts with getter & setter methods)

class Employee:
    first_nm = '';
    last_nm = '';
    raise_amount = 1.04

    def __init__(self, first_nm, last_nm, salary) -> None:
        self.first_nm = first_nm
        self.last_nm = last_nm
        self.salary = salary
        # self.email = first_nm + '.' + last_nm + '@email.com'
    
    @property
    #converting the self.email computation to a setter method
    def email(self):
        return '{}.{}@email.com'.format(self.first_nm, self.last_nm)
    
    @property
    def fullname(self):
        return '{} {}'.format(self.first_nm, self.last_nm)

    @fullname.setter
    def fullname(self, name):
        self.first_nm, self.last_nm = name.split(' ')
    
    @fullname.deleter
    def fullname(self):
        print('Deletor method called ')
        self.first_nm = None
        self.last_nm = None

    def raise_pay(self):
        self.salary = int(self.salary * self.raise_amount)
    
    @classmethod
    def set_raise_amt(cls, amount):
        cls.raise_amount = amount

emp_1 = Employee('First', 'Last', 1000)
print('Calling the email attribute which is actually a function :', emp_1.email)

emp_1.fullname = 'Abc Xyz'

#calling the deletor method
del emp_1.fullname

print("Setting full name using the setter function ", emp_1.fullname)