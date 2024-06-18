# Basics of Python part-7 (oops concepts with magic methods)

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

    def __repr__(self) -> str:
        return "Employee('{}','{}',{})".format(self.first_nm, self.last_nm, self.salary)
    
    def __str__(self) -> str:
        return "__str__ called : Employee('{}','{}',{})".format(self.first_nm, self.last_nm, self.salary)
    
    def __add__(self, other):
        return self.salary + other.salary

emp_1 = Developer('Xyz', 'Abc',1000, 'PHP')
emp_2 = Developer('Abc', 'Def',1300, 'Python')

mgr_1 = Manager('Manager', 'Last', 9000, [])
mgr_2 = Manager('Second', 'Manager', 12000, [])

print("Printing out an object by using the __repr__ magic method : ",mgr_1)
# repr(mgr_1)
# str(mgr_1)
print('The __add__ magic method for addition of 2 integers', int.__add__(1,2))

print('The __add__ magic method for addition of 2 attributes of an object', mgr_1 + mgr_2 )

