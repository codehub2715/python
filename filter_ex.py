# Use filter() to select names that start with the letter 'A'.
name = ['Alice', 'Bob','John', 'Amita']
filtered_names = list(filter(lambda x: x.startswith('A'),name))
print("Names starting with A:", filtered_names)

#Output:
#Names starting with A: ['Alice', 'Amita']