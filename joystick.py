#!/usr/bin/python
import random
from sense_hat import SenseHat
sense = SenseHat()
sense.clear()



while True:
    for event in sense.stick.get_events():
        print(event.direction, event.action)

"""
(u'right', u'pressed')
(u'right', u'held')
(u'right', u'held')
(u'right', u'held')
(u'right', u'released')
(u'right', u'pressed')
(u'right', u'held')
(u'right', u'held')
(u'right', u'released')
(u'down', u'pressed')
(u'down', u'held')
(u'down', u'held')
(u'down', u'released')
(u'left', u'pressed')
(u'left', u'held')
(u'left', u'held')
(u'left', u'released')
(u'up', u'pressed')
(u'up', u'held')
(u'up', u'held')
(u'up', u'released')
"""


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
