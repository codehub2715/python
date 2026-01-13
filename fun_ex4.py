#Write a function that accepts any number of numbers and returns their average using *args.
def average(numbers):
    return sum(numbers) / len(numbers)
print("Average :", average([100,200,300,400,500]))

#Output : 
#Average : 300.0
