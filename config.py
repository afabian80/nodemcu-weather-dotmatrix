from json import load


class Config:
    wifi_ssid = None
    wifi_password = None
    location = None
    api_key = None

    def __init__(self, file_name):
        with open(file_name) as json_file:
            config = load(json_file)
            self.wifi_ssid = config['wifi']['ssid']
            self.wifi_password = config['wifi']['password']
            self.location = config['location']
            self.api_key = config['api_key']
