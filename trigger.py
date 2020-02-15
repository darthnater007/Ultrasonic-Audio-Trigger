import RPi.GPIO as GPIO
import random
import time

import pin
import audio

trig_pin_number = pin.trig_pin.number
echo_pin_number = pin.echo_pin.number

max_distance = 150.0 #cm
min_distance = 5.0 #cm
trigger_distance = 30.0 #cm  

SPEED_OF_SOUND = 34300.0 #cm/s
TIME_OUT = max_distance / SPEED_OF_SOUND

# get_pulse_timemeasures how long in seconds a delivered pulse takes to return to the rangerfinder
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
    print(pulse_time, " seconds")
    return pulse_time

# return the distance traveled one way by the pulse
def get_distance():
    activate_rangefinder()
    distance = get_pulse_time(echo_pin_number,GPIO.HIGH) * SPEED_OF_SOUND / 2.0 
    #divide by two because sound travels from and back to the rangefinder
    return distance

# activate_rangefinder initiates a 10us pulse to the rangefinder sensor to activate it
def activate_rangefinder():
    GPIO.output(trig_pin_number, GPIO.HIGH)
    time.sleep(0.00001) #10us
    GPIO.output(trig_pin_number, GPIO.LOW)

# run_ultrasonic_trigger runs the loop that continuously operates the ultrasonic trigger
def run_ultrasonic_trigger():
    while(True):
        distance = get_distance()
        print(str(distance))
        if distance > min_distance and distance <= trigger_distance:
            audio.play()
            print("TRIGGERED!")
            time.sleep(10)
        time.sleep(0.5)
