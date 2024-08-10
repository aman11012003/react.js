import request
import json

def get_weather_data(city):
    api_key = 'YOUR_API_KEY'  # Replace 'YOUR_API_KEY' with your actual API key
    base_url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric'
    
    try:
        response = requests.get(base_url)
        data = response.json()

        if data['cod'] == 200:
            return data
        else:
            print(f'Error: {data["message"]}')
            return None
    except Exception as e:
        print(f'An error occurred: {e}')
        return None

def analyze_weather(data):
    if data:
        city = data['name']
        country = data['sys']['country']
        temp = data['main']['temp']
        description = data['weather'][0]['description']

        print(f'Weather analysis for {city}, {country}:')
        print(f'Temperature: {temp}°C')
        print(f'Weather description: {description}')
    else:
        print('Weather data not available.')

# Example usage
city_name = 'London'  # Replace 'London' with the city name you want to analyze
weather_data = get_weather_data(city_name)
analyze_weather(weather_data)
