#!/usr/bin/env python3

#developer: darthnater007

import RPi.GPIO as GPIO

import board
import pin
import trigger

Pins = pin.Pins

if __name__ == '__main__':
    board.setup(Pins)
    try:
        trigger.run_ultrasonic_trigger()
    except KeyboardInterrupt:  #when 'Ctrl+C' is pressed, the program will exit
        print("\nGOODBYE")
        #GPIO.cleanup()   
