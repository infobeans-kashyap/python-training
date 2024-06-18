# Basics of Python part-6 (oops concepts with inheritance)

class Emp:
    first_nm = '';
    last_nm = '';
    def __init__(self) -> None:
        self.first_nm = 'Abc'
        self.last_nm = 'Xyz'
    
    def getFirstName(self):
        return self.first_nm
    
# creating object
emp = Emp()
print('Calling class method using object : ', emp.getFirstName())

class Emp2:
    #public variable
    raise_amount = 1.04

    def __init__(self, first_nm, last_nm, salary) -> None:
        self.first_nm = first_nm
        self.last_nm = last_nm
        self.salary = salary

    #regular methods
    def getFirstName(self):
        return self.first_nm
    
    def raise_pay(self):
        self.salary = int(self.salary * self.raise_amount)
    
    @classmethod
    def set_raise_amt(cls, amount):
        cls.raise_amount = amount
    
    @classmethod
    def alternative_constructor(cls,str):
        first_nm,last_nm, salary = str.split('-')     # this is similar to spread operator in javascript
        return cls(first_nm,last_nm, salary)
    
    @staticmethod
    def is_workday(day):
        #weekday() is a default method for days in python
        if day.weekday() == 5 or day.weekday() == 6:
            return 'It is a weekend'
        else:
            return 'It is a work day'
    
emp2 = Emp2('Xyz', 'Abc',1000)
emp2.raise_pay()
print('Parameterized init function (constructor)', emp2.getFirstName())
print('{} has a salary of {}'.format(emp2.getFirstName(), emp2.salary))
print('{} get a salary hike & updated salary is now {}'.format(emp2.getFirstName(), emp2.salary))

print('Printing out the name space of the class object', emp2.__dict__)

#calling the class method
Emp2.set_raise_amt(1.05)
print('Example usage of class methods, accessing class variables that changed : ', Emp2.raise_amount)

print('Example usage of class methods, accessing class variables via object of the class', emp2.raise_amount)

emp3 = Emp2.alternative_constructor('First-Last-2000')
print('Calling an alternate constructor in form of class method : ',emp3.first_nm, emp3.last_nm, emp3.salary)

import datetime

new_date = datetime.date(2024, 6, 18)
print('Calling a static method to check whether it is a weekend or workday :', Emp2.is_workday(new_date))