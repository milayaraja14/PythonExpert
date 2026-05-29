    import requests
    from bs4 import BeautifulSoup
    
    # Step 1: Define the URL to scrape
    URL = "http://quotes.toscrape.com"
    
    def scrape_quotes():
        # Step 2: Send a GET request to the website
        response = requests.get(URL)
        
        # Check if the request was successful (Status Code 200)
        if response.status_code == 200:
            # Step 3: Parse the HTML content using BeautifulSoup
            soup = BeautifulSoup(response.text, 'html.parser')
            
            # Step 4: Find all elements containing quotes
            # On this site, each quote is inside a <div> with the class 'quote'
            quote_elements = soup.find_all('div', class_='quote')
            
            print(f"--- Top Quotes from {URL} ---\n")
            
            for element in quote_elements:
                # Extract the text of the quote (found in a <span> with class 'text')
                text = element.find('span', class_='text').get_text()
                
                # Extract the author (found in a <small> tag with class 'author')
                author = element.find('small', class_='author').get_text()
                
                print(f"Quote: {text}")
                print(f"By: {author}\n")
        else:
            print(f"Failed to retrieve the webpage. Status code: {response.status_code}")
    
    if __name__ == "__main__":
        scrape_quotes()
