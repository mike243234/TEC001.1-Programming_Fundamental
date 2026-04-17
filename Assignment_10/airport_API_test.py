import requests

request_url = "http://127.0.0.1:5000/airport/NBAP"
response = requests.get(request_url).json()

print(response)