import os
import time
from sense_hat import SenseHat

sense = SenseHat()

while True:
    sense.clear()
    sense.load_image("balena.png")
    time.sleep(2)
    sense.show_message("balena")
    print "Just sleeping..."
    time.sleep(10)