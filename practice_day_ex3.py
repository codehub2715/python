#Create a program that reads a file and counts how many lines, words, and characters it contains.
with open("sample.txt", "r") as file:
    content = file.read()
    lines = content.splitlines()
    line_count = len(lines)
    word_count = len(content.split())
    char_count = len(content)

    print("Number of Lines:", line_count)
    print("Number of Words:", word_count)
    print("Number of Characters:", char_count)
