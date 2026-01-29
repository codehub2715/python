#Convert a list of strings to lowercase using set comprehension.

List = ["APPLE", "BANANA", "MANGO", "GRAPES", "STRAWBERRY"]
lowercase_list = {item.lower() for item in List}
print("Lowercase List:", lowercase_list)

#Output :
#Lowercase List: {'apple', 'banana', 'grapes', 'mango', 'strawberry'}