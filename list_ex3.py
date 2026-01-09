#Take 5 inputs from the user and store them in a list. Then print the reversed list.
inputs = []
for i in range(5):
    item = input("Enter item : ")
    inputs.append(item)
    print("List:", inputs)

reversed_list = inputs[::-1]
print("Reversed List:", reversed_list)



#Output :
#Enter item : apple
#List: ['apple']
#Enter item : banana
#List: ['apple', 'banana']
#Enter item : mango
#List: ['apple', 'banana', 'mango']
#Enter item : graps
#List: ['apple', 'banana', 'mango', 'graps']
#Enter item : strawberry
#List: ['apple', 'banana', 'mango', 'graps', 'strawberry']
#Reversed List: ['strawberry', 'graps', 'mango', 'banana', 'apple']