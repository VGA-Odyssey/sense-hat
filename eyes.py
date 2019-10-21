from time import sleep
from sense_hat import SenseHat
sense = SenseHat()

w = (150, 150, 150)
b = (0, 0, 255)
e = (0, 0, 0)

image = [
e,e,e,e,e,e,e,e,
e,e,e,e,e,e,e,e,
w,w,w,e,e,w,w,w,
w,w,b,e,e,w,w,b,
w,w,w,e,e,w,w,w,
e,e,e,e,e,e,e,e,
e,e,e,e,e,e,e,e,
e,e,e,e,e,e,e,e
]

sense.set_pixels(image)

rot = 0
while True:
    sleep(1)
    #sense.flip_h()
    rot = (rot + 90) % 360
    sense.set_rotation(rot)
