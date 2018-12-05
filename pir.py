import RPi.GPIO as GPIO
import time, pygame

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(11, GPIO.IN)         #Read output from PIR motion sensor
GPIO.setup(3, GPIO.OUT)         #LED output pin
pygame.mixer.init()
pygame.mixer.music.load("/home/pi/honk.mp3")

while True:
   i=GPIO.input(11)
   if i==0:                 #When output from motion sensor is LOW
      print("Sleepy time")
      time.sleep(0.1)
   elif i==1:               #When output from motion sensor is HIGH
      print("Intruder detected")
      #GPIO.output(3, 1)  #Turn ON LED
      pygame.mixer.music.play()
      while pygame.mixer.music.get_busy() == True:
         continue
