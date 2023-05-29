import config
import requests

search_query = input("Enter search query: ")
api_key = config.API_KEY

api_url = f"https://api.shodan.io/shodan/host/search?key={api_key}&query={search_query}"

response = requests.get(api_url)

if response.status_code == 200:
	data = response.json()
	if 'matches' in data:
		for result in data['matches']:
			ip = result['ip_str']
			port = result['port']
			print(f"IP: {ip}, Port: {port}")
		else:
			print("No search results found.")
	else:
		print(f"Error: {response.status_code} - {response.text}")

