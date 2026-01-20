# Try accessing private attributes directly vs using public methods. Observe the behavior.
class Employee:
    def __init__(self,name,salary):
        self.name = name
        self.__salary = salary 
    def get_salary(self):
        return self.__salary

    def set_salary(self,salary):
        if salary >=0:
            self.__salary = salary
        else :
            print("Invalid")

emp = Employee("Mayur" , 100000)
print(emp.get_salary())



