import RPi.GPIO as GPIO
from time import sleep
import time

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(3, GPIO.IN)

while True:
       i=GPIO.input(3)
       if i==0:
             print "No intruders",i



       elif i==1:
             print "Intruder detected",i