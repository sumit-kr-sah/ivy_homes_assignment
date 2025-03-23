import requests
import time

# Base URL for the autocomplete API
BASE_URL = "http://35.200.185.69:8000/v3/autocomplete"

# Delay between requests to avoid overwhelming the server (currently commented out)
DELAY = 0.01  # seconds between requests

# Set to store all unique names fetched from the API
all_names = set()

def fetch_names(query):
    """
    Fetches names from the autocomplete API based on the given query.
    
    Args:
        query (str): The search query to send to the API.
    """
    # Construct the full URL with the query parameter
    url = f"{BASE_URL}?query={query}"
    
    # Send a GET request to the API
    response = requests.get(url)
    
    # Check if the request was successful
    if response.status_code == 200:
        # Parse the JSON response
        data = response.json()
        
        # Check if the 'results' key exists in the response
        if "results" in data:
            # Extract the list of names from the response
            names = data["results"]
            
            # Add the names to the global set of all names
            all_names.update(names)
        else:
            # Print a message if the 'results' key is not found
            print(f"No 'results' key found in the response for query '{query}'")
    else:
        # Print an error message if the request failed
        print(f"Error fetching names for query '{query}': {response.status_code}")

def extract_all_names():
    """
    Extracts all possible names by querying the API with each character in the 
    alphanumeric set (a-z, 0-9). The results are saved to a file.
    """
    # Define the characters to use as queries
    characters = 'abcdefghijklmnopqrstuvwxyz0123456789'
    
    # Loop through each character and fetch names
    for char in characters:
        fetch_names(char)
        
        # Optional: Add a delay between requests (currently commented out)
        # time.sleep(DELAY)      
    
    # Save the extracted names to a file
    with open('extracted_names_3.txt', 'w') as file:
        # Write each name to the file, sorted alphabetically
        for name in sorted(all_names):
            file.write(f"{name}\n")

# Execute the function to extract all names
extract_all_names()

# Print the total number of unique names extracted
print(f"Total unique names extracted: {len(all_names)}")