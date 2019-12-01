import RPi.GPIO as GPIO
import random
import time

import pin
trig_pin = pin.trig_pin.number
echo_pin = pin.echo_pin.number
import tts

max_distance = 500
trigger_distance = 80          
time_out = (max_distance*60)*0.000001

def measure_results(pin,level,time_out):
    t0 = time.time()
    while(GPIO.input(pin) != level):
        if((time.time() - t0) > time_out):
            return 0.0
    t0 = time.time()
    while(GPIO.input(pin) == level):
        if((time.time() - t0) > time_out):
            return 0.0
    ping_time = (time.time() - t0)*1000000
    return ping_time

def activate_sensor():
    #activate with 10us high level
    GPIO.output(trig_pin,GPIO.HIGH)
    time.sleep(0.00001)     #10us
    GPIO.output(trig_pin,GPIO.LOW)

def get_distance():
    activate_sensor()
    ping_time = measure_results(echo_pin,GPIO.HIGH,time_out)   #read plus time of echoPin
    distance = ping_time * 340.0 / 2.0 / 10000.0
    return distance


def run_ultrasonic_trigger():
    while(True):
        distance = get_distance()
        print(str(distance))
        if distance > 0 and distance <= trigger_distance:
            tts.play_audio()
            print("TRIGGERED!")
            time.sleep(10)
        time.sleep(1)
