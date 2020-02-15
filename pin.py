# The Pin class holds a value for a shorthand name of a pin, the number the pin corresponds with, and wether it should direct or accept current
class Pin:
    def __init__(self, name, number,in_out):
        self.name = name
        self.number = number
        self.in_out = in_out

    def get_pin_info(self):
        print(
            "PIN_INFO:\n"+
            "\tname: " + self.name + "\n" +
            "\tnumber: " + str(self.number) + "\n" +
            "\tIO state: " + self.in_out + "\n\n"
            )

trig_pin = Pin("trig_pin", 11, "out"),
echo_pin = Pin("echo_pin", 16, "in")

Pins = [trig_pin,echo_pin]

