#Install the requests package and make a GET request to https://api.github.com.
import requests
response = requests.get('https://api.github.com')
print("Status Code:", response.status_code)
