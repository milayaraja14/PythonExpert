    import pymongo
    
    # 1. Connection
    # If using MongoDB Atlas, replace with your connection string
    # For local: "mongodb://localhost:27017/"
    client = pymongo.MongoClient("mongodb://localhost:27017/")
    
    # 2. Create Database and Collection
    db = client["python_course_db"]
    students = db["students"]
    
    def insert_data():
        """Demonstrates inserting single and multiple documents."""
        # Insert One
        student = {"name": "Alice", "age": 22, "course": "Python"}
        result = students.insert_one(student)
        print(f"Inserted single ID: {result.inserted_id}")
    
        # Insert Many
        student_list = [
            {"name": "Bob", "age": 25, "course": "JavaScript"},
            {"name": "Charlie", "age": 20, "course": "Python"},
            {"name": "David", "age": 23, "course": "Java"}
        ]
        results = students.insert_many(student_list)
        print(f"Inserted IDs: {results.inserted_ids}")
    
    def find_data():
        """Demonstrates querying the database."""
        print("\n--- Finding all students ---")
        for student in students.find():
            print(student)
    
        print("\n--- Finding students taking Python ---")
        query = {"course": "Python"}
        python_students = students.find(query)
        for s in python_students:
            print(s['name'])
    
    def update_data():
        """Demonstrates updating documents."""
        query = {"name": "Alice"}
        new_values = {"$set": {"age": 23}}
        students.update_one(query, new_values)
        print("\nUpdated Alice's age.")
    
    def delete_data():
        """Demonstrates deleting documents."""
        query = {"name": "David"}
        students.delete_one(query)
        print("\nDeleted David from the record.")
    
    if __name__ == "__main__":
        # Run the operations
        insert_data()
        find_data()
        update_data()
        delete_data()
        
        # Check final state
        print("\nFinal Student Count:", students.count_documents({}))
