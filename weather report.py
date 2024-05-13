import requests
from datetime import datetime
def weather_location(city):
    """
    Taking from OpenWeatherMap API
    """
    try:
        response = requests.get(
            f"https://api.openweathermap.org/data/2.5/weather?q={city}&units=metric&appid=f1d9c587d07fd8c7642cb855c1d28058"
        )
        response.raise_for_status()  # Raise an exception for 4xx or 5xx status codes
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error")
        return None

def parse_weather_data(data):
    """
    Parse weather data from API response
    """
    if data is None:
        return None
    if data['cod'] == '404':
        return None
    weather = data['weather'][0]['main']
    temp = round(data['main']['temp'])
    humidity = data['main']['humidity']
    sunrise = datetime.fromtimestamp(data['sys']['sunrise']).time()
    sunset = datetime.fromtimestamp(data['sys']['sunset']).time()
    description = data["weather"][0]["description"]
    return weather, temp, humidity ,sunrise, sunset

def display_weather_data(city, weather_data):
    if weather_data is None:
        print("No city found in API with this name or API error")
    else:
       
        weather, temp, humidity,sunrise,sunset = parse_weather_data(weather_data)
        if weather is None:
            print("No city found or API error")
        else:
            print(f"Todays weather report of {city} is here!!!")
            print(f"The weather in {city} is: {weather}")
            print(f"The temperature in {city} is: {temp}ºC")
            print(f"The humidity in {city} is: {humidity}%")
            print(f"The Sunrises in {city} at: {sunrise}")
            print(f"The Sunsets in {city} at: {sunset}")

def main():
    city = input("Enter city: ")
    if not city:
        print("Please enter a city")
        return
    weather_data = weather_location(city)
    display_weather_data(city, weather_data)

main()