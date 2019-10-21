#!/usr/bin/python
# -*- coding: UTF-8 -*-

import random
from time import sleep
from sense_hat import SenseHat
sense = SenseHat()

p = sense.get_humidity()
p = "H: %.0f%%" % p
print(p)
sense.show_message(p)

p = sense.get_temperature()
#p = "%.2f °C" % p
p = "T: %.0fC" % p
print(p)

sense.show_message(p)
p = sense.get_pressure()
p = "P: %.0fmBa" % p
print(p)
sense.show_message(p)

"""
r = random.randint(0,255)
g = random.randint(0,255)
b = random.randint(0,255)
sense.show_letter("&", text_colour=(r,g,b), back_colour=(255-r,255-g,255-b))
sense.set_pixel(0,1,(5,10,15))
sense.show_message("VGA Odyssey",
text_colour=(200,0,128),
back_colour=(0,50,30),
scroll_speed=0.05)
"""
