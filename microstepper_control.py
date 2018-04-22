import RPi.GPIO as GPIO
import time

delay=0.02
steps=50

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)


coil_A1= 13
coil_A2 = 11
coil_B1 = 15
coil_B2 = 12

GPIO.setup(coil_A1, GPIO.OUT)
GPIO.setup(coil_A2, GPIO.OUT)
GPIO.setup(coil_B1, GPIO.OUT)
GPIO.setup(coil_B2, GPIO.OUT)

def setStep (w1, w2, w3, w4):
  GPIO.output(coil_A1, w1)
  GPIO.output(coil_A2, w2)
  GPIO.output(coil_B1, w3)
  GPIO.output(coil_B2, w4)

#for i in range(0, steps):

    # setStep(0,1,1,0)
   #  time.sleep(delay)
   #  setStep(0,1,0,1)
    # time.sleep(delay)
    # setStep(1,0,0,1)
  #   time.sleep(delay)
#     setStep(1,0,1,0)
 #    time.sleep(delay)

def forward(delay, steps):
	for i in range(0, steps):
		setStep(1, 0, 1, 0)
		time.sleep(delay)
		setStep(0, 1, 1, 0)
		time.sleep(delay)
		setStep(0, 1, 0, 1)
		time.sleep(delay)
		setStep(1, 0, 0, 1)
		time.sleep(delay)

def backwards(delay, steps):
	for i in range(0, steps):
		setStep(1, 0, 0, 1)
		time.sleep(delay)
		setStep(0, 1, 0, 1)
		time.sleep(delay)
		setStep(0, 1, 1, 0)
		time.sleep(delay)
		setStep(1, 0, 1, 0)
		time.sleep(delay)

backwards(0.002,200)
time.sleep(0.5)
forward(0.002,200)
