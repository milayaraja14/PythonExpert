    # --- 1. Creating Strings ---
    simple_string = "Hello, Python!"
    multi_line_string = """This is a string that
    spans across multiple
    lines."""
    
    # --- 2. Concatenation & Repetition ---
    first_name = "Guido"
    last_name = "van Rossum"
    full_name = first_name + " " + last_name  # Using + to combine
    greeting = "Hi! " * 3  # Using * to repeat
    
    # --- 3. Indexing and Slicing ---
    # P  y  t  h  o  n
    # 0  1  2  3  4  5
    language = "Python"
    first_letter = language[0]      # 'P'
    last_letter = language[-1]       # 'n' (negative indexing starts from the end)
    substring = language[0:2]        # 'Py' (starts at 0, goes up to but NOT including 2)
    
    # --- 4. String Methods ---
    text = "  python is fun  "
    print(text.upper())              # "  PYTHON IS FUN  "
    print(text.strip())              # "python is fun" (removes leading/trailing whitespace)
    print(text.replace("fun", "wow")) # "  python is wow  "
    
    # --- 5. F-Strings (Modern Formatting) ---
    # This is the preferred way to format strings in Python 3.6+
    age = 30
    message = f"I am {full_name} and I am {age} years old."
    
    print(full_name)
    print(substring)
    print(message)
