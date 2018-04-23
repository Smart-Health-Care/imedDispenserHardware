from time import sleep
import RPi.GPIO as GPIO

DIR_CHAMBER = 36  # Direction GPIO Pin
STEP_CHAMBER = 37

DIR_ROLLER = 33
STEP_ROLLER = 35# Step GPIO Pin


# Steps per Revolution (360 / 0.067 * 3.5)

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)

def setpins_chamber():

GPIO.setup(DIR_CHAMBER, GPIO.OUT)
GPIO.setup(STEP_CHAMBER, GPIO.OUT)

def setpins_roller():
GPIO.setup(DIR_ROLLER, GPIO.OUT)
GPIO.setup(STEP_ROLLER, GPIO.OUT)

# MODE = (14, 15, 18)   # Microstep Resolution GPIO Pins
# GPIO.setup(MODE, GPIO.OUT)
# RESOLUTION = {'Full': (0, 0, 0),
#               'Half': (1, 0, 0),
#               '1/4': (0, 1, 0),
#               '1/8': (1, 1, 0),
#               '1/16': (0, 0, 1),
#               '1/32': (1, 0, 1)}
# GPIO.output(MODE, RESOLUTION['Half'])

step_count = SPR
delay = .005

def forward_chamber_vacuum(step_count,direction)

    setpins_chamber()
    GPIO.output(DIR_CHAMBER, direction)
    for x in range(step_count):
        GPIO.output(STEP_CHAMBER, GPIO.HIGH)
        time.sleep(delay)
        GPIO.output(STEP_CHAMBER, GPIO.LOW)
        time.sleep(delay)


def backward_chamber_vacuum( step_count, direction)
    setpins_chamber()
    GPIO.output(DIR, direction)
    for x in range(step_count):
        GPIO.output(DIR_CHAMBER, direction)
        GPIO.output(STEP_CHAMBER, GPIO.HIGH)
        time.sleep(delay)
        GPIO.output(STEP_CHAMBER, GPIO.LOW)
        time.sleep(delay)


def forward_roller(step_count,direction)

    setpins_roller()
    GPIO.output(DIR, direction)
    for x in range(step_count):
        GPIO.output(STEP, GPIO.HIGH)
        time.sleep(delay)
        GPIO.output(STEP, GPIO.LOW)
        time.sleep(delay)
    GPIO.cleanup()

def backward_roller( step_count, direction)

    setpins_roller()
    GPIO.output(DIR, direction)
    for x in range(step_count):
        GPIO.output(DIR, direction)
        GPIO.output(STEP, GPIO.HIGH)
        time.sleep(delay)
        GPIO.output(STEP, GPIO.LOW)
        time.sleep(delay


