from network import WLAN, STA_IF
from time import sleep


class WifiConnectError(Exception):
    pass


class Wifi:
    def __init__(self, ssid, password):
        self.ssid = ssid
        self.password = password
        self.wlan = WLAN(STA_IF)

    def connect(self):
        self.wlan.active(True)
        self.wlan.connect(self.ssid, self.password)
        retry = 0
        while not self.wlan.isconnected() and retry < 30:
            retry += 1
            sleep(1)
        if not self.wlan.isconnected():
            raise WifiConnectError()

    def is_connected(self):
        return self.wlan.isconnected()
