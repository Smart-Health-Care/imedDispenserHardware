import RPi.GPIO as GPIO
from time import sleep
import time

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(3, GPIO.IN)
i = GPIO.input(3)
print(i)

motora = 7
motorb = 8  # Input Pin
motorc = 5  # Enable Pin


def set():
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(motora, GPIO.OUT)
    GPIO.setup(motorb, GPIO.OUT)
    GPIO.setup(motorc, GPIO.OUT)
    GPIO.setwarnings(False)


def backward():
    set()
    GPIO.output(motora, GPIO.HIGH)
    GPIO.output(motorb, GPIO.LOW)
    GPIO.output(motorc, GPIO.HIGH)


def forward():
    set()
    GPIO.output(motora, GPIO.LOW)
    GPIO.output(motorb, GPIO.HIGH)
    GPIO.output(motorc, GPIO.HIGH)


def stop():
    set()
    GPIO.output(motorc, GPIO.LOW)

flag = True
while True:
    if flag:
        print "Waiting for Server Confirmation"
        a = raw_input()
        flag = False
        forward()
        time.sleep(0.5)
    i = GPIO.input(3)
    if i == 0:
        flag = True
        stop()
        time.sleep(0.5)
    else:
        forward()
        time.sleep(0.5)
