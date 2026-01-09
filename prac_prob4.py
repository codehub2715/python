#Input marks and print grade:
#- 90–100: A
#- 80–89: B
#- 70–79: C
#- 60–69: D
#- Below 60: F

Marks = float(input("Enter your marks: "))
if 90 <= Marks <= 100:
    print("Grade:A")
elif 80 <= Marks < 90:
    print("Grade:B")
elif 70 <= Marks < 80:
    print("Grade:C")
elif 60 <= Marks < 70:
    print("Grade:D")
else:
    print("Grade:F")

#Output:
#Enter your marks: 85
#Grade:B

