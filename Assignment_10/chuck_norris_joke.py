import requests

def get_joke():
    url = "https://api.chucknorris.io/jokes/random"
    response = requests.get(url).json()
    print(response["value"])

if __name__ == "__main__":
    get_joke()
