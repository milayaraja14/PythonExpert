    # 1. Creating Tuples
    # Tuples are defined using parentheses ()
    fruits = ("apple", "banana", "cherry", "apple")
    print(f"Fruit Tuple: {fruits}")
    
    # Note: To create a tuple with only ONE item, you must include a trailing comma
    single_item_tuple = ("orange",)
    print(f"Single item: {type(single_item_tuple)}")
    
    # 2. Accessing Elements
    # Like lists, tuples use zero-based indexing
    print(f"First fruit: {fruits[0]}")
    print(f"Last fruit: {fruits[-1]}")
    
    # 3. Immutability (The 'Immutable' Rule)
    # The following line would raise a TypeError:
    # fruits[1] = "mango" 
    
    # 4. Tuple Unpacking
    # You can extract values into variables in one line
    coordinates = (10, 20, 30)
    x, y, z = coordinates
    print(f"Unpacked values - X: {x}, Y: {y}, Z: {z}")
    
    # 5. Useful Tuple Methods
    # Since tuples can't change, they only have two built-in methods
    print(f"How many apples? {fruits.count('apple')}")
    print(f"Index of 'cherry': {fruits.index('cherry')}")
    
    # 6. Joining Tuples
    # You can't change a tuple, but you can combine two to make a new one
    vegetables = ("carrot", "potato")
    food_basket = fruits + vegetables
    print(f"Combined Basket: {food_basket}")
