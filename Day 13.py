# Basic List Comprehension

    # Traditional Way: Squaring numbers 0-5
    squares = []
    for x in range(6):
        squares.append(x**2)
    
    print(f"Traditional: {squares}")
    
    # List Comprehension Way
    # [expression for item in iterable]
    squares_comp = [x**2 for x in range(6)]
    
    print(f"Comprehension: {squares_comp}")

# Adding a Condition (Filtering)

    # Create a list of even numbers from 0 to 10
    evens = [n for n in range(11) if n % 2 == 0]
    
    print(f"Even numbers: {evens}")
    
    # Extracting names that start with 'A'
    names = ["Alice", "Bob", "Amanda", "Charlie", "Austin"]
    a_names = [name for name in names if name.startswith("A")]
    
    print(f"Names starting with A: {a_names}")

# String Manipulation

    languages = ["python", "java", "javascript", "c++"]
    
    # Convert all strings to uppercase
    upper_languages = [lang.upper() for lang in languages]
    
    print(f"Uppercase: {upper_languages}")
