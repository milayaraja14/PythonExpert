    # --- Variable Assignment ---
# We use the '=' sign to assign a value to a variable name
first_name = "Alex"
last_name = "Smith"
age = 25
is_student = True

# --- Using Built-in Functions ---

# 1. print(): Outputs data to the console
print("Hello, World!") 
print("Name:", first_name, last_name)

# 2. len(): Returns the length of a string or list
name_length = len(first_name)
print("The first name has", name_length, "letters.")

# 3. type(): Checks the data type of a variable
print(type(first_name))  # Output: <class 'str'>
print(type(age))         # Output: <class 'int'>

# 4. input(): Gets information from the user
# Note: input() always returns data as a string
favorite_color = input("What is your favorite color? ")
print("Your favorite color is " + favorite_color)

# 5. Multiple assignment
x, y, z = 10, 20, 30
print(x, y, z)

# --- Naming Rules (PEP 8) ---
# Variables should be lowercase, words separated by underscores
user_home_address = "123 Python Lane"  # Good
UserHomeAddress = "123 Python Lane"    # Avoid (PascalCase is for Classes)
