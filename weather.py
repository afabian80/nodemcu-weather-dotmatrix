from urequests import get
from json import loads

URL = 'http://api.openweathermap.org/data/2.5/weather?q={0}&APPID={1}'
KELVIN = 273.15


class WeatherUpdateError(Exception):
    pass


class Weather:
    api_key = None
    location = None
    temperature = None

    def __init__(self, api_key, location):
        self.api_key = api_key
        self.location = location

    def update(self):
        try:
            resp = get(URL.format(self.location, self.api_key))
            data = loads(resp.text)
            temp_fine = float(data['main']['temp']) - KELVIN
            self.temperature = round(temp_fine)
        except:
            raise WeatherUpdateError()
