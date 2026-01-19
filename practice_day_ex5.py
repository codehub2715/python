#Write a program using filter() that removes empty strings from a list.
strings = ["Vadodara" , "", "Ahmedabad" , "" , "Surat" , "Rajkot" , ""]
non_empty_strings = list(filter(lambda x: x != "", strings))
print("Non-empty strings:", non_empty_strings)

#Output:
#Non-empty strings: ['Vadodara', 'Ahmedabad', 'Surat', 'Rajkot']
