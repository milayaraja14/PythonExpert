# Using Built-in Modules

    import math
    import random
    
    # Using the math module for square roots and constants
    print(f"The value of Pi is: {math.pi}")
    print(f"The square root of 64 is: {math.sqrt(64)}")
    
    # Using the random module to generate a random integer
    lucky_number = random.randint(1, 100)
    print(f"Your lucky number today is: {lucky_number}")

# Creating and Importing a Custom Module

    # Save this as calculator.py
    def add(a, b):
        return a + b
    
    def multiply(a, b):
        return a * b

    #Now, you can import it into your main script:

    # main.py
    import calculator
    
    # Using the functions from our custom module
    result_sum = calculator.add(10, 5)
    result_product = calculator.multiply(10, 5)
    
    print(f"Sum: {result_sum}")       # Output: 15
    print(f"Product: {result_product}") # Output: 50

# Import Variations

    # 1. Importing specific functions (no need to use 'module.function()')
    from math import pi, pow
    
    print(pow(2, 3)) # 2 raised to the power of 3
    
    # 2. Renaming a module with an alias (standard practice for some libraries)
    import statistics as stats
    
    data = [1, 2, 3, 4, 100]
    print(stats.mean(data)) # Calculates the average
