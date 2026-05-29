    import re
    
    # Sample text for our demonstrations
    text = "Python is amazing. I love learning Python in 2024!"
    
    # 1. re.findall() - Finds all occurrences of a pattern
    # Let's find every instance of 'Python'
    matches = re.findall(r"Python", text)
    print(f"Findall matches: {matches}")  # Output: ['Python', 'Python']
    
    # 2. re.search() - Searches for a pattern and returns a Match object (first occurrence)
    search_obj = re.search(r"amazing", text)
    if search_obj:
        print(f"Match found at index: {search_obj.start()}")
    else:
        print("No match found.")
    
    # 3. Using Meta-characters
    # \d matches any digit (0-9)
    # + means 'one or more'
    digits = re.findall(r"\d+", text)
    print(f"Digits found: {digits}")  # Output: ['2024']
    
    # 4. Character Sets []
    # Let's find words that start with 'l' or 'a'
    # \b represents a word boundary
    words = re.findall(r"\b[la]\w+", text)
    print(f"Words starting with 'l' or 'a': {words}") # Output: ['love', 'learning', 'amazing']
    
    # 5. re.sub() - Replace patterns
    # Replace 'Python' with 'Coding'
    new_text = re.sub(r"Python", "Coding", text)
    print(f"Replaced text: {new_text}")
