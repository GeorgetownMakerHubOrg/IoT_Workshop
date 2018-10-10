# Micropython code for Georgetown Maker Hub's IoT Workshop

# The monitor uses the following components:
# - ESP8266
# - Simple push button

def do_post():
        import urequests
        from sys import exit
        url = "http://maker.ifttt.com/trigger/onebutton/with/key/ThisIsYourOwnIFTTTKey"
        headers = {'Content-Type': 'application/json\r\n'}
        json='{"value1":"1","value2":"2","value3":"3"}'
        try:
                response = urequests.post(url, headers=headers, json=json)
                # response = urequests.post(url)
                print('Posted on IFTTT')
        except OSError as err:
                print("OS error: {0}".format(err))
                exit()
        else:
                response.close()

def do_connect():
        import network
        SSID = 'GuestNet'
        Password = ''
        wlan = network.WLAN(network.STA_IF)
        wlan.active(True)
        ap = network.WLAN(network.AP_IF) # let's make sure we don't boot as an Access Point
        ap.active(False)
        if not wlan.isconnected():
                print('Connecting to Network...')
                wlan.connect(SSID, Password)
                while not wlan.isconnected():
                        pass
        print('Network Configuration (IP/GW/DNS1/DNS2): ', wlan.ifconfig())

def main():
        from machine import Pin, Signal
        from utime import sleep

        pin2 = Pin(2, Pin.IN, Pin.PULL_UP)   # set GPIO2 as input with pullup
        button = Signal(pin2, invert=True)   # let's use Signals, eh?
        pressed = False

        do_connect()    # On boot, connect.
        while True:
                if not pressed and button.value():  # falling edge - button was pressed
                        print("Button Pressed")
                        pressed = True
                        do_post()
                elif pressed and not button.value():   # rising edge - released button
                        print("Button Released")
                        pressed = False
                sleep(0.01)

