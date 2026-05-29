    from flask import Flask, jsonify, request
    
    app = Flask(__name__)
    
    # Sample data: In a real app, this would come from a database
    books = [
        {"id": 1, "title": "1984", "author": "George Orwell"},
        {"id": 2, "title": "The Hobbit", "author": "J.R.R. Tolkien"}
    ]
    
    # Route 1: A simple Welcome message (GET)
    @app.route('/', methods=['GET'])
    def home():
        return jsonify({"message": "Welcome to the Day 29 Library API!"})
    
    # Route 2: Get all books (GET)
    @app.route('/api/books', methods=['GET'])
    def get_books():
        # jsonify converts Python lists/dicts into JSON format
        return jsonify({"books": books, "count": len(books)})
    
    # Route 3: Add a new book (POST)
    @app.route('/api/books', methods=['POST'])
    def add_book():
        # request.get_json() gets the data sent by the user
        new_data = request.get_json()
        
        # Basic validation
        if not new_data or 'title' not in new_data:
            return jsonify({"error": "Missing title"}), 400
        
        new_book = {
            "id": len(books) + 1,
            "title": new_data['title'],
            "author": new_data.get('author', 'Unknown')
        }
        
        books.append(new_book)
        return jsonify(new_book), 201
    
    if __name__ == '__main__':
        # run the app in debug mode so it restarts when you save changes
        app.run(debug=True, port=5000)
