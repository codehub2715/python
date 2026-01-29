#Use a generator expression to find the sum of squares of even numbers from 1 to 100.

sum_of_squares = sum(num**2 for num in range (1,101) if num%2==0)
print("Sum of squares of even numbers:", sum_of_squares)

#Output :
#Sum of squares of even numbers: 171700
