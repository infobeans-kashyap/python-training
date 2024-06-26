# Basics of Python part-6 (oops concepts with inheritance)

class Employee:
    first_nm = '';
    last_nm = '';
    raise_amount = 1.04

    def __init__(self, first_nm, last_nm, salary) -> None:
        self.first_nm = first_nm
        self.last_nm = last_nm
        self.salary = salary
    
    def getFirstName(self):
        return self.first_nm

    def raise_pay(self):
        self.salary = int(self.salary * self.raise_amount)
    
    @classmethod
    def set_raise_amt(cls, amount):
        cls.raise_amount = amount

class Developer(Employee):
    def __init__(self, first_nm, last_nm, salary, prog_lang) -> None:
        super().__init__(first_nm, last_nm, salary)
        self.prog_lang = prog_lang

class Manager(Employee):
    def __init__(self, first_nm, last_nm, salary, employees=None) -> None:
        super().__init__(first_nm, last_nm, salary)
        if employees is None:
            self.employees = None
        else:
            self.employees = employees

    def add_employee(self,emp):
        if emp not in self.employees:
            self.employees.append(emp)
    
    def remove_employee(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)
        
    def print_employees(self):
        for emp in self.employees:
            print('Emp Managed : ', emp.first_nm)
    

emp = Developer('Xyz', 'Abc',1000, 'PHP')

print('Calling the inheriten class and using all the class variables of parent class', emp.first_nm)

# print('Visualizing the inheritance order', help(Developer))

print('Calling other functions & variables of the parent class using object of child class : ', emp.raise_amount)
emp.set_raise_amt(1.05)
print('Changing parent class variables using object of child class : ', emp.raise_amount)

emp = Developer('First', 'Last', 1000, 'PHP')
print('Overriding the init method of parent class in child class', emp.prog_lang)

emp_1 = Developer('Xyz', 'Abc',1000, 'PHP')
emp_2 = Developer('Abc', 'Def',1300, 'Python')

mgr_1 = Manager('Manager','Last', 90000, [emp_1])
print('List of employees managed by {}'.format(mgr_1.first_nm))
mgr_1.add_employee(emp_2)
mgr_1.print_employees()

print('Checking whether an object is an instance of a given class using isinstance method :', isinstance(mgr_1,Manager))

print('Checking whether a class is a child of a given parent class using issubclass method :', issubclass(Manager, Employee))