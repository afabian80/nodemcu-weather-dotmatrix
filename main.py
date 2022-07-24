from display import Display
from config import Config
from wifi import Wifi, WifiConnectError
from weather import Weather, WeatherUpdateError
from time import sleep
import machine


def log_error(e):
    with open('error.log', 'a') as f:
        f.write(repr(e) + '\n')


def main():
    log_error("normal operation started")
    display = None
    wifi = None
    weather = None
    wifi_errors = 0
    try:
        display = Display(cs_pin=15, brightness=1)
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
            # display.show_text('....')
            # sleep(1)
        except WifiConnectError as e:
            print(e)
            wifi_errors += 1
            display.show_text('wifi')
            log_error(wifi_errors)
            if wifi_errors > 5:
                log_error("resetting")
                sleep(1)
                machine.reset()
            sleep(10)
        except WeatherUpdateError as e:
            print(e)
            display.show_text('svc')
            sleep(10)
        except Exception as e:
            print(e)
            log_error(e)
            display.show_text('shit')
            break


if __name__ == '__main__':
    main()
