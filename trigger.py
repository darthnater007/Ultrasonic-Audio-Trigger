import RPi.GPIO as GPIO
import random
import time

import pin
trig_pin = pin.trig_pin.number
echo_pin = pin.echo_pin.number
import tts

max_distance = 150
min_distance = 5
trigger_distance = 30          
time_out = (max_distance*60)

def measure_results(pin,level,time_out):
    t0 = time.time()
    while(GPIO.input(pin) != level):
        if((time.time() - t0) > time_out*0.000001):
            return 0.0
    t0 = time.time()
    while(GPIO.input(pin) == level):
        if((time.time() - t0) > time_out*0.000001):
            return 0.0
    ping_time = (time.time() - t0)*1000000
    return ping_time

def get_distance():
    #activate sensor with 10us high pulse
    GPIO.output(trig_pin, GPIO.HIGH)
    time.sleep(0.00001) #10us
    GPIO.output(trig_pin, GPIO.LOW)
    #get results and measure distance
    ping_time = measure_results(echo_pin,GPIO.HIGH,time_out)   #read pulse time of echoPin
    distance = ping_time * 340.0 / 2.0 / 10000.0
    return distance


def run_ultrasonic_trigger():
    while(True):
        distance = get_distance()
        print(str(distance))
        if distance > min_distance and distance <= trigger_distance:
            tts.play_audio()
            print("TRIGGERED!")
            time.sleep(10)
        time.sleep(1)
