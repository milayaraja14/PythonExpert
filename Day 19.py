# Day 19: File Handling - Writing
    file_path = "example.txt"
    
    # 'with' acts as a context manager. It automatically closes the file for us.
    # 'w' mode: Write (Overwrites existing content or creates a new file)
    with open(file_path, "w") as file:
        file.write("Hello! This is Day 19 of Python.\n")
        file.write("Today we are learning about files.\n")
    
    print(f"Successfully created '{file_path}'")
    
    # 'a' mode: Append (Adds to the end of the file without deleting content)
    with open(file_path, "a") as file:
        file.write("This line was added using the append mode!\n")
    
    print("Content appended successfully.")

# Reading from a File

# Day 19: File Handling - Reading
    file_path = "example.txt"
    
    print("\n--- Reading the entire file ---")
    with open(file_path, "r") as file:
        content = file.read()
        print(content)
    
    print("--- Reading line by line using a loop ---")
    with open(file_path, "r") as file:
        for line in file:
            # strip() removes the extra newline character from the file
            print(f"Line: {line.strip()}")

# Handling CSV Files (Optional but Useful)

    import csv
    
    # Writing to a CSV file
    with open("students.csv", "w", newline="") as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(["Name", "Course", "Progress"])
        writer.writerow(["Alice", "Python", "Day 19"])
        writer.writerow(["Bob", "Python", "Day 5"])
    
    print("\n'students.csv' has been created.")
