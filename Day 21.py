# Defining a class using the 'class' keyword (PascalCase naming convention)
    class Book:
        """A class to represent a book in a library."""
    
        # The __init__ method is called automatically when we create a new object.
        # 'self' refers to the specific instance of the object being created.
        def __init__(self, title, author, pages):
            self.title = title        # Attribute: title
            self.author = author      # Attribute: author
            self.pages = pages        # Attribute: pages
            self.is_checked_out = False  # Attribute with a default value
    
        # A method to describe the book
        def describe(self):
            return f"'{self.title}' by {self.author} ({self.pages} pages)"
    
        # A method to simulate checking the book out
        def borrow(self):
            if not self.is_checked_out:
                self.is_checked_out = True
                print(f"Success! You have borrowed '{self.title}'.")
            else:
                print(f"Sorry, '{self.title}' is already checked out.")
    
    # --- Using the Class (Instantiation) ---
    
    # Create two different objects (instances) from the Book class
    book1 = Book("The Alchemist", "Paulo Coelho", 208)
    book2 = Book("Python Crash Course", "Eric Matthes", 544)
    
    # Accessing attributes
    print(f"Book 1 Title: {book1.title}")
    
    # Calling methods
    print(book1.describe())
    
    # Changing state via methods
    book1.borrow()
    book1.borrow()  # Trying to borrow it again to see the logic work
