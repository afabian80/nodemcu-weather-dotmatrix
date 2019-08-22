from display import Display
from config import Config
from wifi import Wifi, WifiConnectError
from weather import Weather, WeatherUpdateError
from time import sleep


def log_error(e):
    with open('error.log', 'a') as f:
        f.write(repr(e) + '\n')


def main():
    log_error("normal operation started")
    display = None
    wifi = None
    weather = None
    try:
        display = Display(cs_pin=15, brightness=4)
        config = Config(file_name='config.json')
        weather = Weather(api_key=config.api_key, location=config.location)
        wifi = Wifi(config.wifi_ssid, config.wifi_password)
    except OSError as e:
        print(e)
        log_error(e)
        display.show_text('E 01')
        return
    except KeyError as e:
        print(e)
        log_error(e)
        display.show_text('E 02')
        return
    except Exception as e:
        print(e)
        log_error(e)
        display.show_text('E 09')
        return

    while True:
        try:
            if not wifi.is_connected():
                wifi.connect()
            weather.update()
            display.show_number(weather.temperature)
            sleep(60)
            display.show_text('UP  ')
            sleep(1)
        except WifiConnectError as e:
            print(e)
            display.show_text('E 11')
            sleep(10)
        except WeatherUpdateError as e:
            print(e)
            display.show_text('E 12')
            sleep(10)
        except Exception as e:
            print(e)
            log_error(e)
            display.show_text('E 19')
            break


if __name__ == '__main__':
    main()
