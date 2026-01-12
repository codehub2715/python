#Try modifying a tuple and observe the error message (to understand immutability).

Tuple = (1,2,3,4,5)
print("Original Tuple:", Tuple)

List = list(Tuple)
print("List from tuple:", List)

List.append(6)
print("Modified List:", List)

New_Tuple = tuple(List)
print("New Tuple : ",New_Tuple)


#Output:
#Original Tuple: (1, 2, 3, 4, 5)
#List from tuple: [1, 2, 3, 4, 5]
#Modified List: [1, 2, 3, 4, 5, 6]
#New Tuple :  (1, 2, 3, 4, 5, 6)