#Write a program that takes a list of words and filters only those longer than 5 characters.
words = ["apple", "banana", "cherry", "date", "grape"]
long_words = list(filter(lambda x: len(x) > 5, words))
print("Words longer than 5 characters:", long_words)
