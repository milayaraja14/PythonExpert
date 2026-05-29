    import requests
    
    def fetch_data():
        """
        Fetches data from a public API to demonstrate 
        that our virtual environment package is working.
        """
        url = "https://jsonplaceholder.typicode.com/todos/1"
        
        try:
            # We can use 'requests' because it is installed in our venv
            response = requests.get(url)
            response.raise_for_status()
            
            data = response.json()
            print("Successfully fetched data using the 'requests' library!")
            print(f"Title: {data.get('title')}")
            
        except ImportError:
            print("Error: 'requests' library not found. Is your venv active?")
        except Exception as e:
            print(f"An error occurred: {e}")
    
    if __name__ == "__main__":
        fetch_data()
