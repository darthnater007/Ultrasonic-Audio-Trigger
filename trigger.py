import RPi.GPIO as GPIO
import random
import time

import pin
import audio

# distance in cm after which the distance will report as 0
max_distance = 150
# it was necessary to set a minimum distance on which not to play audio
min_distance = 5

# the distance in centimeters at which audio should play
trigger_distance = 30   

# speed of sound in cm/s
SPEED_OF_SOUND = 34300

#calculated timeout based on max distance
TIME_OUT = (max_distance * 60) * 0.00001

# get_pulse_timemeasures how long in milliseconds a delivered pulse takes to return to the rangerfinder
def get_pulse_time(pin,level):
    t0 = time.time()
    while(GPIO.input(pin) != level):
        if((time.time() - t0) > TIME_OUT):
            return 0.0
    t0 = time.time()
    while(GPIO.input(pin) == level):
        if((time.time() - t0) > TIME_OUT):
            return 0.0
    pulse_time = (time.time() - t0)
    return pulse_time

# return the distance traveled one way by the pulse
def get_distance():
    activate_rangefinder()
    distance = get_pulse_time(pin.get_pin_number("echo_pin"),GPIO.HIGH) * SPEED_OF_SOUND / 2.0 
    #divide by two because sound travels from and back to the rangefinder
    return distance

# activate_rangefinder initiates a 10us pulse to the rangefinder sensor to activate it
def activate_rangefinder():
    GPIO.output(pin.get_pin_number("trig_pin"), GPIO.HIGH)
    time.sleep(0.00001) #10us
    GPIO.output(pin.get_pin_number("trig_pin"), GPIO.LOW)

# run_ultrasonic_trigger runs the loop that continuously operates the ultrasonic trigger
def run_ultrasonic_trigger():
    while(True):
        distance = get_distance()
        print(str(distance))
        if distance > min_distance and distance <= trigger_distance:
            audio.play_audio()
            print("TRIGGERED!")
            time.sleep(10)
        time.sleep(0.5)
