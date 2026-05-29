    # 1. Creating a Dictionary
    # Keys are usually strings, values can be any data type
    student = {
        "name": "Alice Smith",
        "age": 21,
        "course": "Computer Science",
        "skills": ["Python", "SQL", "Math"]
    }
    
    print(f"Student Data: {student}")
    
    # 2. Accessing Values
    # Accessing using the key inside square brackets
    print(f"Name: {student['name']}")
    
    # Accessing using the .get() method (Safer: returns None if key doesn't exist)
    email = student.get("email", "Email not found")
    print(f"Email Status: {email}")
    
    # 3. Modifying and Adding Items
    student["age"] = 22  # Updating an existing value
    student["graduated"] = False  # Adding a new key-value pair
    print(f"Updated Student: {student}")
    
    # 4. Removing Items
    # .pop() removes the item with the specified key
    removed_value = student.pop("course")
    print(f"Removed Course: {removed_value}")
    
    # 5. Iterating through a Dictionary
    print("\n--- Dictionary Iteration ---")
    for key, value in student.items():
        print(f"{key.capitalize()}: {value}")
    
    # 6. Nested Dictionaries
    classroom = {
        "student_1": {"name": "Bob", "grade": "A"},
        "student_2": {"name": "Eve", "grade": "B+"}
    }
    print(f"\nStudent 1 Name: {classroom['student_1']['name']}")
