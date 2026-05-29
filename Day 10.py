# For Loop

    # Iterating through a list of fruits
    fruits = ["apple", "banana", "cherry"]
    
    print("--- Fruit List ---")
    for fruit in fruits:
        print(f"I love eating {fruit}!")
    
    # Using range(start, stop, step)
    # This will print numbers from 1 to 5
    print("\n--- Counting 1 to 5 ---")
    for i in range(1, 6):
        print(f"Number: {i}")

# While Loop

    # A simple countdown
    count = 5
    
    print("--- Countdown ---")
    while count > 0:
        print(count)
        count -= 1  # Important: decrement count to eventually end the loop
    print("Blast off! 🚀")

# Break and Continue

    print("--- Break and Continue ---")
    for n in range(1, 11):
        if n == 3:
            continue  # Skip the rest of this iteration (skips number 3)
        if n == 7:
            break     # Exit the loop entirely when we hit 7
        print(f"Processing: {n}")

# Nested Loops

    # Multiplication Table (1 to 3)
    print("--- Multiplication Table ---")
    for i in range(1, 4):       # Outer loop
        for j in range(1, 4):   # Inner loop
            print(f"{i} x {j} = {i * j}")
        print("---")
