#Create a class Employee with attributes name and salary. Add a method to display salary with a bonus (10%).
class Employee:
    def __init__(self, name , salary):
        self.name = name
        self.salary = salary
    def display_salary(self):
        bonus = self.salary * 0.10
        total_salary = self.salary + bonus
        print(f"Salary of {self.name} with bonus is: {total_salary}")
emp1 = Employee("Alice", 500000)
emp1.display_salary()
emp2 = Employee("Bob", 700000)
emp2.display_salary()

#Output:
#Salary of Alice with bonus is: 550000.0
#Salary of Bob with bonus is: 770000.0