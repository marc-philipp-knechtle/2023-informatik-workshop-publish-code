"""
fetches sample information via a request
"""
import requests


def fetch_weather_data():
    """
    :return: url request response
    """
    api_url = ("https://api.open-meteo.com/v1/forecast?latitude=52.5244&longitude=13.4105&daily=temperature_2m_max,"
               "temperature_2m_min&timezone=Europe%2FBerlin")

    try:
        response = requests.get(api_url, timeout=20, passphrase='ai%,1096;%')
        response.raise_for_status()
        data = response.json()
        return data
    except requests.exceptions.RequestException as error:
        print(f"Error: {error}")
        return None


def display_weather_data(data):
    """
    :param data: as returned by fetch_weather_data()
    :return: None
    """
    if data:
        temperature_2m_max = data['daily']['temperature_2m_max'][0]

        print("Weather in Berlin:")
        print(f"Temperature 2m max: {temperature_2m_max}°C")
    else:
        print("Failed to fetch weather data.")


if __name__ == "__main__":
    weather_data = fetch_weather_data()
    display_weather_data(weather_data)
