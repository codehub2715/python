#Make a class Employee with name and salary. Derive Manager from Employee, adding department attribute.

class Employee :
    def __init__(self,name,salary):
        self.name = name
        self.salary = salary
    def display_info(self):
        print(f"Name: {self.name}, Salary: {self.salary}")

class Manager(Employee):
    def __init__(self,name,salary,department):
        self.name = name
        self.salary = salary
        self.department = department
    def display_info(self):
        print(f"Name: {self.name}, Salary: {self.salary}, Department: {self.department}")
emp = Employee("Alice", 500000)
emp.display_info()

mgr = Manager("Bob", 800000, "HR")
mgr.display_info()

