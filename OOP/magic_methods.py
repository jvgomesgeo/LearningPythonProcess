# Magic Methods = Dunder methods (double underscore) __init__, __str__, __eq__,
#                   They are automatically called by many of pythons built in operation
#                   They allow developers to define or customize the behavior of objects.




class Book:
    def __init__(self, title, author, num_pages):
        self.title = title
        self.author = author
        self.num_pages = num_pages
        
    
    def __str__(self): #this magic method returns a string representaion of the object
        return f"Book: {self.title}; by {self.author}"
    
    
    def __eq__(self, other_book):
        return self.title == other_book.title and self.author == other_book.author # this will return a boolean comparing two objects
    
    
    def __lt__(self, other_book): #magic method of less then (lt)
        return self.num_pages < other_book.num_pages
    
    def __gt__(self, other_book):
        return self.num_pages > other_book.num_pages #magic method of great then (gt)
    
    def __add__(self, other_book): #magic method to add attributes
        return self.num_pages + other_book.num_pages
        
    def __contains__(self, keyword):  #returns a boolean if a key word is in self.tittle
        return keyword in self.title
    
    def __getitem__(self, key):
        if key == "title":
            return self.title
        elif key == "author":
            return self.author
        elif key == 'num_pages':
            return self.num_pages
        else:
            return f"Key {key} was not found"
        
book1 = Book("Lord of the ring", "J.R.R. Tolkien", 310)
book2 = Book("Harry Potter and The Philosopher's Stone", "J.K. Rowling", 223)
book3 = Book("The Lion, the witch and the WardRobe", "C.S. Lewis", 172)
book4 = Book("The Lion, the witch and the WardRobe", "C.S. Lewis", 172)

print(book1) # Book: Lord of the ring; by J.R.R. Tolkien
print(book1 == book2) # False
print(book3 == book4) # True

print(book1 < book2) # False
print(book1 > book2) # True 
print(book1 + book3) # Sum Pages

print("Lord" in book1)# True 

print(book3['title']) # Return the title of book
print(book3['author']) # Return the author of book
print(book3['num_pages']) # Return the number of pages of book
