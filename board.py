import RPi.GPIO as GPIO
import pin

Pins = pin.Pins

#get_pin_status outputs a message describing pin information
def get_pin_status(pin):
    print("Pin Set!")
    pin.get_pin_info()

#configure_pin sets both pin number and i/o status for pin objects
def configure_pin(pin):
    if(pin.in_out == "in"):
        GPIO.setup(pin.number, GPIO.IN)
        get_pin_status(pin)
    elif(pin.in_out == "out"):
        GPIO.setup(pin.number, GPIO.OUT)
        get_pin_status(pin)
    else:
        print("The following pin has not been set, check your pin definition: ")
        pin.get_pin_info()

#setup  set up all defined pins on the board
def setup(Pins):
    GPIO.setmode(GPIO.BOARD)
    for pin in Pins:
        configure_pin(pin)
