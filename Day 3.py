    # --- Arithmetic Operators ---
    a = 10
    b = 3
    
    print("--- Arithmetic ---")
    print(f"Addition: {a} + {b} = {a + b}")         # 13
    print(f"Subtraction: {a} - {b} = {a - b}")      # 7
    print(f"Multiplication: {a} * {b} = {a * b}")   # 30
    print(f"Division: {a} / {b} = {a / b}")         # 3.333...
    print(f"Floor Division: {a} // {b} = {a // b}") # 3 (removes decimals)
    print(f"Modulus: {a} % {b} = {a % b}")           # 1 (the remainder)
    print(f"Exponentiation: {a} ** {b} = {a ** b}") # 1000 (10 to the power of 3)
    
    # --- Assignment Operators ---
    print("\n--- Assignment ---")
    x = 5           # Assign 5 to x
    x += 3          # Equivalent to x = x + 3
    print(f"Value of x after += 3: {x}")
    
    # --- Comparison Operators (Returns Boolean) ---
    print("\n--- Comparison ---")
    print(f"Is {a} equal to {b}? {a == b}")         # False
    print(f"Is {a} not equal to {b}? {a != b}")     # True
    print(f"Is {a} greater than {b}? {a > b}")      # True
    
    # --- Logical Operators ---
    # Used to check multiple conditions
    print("\n--- Logical ---")
    is_sunny = True
    is_warm = False
    
    # Both must be True
    print(f"Is it sunny AND warm? {is_sunny and is_warm}") 
    # At least one must be True
    print(f"Is it sunny OR warm? {is_sunny or is_warm}")   
    # Reverses the result
    print(f"Is it NOT sunny? {not is_sunny}")
