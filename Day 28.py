# Making your first GET Request
    import requests
    
    # The URL of the API endpoint
    url = "https://jsonplaceholder.typicode.com/posts/1"
    
    # Sending a GET request to the server
    response = requests.get(url)
    
    # Check the status code (200 means Success!)
    if response.status_code == 200:
        print("Success! Data retrieved.")
        
        # The data comes back as JSON, we convert it to a Python Dictionary
        data = response.json()
        
        # Accessing specific fields in the dictionary
        print(f"Title: {data['title']}")
        print(f"Body: {data['body']}")
    else:
        print(f"Failed to fetch data. Status code: {response.status_code}")

# Handling a List of Data

    import requests
    
    url = "https://jsonplaceholder.typicode.com/users"
    
    response = requests.get(url)
    
    if response.status_code == 200:
        users = response.json()  # This will be a list of dictionaries
        
        print(f"Found {len(users)} users:\n")
        
        # Loop through the first 3 users
        for user in users[:3]:
            name = user['name']
            email = user['email']
            city = user['address']['city']
            print(f"- {name} lives in {city} (Email: {email})")
    else:
        print("Error connecting to the API.")
