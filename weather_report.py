import requests
from datetime import datetime

API_KEY = "b22fb4e46accde8022842efe0793e167"
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"


def get_weather(city_name):
    params = {
        "q": city_name,
        "appid": API_KEY,
        "units": "metric"
    }
    response = requests.get(BASE_URL, params=params)

    if response.status_code == 200:
        data = response.json()
        main = data["main"]
        weather = data["weather"][0]

        # Prepare weather report text
        report = (
            f"Weather Report - {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n"
            f"City: {city_name.title()}\n"
            f"Temperature: {main['temp']} C\n"
            f"Feels Like: {main['feels_like']} C\n"
            f"Humidity: {main['humidity']}%\n"
            f"Condition: {weather['description'].title()}\n"
        )

        # Print to terminal
        print("\n" + report)

        # Save to file with timestamped filename
        filename = f"weather_report_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
        with open(filename, "w", encoding="utf-8") as file:
            file.write(report)

        print(f"[OK] Report saved to {filename}")
    else:
        error_msg = response.json().get('message', 'Unknown error')
        print("\nCould not fetch weather data.")
        print(f"Reason: {error_msg}")


if __name__ == "__main__":
    city = input("Enter city name: ").strip()
    get_weather(city)

    # 👇 Keeps the window open until user presses Enter
    input("\nPress Enter to exit...")





#What it does:
#Asks the user to enter a city name.
#Sends a request to the OpenWeatherMap API to get the current weather data for that city.
#If the city is found:
#Shows a weather report with:
#Temperature
#Feels like temperature
#Humidity
#Weather condition (e.g., clouds, rain)
#Prints the report on the screen.
#Saves the report in a .txt file with the current date and time in the filename.
#If there's an error (like city not found), it shows the reason.
#Waits for the user to press Enter before closing.

