    # --- Example 1: A Simple Function ---
    def greet_user():
        """This function prints a simple greeting."""
        print("Hello! Welcome to Day 11 of Python.")
    
    # To execute the code inside, we must "call" the function
    greet_user()
    
    # --- Example 2: Functions with Parameters ---
    def greet_by_name(name):
        """This function takes a name as an input and greets the user."""
        print(f"Hello, {name}! Glad to see you.")
    
    # 'Alice' is the argument being passed into the parameter 'name'
    greet_by_name("Alice")
    
    # --- Example 3: Returning a Value ---
    def add_numbers(a, b):
        """This function adds two numbers and returns the result."""
        result = a + b
        return result
    
    # We can store the returned value in a variable
    sum_total = add_numbers(10, 5)
    print(f"The sum is: {sum_total}")
    
    # --- Example 4: Default Parameters ---
    def describe_pet(pet_name, animal_type="dog"):
        """Displays information about a pet. animal_type defaults to 'dog'."""
        print(f"I have a {animal_type} named {pet_name}.")
    
    # Using the default value
    describe_pet("Buddy") 
    
    # Overriding the default value
    describe_pet(pet_name="Whiskers", animal_type="cat")
