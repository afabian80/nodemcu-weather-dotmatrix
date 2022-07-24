from machine import Pin, SPI
from utime import sleep_ms
from max7219 import Max7219


class Display:
    display = None

    def __init__(self, cs_pin, brightness):
        spi = SPI(1, baudrate=10000000)
        self.display = Max7219(width=32, height=8, spi=spi, cs=Pin(cs_pin))
        self.display.brightness(brightness)
        sleep_ms(100)
        self.show_text('init')
        sleep_ms(500)

    def show_text(self, text):
        self.display.fill(0)
        self.display.text(text, 0, 0, 1)
        self.display.show()

    def show_number(self, number):
        text = "{0:4d}".format(number)
        self.show_text(text)
