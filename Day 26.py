    from flask import Flask, render_template
    
    # Initialize the Flask application
    app = Flask(__name__)
    
    # The 'route' decorator tells Flask which URL should trigger our function
    @app.route('/')
    def home():
        """
        This function runs when a user visits the root URL (127.0.0.1:5000/)
        """
        return "<h1>Welcome to Day 26!</h1><p>Python Web is amazing.</p>"
    
    @app.route('/user/<name>')
    def greet_user(name):
        """
        This is a dynamic route. The <name> part is passed as an argument.
        """
        return f"<h2>Hello, {name}!</h2><p>Welcome to your profile page.</p>"
    
    if __name__ == '__main__':
        # Run the application in debug mode
        # Debug mode allows the server to reload automatically when you save changes
        app.run(debug=True)
