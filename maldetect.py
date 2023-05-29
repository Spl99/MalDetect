import config
import requests

# Add your API file below.
api_key = config.API_KEY

# Add a loop to the whole program, performs the search, asks user to do it again
while True:
    # Prompt the user to enter the search query
    search_query = input("Enter the Shodan search query (or 'exit' to quit): ")

    # Check if the user wants to exit the loop
    if search_query.lower() == "exit":
        break

    # Construct the API request URL
    api_url = f"https://api.shodan.io/shodan/host/search?key={api_key}&query={search_query}"

    # Send the API request
    response = requests.get(api_url)

    # Handle the API response
    if response.status_code == 200:
        data = response.json()
        # Process the search results
        if 'matches' in data:
            for result in data['matches']:
                # Extract relevant information from the result
                ip = result['ip_str']
                port = result['port']
                print(f"IP: {ip}, Port: {port}")
            if len(data['matches']) == 0:
                print("No search results found.")
        else:
            print("No search results found.")
    else:
        print(f"Error: {response.status_code} - {response.text}")
