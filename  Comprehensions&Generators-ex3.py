# Write a generator function that yields Fibonacci numbers up to n terms.

def fibonacci_generator(n):
    a,b = 0,1
    for i in range(n):
        yield a
        a,b = b,a+b

n = int(input("Enter the number of terms: "))
fibonacci_sequence = list(fibonacci_generator(n))
print("Fibonacci Sequence:", fibonacci_sequence)

#Output :
#Enter the number of terms: 10
#Fibonacci Sequence: [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
