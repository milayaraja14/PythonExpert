    """
    day20_pip_demo.py
    Demonstrating the use of the 'requests' package installed via pip.
    """
    
    import requests
    
    def fetch_github_status():
        # We use the requests library to get data from an API
        url = "https://api.github.com"
        
        try:
            response = requests.get(url)
            
            # Check if the request was successful (Status Code 200)
            if response.status_code == 200:
                print("Successfully connected to GitHub API!")
                data = response.json()
                # Accessing data from the returned JSON
                print(f"Current GitHub API URL: {data['current_user_url']}")
            else:
                print(f"Failed with status code: {response.status_code}")
                
        except Exception as e:
            print(f"An error occurred: {e}")
    
    if __name__ == "__main__":
        fetch_github_status()

# Useful pip Commands (Terminal)
# Check the version of pip
    pip --version
    
    # List all installed packages
    pip list
    
    # Show details about a specific package
    pip show requests
    
    # Uninstall a package
    pip uninstall requests -y
