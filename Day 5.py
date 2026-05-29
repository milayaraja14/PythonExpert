    # --- 1. Creating a List ---
    fruits = ["apple", "banana", "cherry"]
    numbers = [10, 20, 30, 40, 50]
    mixed_list = ["Python", 2023, True, 3.14]
    
    # --- 2. Accessing Items ---
    # Lists are zero-indexed
    print(f"First fruit: {fruits[0]}")  # apple
    print(f"Last fruit: {fruits[-1]}")   # cherry (negative indexing)
    
    # --- 3. Slicing ---
    # [start:stop] - stop index is not included
    print(f"Slice of numbers: {numbers[1:4]}")  # [20, 30, 40]
    
    # --- 4. Modifying a List ---
    fruits[1] = "blueberry"
    print(f"Updated list: {fruits}")
    
    # --- 5. Adding Items ---
    # .append() adds to the end
    fruits.append("orange")
    
    # .insert() adds at a specific index
    fruits.insert(1, "mango")
    print(f"After additions: {fruits}")
    
    # --- 6. Removing Items ---
    # .remove() deletes a specific value
    fruits.remove("apple")
    
    # .pop() removes an item at a specific index (or the last item if empty)
    deleted_item = fruits.pop(0) 
    print(f"Removed item: {deleted_item}")
    print(f"Final list: {fruits}")
    
    # --- 7. List Length ---
    print(f"Number of fruits remaining: {len(fruits)}")
