import requests

API_KEY = "0b4d9a22eadcf23645e97e869feca388"  # Replace with your actual API key

def kelvin_to_celsius(kelvin):
    return kelvin - 273.15

def get_weather(city):
    url = "https://api.openweathermap.org/data/2.5/weather"
    params = {
        "q": city,
        "appid": API_KEY
    }

    try:
        response = requests.get(url, params=params)
        data = response.json()

        if response.status_code != 200:
            print("Error:", data.get("message", "Unable to fetch data"))
            return

        # Extraction
        description = data["weather"][0]["description"]
        temp_kelvin = data["main"]["temp"]
        temp_celsius = kelvin_to_celsius(temp_kelvin)

        # Outputs
        print(f"\nWeather in {city}:")
        print(f"Condition: {description}")
        print(f"Temperature: {temp_celsius:.2f} °C")

    except requests.exceptions.RequestException:
        print("Network error. Please check your connection.")

if __name__ == "__main__":
    city = input("Enter municipality (city name): ")
    get_weather(city)