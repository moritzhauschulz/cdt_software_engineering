import numpy as np

class Book:
    def __init__(self, name, author):
        self.name = name
        self.author = author
    
    def __str__(self):
        return self.name + ' by ' + self.author
    
my_book = Book('A Book', 'Me')

print(my_book)