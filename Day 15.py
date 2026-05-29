# Day 15: Python Errors and Exceptions
    
    # 1. SyntaxError: Occurs when the code is not formatted correctly.
    # Uncomment the line below to see: it's missing a closing quote.
    # print("Hello World) 
    
    # 2. NameError: Occurs when a variable is used before it's defined.
    try:
        print(my_variable)
    except NameError as e:
        print(f"NameError caught: {e}")
    
    # 3. TypeError: Occurs when an operation is applied to an object of inappropriate type.
    try:
        # Adding an integer and a string
        result = 10 + "20"
    except TypeError as e:
        print(f"TypeError caught: {e}")
    
    # 4. IndexError: Occurs when trying to access an index outside a list's range.
    numbers = [1, 2, 3]
    try:
        print(numbers[5])
    except IndexError as e:
        print(f"IndexError caught: {e}")
    
    # 5. KeyError: Occurs when a dictionary doesn't have the requested key.
    user = {"name": "Asabeneh", "age": 250}
    try:
        print(user["country"])
    except KeyError as e:
        print(f"KeyError caught: Key {e} not found")
    
    # 6. AttributeError: Occurs when an invalid attribute/method is called.
    import math
    try:
        # math has 'sqrt', but not 'square_root'
        math.square_root(25)
    except AttributeError as e:
        print(f"AttributeError caught: {e}")
    
    # 7. ZeroDivisionError: Occurs when dividing by zero.
    try:
        division = 10 / 0
    except ZeroDivisionError as e:
        print(f"ZeroDivisionError caught: {e}")
