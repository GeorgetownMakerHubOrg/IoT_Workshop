#IoT Class Outline

##Introduction

- Establish Terminology/Concepts (1 slide - 15 minutes) - Use Bookmarks
- IoT - Show IFTTT screen
- ESP8266 & Pi & Arduino
- MicroPython
- Git Repo
- What We Will Attempt (1 slide 5 minutes)
- A Modifiable Staples Easy Button - SMS webhook

##Project - ambitious for 90 minutes

###Steps

- Create IFTTT account  & create one recipe without IoT (tbd) (15 minutes)
- Download Git IoT repo from Gtown (download zip) (5 minutes)
- Install ampy (10 minutes)
- USB connect ESP (anticipate driver issues?) (20 minutes)
- Wire ESP & Button (20 minutes)
- ampy --port /dev/tty.wusbxxxx put ez.py (5 minutes)
- Test functionality via print statements (10 minutes)
- Uncomment networking commands and integrate WebHooks UID. (20 minutes)
- Upload and get SMS message (5 minutes)
- Change recipe

##Notes
https://github.com/adafruit/ampy/issues/19 - there might be issues with ampy, Mac, and D1 - use ‘-d 0.5’
