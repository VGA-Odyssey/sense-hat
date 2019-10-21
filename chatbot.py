#!/usr/bin/python
import random
import requests
from sense_hat import SenseHat
sense = SenseHat()
sense.clear()

while True:
    carl_says = requests.get("https://games.johanv.xyz/carl_api").content

    r = random.randint(128,255)
    g = random.randint(128,255)
    b = random.randint(128,255)
    sense.show_message(carl_says, scroll_speed=0.06, text_colour=(r,g,b))

"""
sense.set_pixel(0,1,(5,10,15))
sense.show_message("VGA Odyssey",
text_colour=(200,0,128),
back_colour=(0,50,30),
scroll_speed=0.05)
"""
