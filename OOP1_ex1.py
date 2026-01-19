#Create a class called Book with attributes title and author. Add a method to display them.
class Book:
    def __init__(self,title, author):
        self.title = title
        self.author = author
    def display_info(self):
        print(f"Title: {self.title}, Author: {self.author}")
book1 = Book("1984", "George Orwell")
book1.display_info()



    
