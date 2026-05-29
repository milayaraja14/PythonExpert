    # --- 1. Creating a Set ---
    # Sets are defined with curly braces {}
    fruits = {"apple", "banana", "cherry", "apple"}
    
    # Notice that "apple" was added twice, but when we print it:
    print(f"Unique fruits: {fruits}")  # Output will only show one 'apple'
    
    # --- 2. Adding and Updating ---
    # Adding a single item
    fruits.add("orange")
    
    # Adding multiple items using update()
    fruits.update(["mango", "grape"])
    print(f"After updates: {fruits}")
    
    # --- 3. Removing Items ---
    # remove() raises an error if the item is not found
    fruits.remove("banana")
    
    # discard() does NOT raise an error if the item is missing
    fruits.discard("watermelon") 
    print(f"After removals: {fruits}")
    
    # --- 4. Mathematical Set Operations ---
    st1 = {"item1", "item2", "item3", "item4"}
    st2 = {"item3", "item4", "item5", "item6"}
    
    # Union: Combine both (removes duplicates)
    all_items = st1.union(st2)
    print(f"Union: {all_items}")
    
    # Intersection: Items present in BOTH sets
    common_items = st1.intersection(st2)
    print(f"Intersection: {common_items}")
    
    # Difference: Items in st1 but NOT in st2
    diff_items = st1.difference(st2)
    print(f"Difference: {diff_items}")
    
    # --- 5. Converting between types ---
    # A common trick to remove duplicates from a list
    numbers_list = [1, 2, 2, 3, 4, 4, 5]
    unique_numbers = list(set(numbers_list))
    print(f"List with duplicates removed: {unique_numbers}")
