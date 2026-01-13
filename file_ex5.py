#Count and print the number of lines in the file.
with open("names.txt", "r") as file:
    lines = file.readlines()
    line_count = len(lines)
    print("Number of Lines in the file:", line_count)
    