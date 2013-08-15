#!/usr/bin/env python

from time import sleep

import RPi.GPIO as GPIO

# Set GPIO pins
# Outputs
MODE_BTN = 23       # Goes to GoPro pin 12
SHUTTER_BTN = 24    # Goes to GoPro pin 13
# Inputs
STATUS_PIN = 25     # Goes to GoPro pin 24

GPIO.setmode(GPIO.BCM)
GPIO.setup(MODE_BTN,  GPIO.OUT)
GPIO.setup(SHUTTER_BTN, GPIO.OUT)
GPIO.setup(STATUS_PIN, GPIO.IN)

def get_power_state(self):
    if ( GPIO.input(STATUS_PIN) == True ):
        return True
    elif ( GPIO.input(STATUS_PIN) == True ):
        return False

def turnon(self):
    if ( get_power_state() == False ):
        GPIO.output(MODE_BTN, True)
        sleep(1)
        GPIO.output(MODE_BTN, True)
        print("Power on")
    elif ( get_power_state() == True ):
        print("GoPro is already on")

def turnoff(self):
    if ( get_power_state() == True ):
        GPIO.output(MODE_BTN, True)
        sleep(3)
        GPIO.output(MODE_BTN, True)
        print("Power off")
    elif ( get_power_state() == False ):
        print("GoPro is already off")

def toggle_mode(self):
    if ( get_power_state() == True ):
        GPIO.output(MODE_BTN, True)
        sleep(0.25)
        GPIO.output(MODE_BTN, True)
    elif ( get_power_state() == False ):
        print("GoPro is not turned on")

def toggle_shutter(self):
    if ( get_power_state() == True ):
        GPIO.output(SHUTTER_BTN, True)
        sleep(0.25)
        GPIO.output(SHUTTER_BTN, True)
    elif ( get_power_state() == False ):
        print("GoPro is not turned on")
