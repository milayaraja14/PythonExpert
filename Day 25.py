    import pandas as pd
    
    # 1. Creating Data from a Dictionary
    data = {
        "Name": ["Alice", "Bob", "Charlie", "David", "Eve"],
        "Age": [25, 30, 35, 40, 22],
        "City": ["New York", "London", "Paris", "Berlin", "Tokyo"],
        "Score": [85, 92, 78, 88, 95]
    }
    
    # Create a DataFrame (The core Pandas object)
    df = pd.DataFrame(data)
    
    # 2. Basic Exploration
    print("--- Full DataFrame ---")
    print(df)
    
    print("\n--- The First 3 Rows ---")
    print(df.head(3))
    
    print("\n--- Summary Statistics ---")
    print(df.describe()) # Shows mean, min, max, etc.
    
    # 3. Selecting Columns
    print("\n--- Column Selection (Names) ---")
    print(df["Name"])
    
    # 4. Filtering Data
    # Let's find people older than 28
    print("\n--- Filtered Data (Age > 28) ---")
    older_than_28 = df[df["Age"] > 28]
    print(older_than_28)
    
    # 5. Adding a New Column
    # Let's add a column that shows if a student passed (Score > 80)
    df["Passed"] = df["Score"] > 80
    
    print("\n--- Updated DataFrame with 'Passed' Column ---")
    print(df)
    
    # 6. Saving to CSV
    # This creates a file named 'students.csv' without the index numbers
    df.to_csv("students.csv", index=False)
    print("\nData saved to 'students.csv' successfully!")
