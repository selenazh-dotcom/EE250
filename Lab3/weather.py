# mail_server.py
import requests

# WeatherAPI key
WEATHER_API_KEY = '003a49dffd01437fa23183609261002'  # TODO: Replace with your own WeatherAPI key

def get_weather(city):
    # TODO: Build the API request URL using the base API endpoint, the API key, and the city name provided by the user.
    # TODO: Make the HTTP request to fetch weather data using the 'requests' library.
    payload = {'key': WEATHER_API_KEY, 'q': city, 'api' : 'no'}
    r = requests.get('http://api.weatherapi.com/v1/current.json?', params=payload)
    
    # TODO: Handle HTTP status codes:
    # - Check if the status code is 200 (OK), meaning the request was successful.
    # - If not 200, handle common errors like 400 (Bad Request), 401 (Unauthorized), 404 (Not Found), and any other relevant codes

    if r.status_code == 200:
        # TODO: Parse the JSON data returned by the API. Extract and process the following information:
        # - Current temperature in Fahrenheit
        # - The "feels like" temperature
        # - Weather condition (e.g., sunny, cloudy, rainy)
        # - Humidity percentage
        # - Wind speed and direction
        # - Atmospheric pressure in mb
        # - UV Index value
        # - Cloud cover percentage
        # - Visibility in miles
        data = r.json();
        loc = data.get("location", {})
        cur = data.get("current", {})

        curtemp = cur.get("temp_f")
        feeltemp = cur.get("feelslike_f")
        condition = (cur.get("condition") or {}).get("text")
        humidity = cur.get("humidity")
        windspeed = cur.get("wind_mph")
        winddir = cur.get("wind_dir")
        pressure = cur.get("pressure_mb")
        uvindex = cur.get("uv")
        cloudcov = cur.get("cloud")
        visibility = cur.get("vis_miles")

        # TODO: Display the extracted weather information in a well-formatted manner.
        print(f"Weather data for {city}...")
        print(f"Current temperature: {curtemp}F (Feels like {feeltemp}F)")
        print(f"Condition: {condition}")
        print(f"Humidity: {humidity}")
        print(f"Wind: {windspeed} mph, Direction: {winddir}")
        print(f"Pressure: {pressure} mb")
        print(f"UV Index: {uvindex}")
        print(f"Cloud coverage: {cloudcov}%")
        print(f"Visibility: {visibility} miles")

    else:
        # TODO: Implement error handling for common status codes. Provide meaningful error messages based on the status code.
        if r.status_code == 400:
            print("Error code 400. Bad request, check city name.")
        elif r.status_code == 401:
            pritn("Error code 401. Unauthorized, check API.")
        elif r.status_code == 404:
            print("Error code 404. Not found.")
        else:
            print(f"Error code {r.status_code}. Something went wrong")

if __name__ == '__main__':
    # TODO: Prompt the user to input a city name.
    print("Enter in a city name: ")
    city = input();

    # TODO: Call the 'get_weather' function with the city name provided by the user.
    get_weather(city);

    pass
