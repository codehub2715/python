#Write a function that prints details about a student using **kwargs (name, age, grade).

def student(**kwargs):
    for key, value in kwargs.items():
        print(key,value)
student(Name="Mayur", Age=21, Grade="A")

#Output:
#name Mayur
#age 21
#grade A
