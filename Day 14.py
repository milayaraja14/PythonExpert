# Passing a Function as an Argument

    def uppercase(text):
        return text.upper()
    
    def greet(func):
        # This is a higher-order function because it takes 'func' as a parameter
        greeting = func("Hello, I am learning Python!")
        print(greeting)
    
    # Note: We pass 'uppercase' without parentheses so we pass the function itself
    greet(uppercase)

# The Map and Filter Functions

    numbers = [1, 2, 3, 4, 5, 6]
    
    # 1. Map: Square every number in the list
    # map(function, iterable)
    squares = list(map(lambda x: x**2, numbers))
    print(f"Squares: {squares}")
    
    # 2. Filter: Only keep even numbers
    # filter(function, iterable)
    evens = list(filter(lambda x: x % 2 == 0, numbers))
    print(f"Evens: {evens}")

# Function Returning a Function (Closures)

    def make_multiplier(n):
        """Returns a function that multiplies its input by n."""
        def multiplier(x):
            return x * n
        return multiplier
    
    # Create a function that doubles numbers
    double = make_multiplier(2)
    # Create a function that triples numbers
    triple = make_multiplier(3)
    
    print(f"Double 5: {double(5)}")  # Output: 10
    print(f"Triple 5: {triple(5)}")  # Output: 15
