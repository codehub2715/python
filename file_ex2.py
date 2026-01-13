#Write a list of names to a file, each on a new line.
names = ["Alice", "Bob", "AMit", "Rohit", "Mayur"]
with open("names.txt", "w") as file:
    for name in names:
        file.write(name + "\n")
        