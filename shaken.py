from sense_hat import SenseHat

sense = SenseHat()

red = (255, 0, 0)

threshold = 1.5

while True:
    acceleration = sense.get_accelerometer_raw()
    x = acceleration['x']
    y = acceleration['y']
    z = acceleration['z']

    x = abs(x)
    y = abs(y)
    z = abs(z)

    if x > threshold or y > threshold or z > threshold:
        sense.show_letter("!", red)
    else:
        sense.clear()
