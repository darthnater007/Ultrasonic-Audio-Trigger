import RPi.GPIO as GPIO
import pin

Pins = pin.Pins

#message for suceesful pin setup
def pin_set_message(pin):
    print("Pin Set!")
    pin.get_pin_info()

#set number and i/o status
def configure_pin(pin):
    if(pin.in_out == "in"):
        GPIO.setup(pin.number, GPIO.IN)
        pin_set_message(pin)
    elif(pin.in_out == "out"):
        GPIO.setup(pin.number, GPIO.OUT)
        pin_set_message(pin)
    else:
        print("The following pin has not been set, check your pin definition: ")
        pin.get_pin_info()

#setup board
def setup(Pins):
    GPIO.setmode(GPIO.BOARD)
    for pin in Pins:
        configure_pin(pin)

setup(Pins)
